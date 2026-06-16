#!/usr/bin/env python3
"""
YouTube Subtitle Generator
===========================
Gera arquivos de legenda (.srt / .vtt) a partir de vídeos do YouTube.

Estratégia:
  1. Tenta baixar legenda existente (manual ou automática) via yt-dlp
  2. Se não houver legenda disponível, baixa o áudio e transcreve com Whisper

Dependências:
  pip install yt-dlp openai-whisper

Para usar Whisper com GPU (mais rápido):
  pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
"""

import argparse
import os
import sys
import subprocess
import glob
import shutil
import tempfile

# ──────────────────────────────────────────────
# Verificação de dependências
# ──────────────────────────────────────────────

def check_dependency(package: str) -> bool:
    try:
        __import__(package.replace("-", "_"))
        return True
    except ImportError:
        return False


def ensure_dependencies():
    missing = []
    if not check_dependency("yt_dlp"):
        missing.append("yt-dlp")
    if not check_dependency("whisper"):
        missing.append("openai-whisper")

    if missing:
        print(f"[!] Dependências faltando: {', '.join(missing)}")
        print(f"    Instale com: pip install {' '.join(missing)}")
        sys.exit(1)


# ──────────────────────────────────────────────
# Funções principais
# ──────────────────────────────────────────────

def sanitize_filename(name: str) -> str:
    """Remove caracteres inválidos para nomes de arquivo."""
    keepchars = (" ", ".", "_", "-")
    return "".join(c for c in name if c.isalnum() or c in keepchars).rstrip()


