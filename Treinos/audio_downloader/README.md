Como usar:
bash# Instalar dependência
pip install yt-dlp

# Rodar interativo (pede a URL no terminal)
python yt_audio_downloader.py

# Ou passar a URL direto
python yt_audio_downloader.py "https://www.youtube.com/watch?v=SEU_VIDEO"

# Também funciona com playlists inteiras
python yt_audio_downloader.py "https://www.youtube.com/playlist?list=..."
O que o script faz:

# Baixa o melhor áudio disponível e converte para MP3
- Suporta vídeo único e playlists (erros em vídeos individuais não travam o restante)
- Salva na pasta downloads/ com o nome original do vídeo
- Exibe progresso em tempo real (%, velocidade, ETA)
- Instala o yt-dlp automaticamente se necessário
- Não baixa de novo se o arquivo já existir


Nota: Para conversão para MP3, o ffmpeg precisa estar instalado no sistema. No Ubuntu/Debian: sudo apt install ffmpeg.

Pequeno ajuste — no Windows o ffmpeg não vem instalado por padrão, então o script precisa lidar com isso. 

# Passo a passo no Windows:
- 1 — Instalar o Python (se ainda não tiver)
Baixe em python.org e marque ✅ "Add Python to PATH" na instalação.
- 2 — Instalar o ffmpeg (necessário para converter para MP3)
Abra o PowerShell como Administrador:
powershellwinget install Gyan.FFmpeg
Feche e reabra o terminal após instalar.
- 3 — Rodar o script
cmdpython yt_audio_downloader.py
Ou arrastar a URL direto:
cmdpython yt_audio_downloader.py "https://youtube.com/watch?v=..."