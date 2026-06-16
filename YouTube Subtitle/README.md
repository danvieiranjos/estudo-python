# Estratégia em duas etapas:

- Legenda nativa do YouTube — usa yt-dlp para baixar legenda manual ou automática já existente (.vtt), converte para .srt
- Fallback via Whisper — se não houver legenda disponível, baixa o áudio e transcreve localmente com o OpenAI Whisper

# Instalação das dependências:
bashpip install yt-dlp openai-whisper

# Uso básico:
bash python youtube_subtitle_generator.py https://youtu.be/bSk0_oy15iE

# Opções disponíveis:
bash# Especificar idioma
python youtube_subtitle_generator.py URL -l pt

# Forçar Whisper (ignora legenda do YouTube)
python youtube_subtitle_generator.py URL --force-whisper

# Escolher modelo Whisper (tiny/base/small/medium/large)
python youtube_subtitle_generator.py URL -m medium

# Definir pasta de saída
python youtube_subtitle_generator.py URL -o ./legendas

# Manter o áudio após transcrição
python youtube_subtitle_generator.py URL --keep-audio