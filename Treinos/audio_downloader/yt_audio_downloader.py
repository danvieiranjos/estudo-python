#!/usr/bin/env python3
"""
YouTube Audio Downloader - Windows
Baixa o áudio de vídeos ou playlists do YouTube em formato MP3.
"""

import subprocess
import sys
import os
import shutil


# ─────────────────────────────────────────
# Configurações
# ─────────────────────────────────────────
PASTA_SAIDA = os.path.join(os.path.expanduser("~"), "Music", "YouTube")
QUALIDADE   = "192"   # kbps: "128", "192" ou "320"
# ─────────────────────────────────────────


def instalar_yt_dlp():
    try:
        import yt_dlp  # noqa: F401
    except ImportError:
        print("[*] Instalando yt-dlp...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp", "-q"])
        print("[+] yt-dlp instalado.\n")


def localizar_ffmpeg() -> str | None:
    """
    Retorna o caminho do ffmpeg ou None se não encontrado.
    Procura: PATH do sistema → mesma pasta do script.
    """
    # 1) PATH do sistema
    caminho = shutil.which("ffmpeg")
    if caminho:
        return os.path.dirname(caminho)

    # 2) Pasta do próprio script (ffmpeg portátil)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    if os.path.isfile(os.path.join(script_dir, "ffmpeg.exe")):
        return script_dir

    # 3) Localização padrão do winget no Windows
    winget_path = os.path.join(
        os.environ.get("LOCALAPPDATA", ""),
        "Microsoft", "WinGet", "Packages"
    )
    for root, dirs, files in os.walk(winget_path):
        if "ffmpeg.exe" in files:
            return root

    return None


def orientar_instalacao_ffmpeg():
    print("\n" + "=" * 60)
    print("  ERRO: ffmpeg não encontrado")
    print("=" * 60)
    print("""
Instale o ffmpeg com um dos métodos abaixo e rode o script novamente:

  OPÇÃO 1 — winget (PowerShell como Administrador):
    > winget install Gyan.FFmpeg

  OPÇÃO 2 — Chocolatey:
    > choco install ffmpeg

  OPÇÃO 3 — Portátil (sem instalar):
    Baixe em https://www.gyan.dev/ffmpeg/builds/
    Extraia e coloque ffmpeg.exe na mesma pasta deste script.
""")
    input("Pressione ENTER para sair...")
    sys.exit(1)


def hook_progresso(d: dict):
    if d["status"] == "downloading":
        pct        = d.get("_percent_str", "?%").strip()
        velocidade = d.get("_speed_str", "?").strip()
        eta        = d.get("_eta_str", "?").strip()
        print(f"\r  {pct} | {velocidade} | ETA: {eta}    ", end="", flush=True)
    elif d["status"] == "finished":
        print(f"\n  [+] Arquivo baixado, convertendo para MP3...")
    elif d["status"] == "error":
        print(f"\n  [!] Erro: {d.get('filename', 'desconhecido')}")


def baixar_audio(url: str, ffmpeg_dir: str):
    import yt_dlp

    os.makedirs(PASTA_SAIDA, exist_ok=True)

    opcoes = {
        # Força download do melhor áudio disponível
        "format": "bestaudio/best",

        # Salva temporariamente com extensão original
        "outtmpl": os.path.join(PASTA_SAIDA, "%(title)s.%(ext)s"),

        # Pós-processadores: conversão para MP3 + metadados
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": QUALIDADE,
            },
            {
                "key": "FFmpegMetadata",
                "add_metadata": True,
            },
        ],

        # Caminho explícito do ffmpeg — evita "not found" mesmo com PATH correto
        "ffmpeg_location": ffmpeg_dir,

        "progress_hooks": [hook_progresso],
        "nooverwrites": True,
        "ignoreerrors": True,
        "windowsfilenames": True,   # remove caracteres inválidos no Windows
        "quiet": False,
        "no_warnings": False,

        # Força recodificação mesmo que o codec já seja compatível
        "postprocessor_args": {
            "ffmpeg": ["-ar", "44100"]  # taxa de amostragem padrão
        },
    }

    print(f"\n[>] URL      : {url}")
    print(f"[>] Destino  : {PASTA_SAIDA}")
    print(f"[>] Qualidade: {QUALIDADE} kbps")
    print(f"[>] ffmpeg   : {ffmpeg_dir}\n")

    with yt_dlp.YoutubeDL(opcoes) as ydl:
        ydl.download([url])

    # Confirma arquivos MP3 gerados
    mp3s = [f for f in os.listdir(PASTA_SAIDA) if f.endswith(".mp3")]
    print(f"\n[✓] Concluído! {len(mp3s)} arquivo(s) MP3 em:\n    {PASTA_SAIDA}\n")


def main():
    instalar_yt_dlp()

    ffmpeg_dir = localizar_ffmpeg()
    if not ffmpeg_dir:
        orientar_instalacao_ffmpeg()

    if len(sys.argv) > 1:
        url = sys.argv[1].strip()
    else:
        url = input("Cole a URL do YouTube (vídeo ou playlist): ").strip()

    if not url:
        print("[!] Nenhuma URL fornecida.")
        sys.exit(1)

    baixar_audio(url, ffmpeg_dir)

    if sys.stdin and sys.stdin.isatty():
        input("Pressione ENTER para sair...")


if __name__ == "__main__":
    main()