def get_video_title(url: str) -> str:
    """Obtém o título do vídeo via yt-dlp."""
    import yt_dlp
    ydl_opts = {"quiet": True, "no_warnings": True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return info.get("title", "video")


def try_download_subtitles(url: str, output_dir: str, lang: str) -> str | None:
    """
    Tenta baixar legenda existente (manual ou automática) via yt-dlp.
    Retorna o caminho do arquivo .vtt/.srt se encontrado, None caso contrário.
    """
    import yt_dlp

    print(f"[1/3] Verificando legendas disponíveis para idioma '{lang}'...")

    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "writesubtitles": True,        # legendas manuais
        "writeautomaticsub": True,     # legendas automáticas
        "subtitleslangs": [lang, f"{lang}-*", "en"],
        "subtitlesformat": "vtt",
        "skip_download": True,
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # Procura arquivo de legenda gerado
    for ext in ("vtt", "srt"):
        files = glob.glob(os.path.join(output_dir, f"*.{ext}"))
        if files:
            print(f"    ✔ Legenda encontrada: {os.path.basename(files[0])}")
            return files[0]

    print("    ✘ Nenhuma legenda disponível no YouTube para este idioma.")
    return None


def download_audio(url: str, output_dir: str) -> str:
    """Baixa apenas o áudio do vídeo em formato mp3."""
    import yt_dlp

    print("[2/3] Baixando áudio para transcrição com Whisper...")

    audio_path = os.path.join(output_dir, "audio.mp3")
    ydl_opts = {
        "format": "bestaudio/best",
        "quiet": False,
        "no_warnings": True,
        "outtmpl": os.path.join(output_dir, "audio.%(ext)s"),
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # yt-dlp pode gerar audio.mp3 ou audio.m4a etc.
    for f in glob.glob(os.path.join(output_dir, "audio.*")):
        return f

    raise FileNotFoundError("Falha ao baixar o áudio.")


def transcribe_with_whisper(audio_path: str, output_dir: str, lang: str, model_size: str) -> str:
    """Transcreve o áudio com Whisper e salva como .srt."""
    import whisper

    print(f"[3/3] Transcrevendo com Whisper (modelo: {model_size})...")
    print("      Isso pode demorar alguns minutos dependendo do hardware.")

    model = whisper.load_model(model_size)

    whisper_lang = lang if lang != "auto" else None
    result = model.transcribe(audio_path, language=whisper_lang, verbose=False)

    # Gera SRT
    srt_path = os.path.join(output_dir, "transcricao_whisper.srt")
    with open(srt_path, "w", encoding="utf-8") as f:
        for i, seg in enumerate(result["segments"], start=1):
            start = format_timestamp(seg["start"])
            end   = format_timestamp(seg["end"])
            text  = seg["text"].strip()
            f.write(f"{i}\n{start} --> {end}\n{text}\n\n")

    print(f"    ✔ Transcrição salva em: {srt_path}")
    return srt_path


def format_timestamp(seconds: float) -> str:
    """Converte segundos para formato SRT: HH:MM:SS,mmm"""
    millis = int((seconds % 1) * 1000)
    s = int(seconds)
    h, remainder = divmod(s, 3600)
    m, sec = divmod(remainder, 60)
    return f"{h:02d}:{m:02d}:{sec:02d},{millis:03d}"


def vtt_to_srt(vtt_path: str) -> str:
    """Converte .vtt para .srt (formato mais compatível)."""
    srt_path = vtt_path.replace(".vtt", ".srt")
    with open(vtt_path, encoding="utf-8") as f:
        lines = f.readlines()

    srt_lines = []
    counter = 1
    i = 0

    while i < len(lines):
        line = lines[i].strip()

        # Pula cabeçalho WEBVTT e tags de estilo
        if line.startswith("WEBVTT") or line.startswith("NOTE") or line.startswith("STYLE"):
            i += 1
            continue

        # Detecta linha de timestamp
        if "-->" in line:
            # Converte timestamp vtt → srt (. → ,)
            timestamp = line.replace(".", ",")
            # Remove posicionamento extra ex: "00:00:01.000 --> 00:00:02.000 align:start position:0%"
            timestamp = " --> ".join(p.split(" ")[0] for p in timestamp.split(" --> "))

            # Coleta texto da legenda
            text_lines = []
            i += 1
            while i < len(lines) and lines[i].strip() != "":
                text = lines[i].strip()
                # Remove tags HTML como <c>, </c>, <00:00:01.000>
                import re
                text = re.sub(r"<[^>]+>", "", text)
                if text:
                    text_lines.append(text)
                i += 1

            if text_lines:
                srt_lines.append(str(counter))
                srt_lines.append(timestamp)
                srt_lines.extend(text_lines)
                srt_lines.append("")
                counter += 1
        else:
            i += 1

    with open(srt_path, "w", encoding="utf-8") as f:
        f.write("\n".join(srt_lines))

    return srt_path


# ──────────────────────────────────────────────
# Ponto de entrada
# ──────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Gera legenda .srt de vídeos do YouTube via yt-dlp + Whisper"
    )
    parser.add_argument("url", help="URL do vídeo do YouTube")
    parser.add_argument(
        "-l", "--lang",
        default="pt",
        help="Idioma da legenda: pt, en, es, auto (padrão: pt)"
    )
    parser.add_argument(
        "-m", "--model",
        default="small",
        choices=["tiny", "base", "small", "medium", "large"],
        help="Tamanho do modelo Whisper (padrão: small). Maior = mais preciso, mais lento."
    )
    parser.add_argument(
        "-o", "--output",
        default=".",
        help="Diretório de saída (padrão: diretório atual)"
    )
    parser.add_argument(
        "--force-whisper",
        action="store_true",
        help="Ignora legendas do YouTube e força transcrição via Whisper"
    )
    parser.add_argument(
        "--keep-audio",
        action="store_true",
        help="Mantém o arquivo de áudio após a transcrição"
    )

    args = parser.parse_args()

    ensure_dependencies()

    output_dir = os.path.abspath(args.output)
    os.makedirs(output_dir, exist_ok=True)

    print(f"\n{'='*55}")
    print(f"  YouTube Subtitle Generator")
    print(f"{'='*55}")
    print(f"  URL   : {args.url}")
    print(f"  Idioma: {args.lang}")
    print(f"  Saída : {output_dir}")
    print(f"{'='*55}\n")

    final_srt = None

    # ── Etapa 1: tenta legenda nativa do YouTube ──
    if not args.force_whisper:
        with tempfile.TemporaryDirectory() as tmpdir:
            sub_file = try_download_subtitles(args.url, tmpdir, args.lang)
            if sub_file:
                # Converte vtt → srt se necessário
                if sub_file.endswith(".vtt"):
                    sub_file = vtt_to_srt(sub_file)

                # Move para output_dir
                dest = os.path.join(output_dir, os.path.basename(sub_file))
                shutil.copy(sub_file, dest)
                final_srt = dest

    # ── Etapa 2: transcrição via Whisper ──
    if final_srt is None:
        with tempfile.TemporaryDirectory() as tmpdir:
            audio_path = download_audio(args.url, tmpdir)
            final_srt  = transcribe_with_whisper(audio_path, output_dir, args.lang, args.model)

            if args.keep_audio:
                audio_dest = os.path.join(output_dir, os.path.basename(audio_path))
                shutil.copy(audio_path, audio_dest)
                print(f"    Áudio mantido em: {audio_dest}")

    print(f"\n✅ Legenda gerada com sucesso!")
    print(f"   Arquivo: {final_srt}\n")


if __name__ == "__main__":
    main()
