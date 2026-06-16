# Converter texto em fala
# Danilo Vieira
# 15/07/2021
# requisitos

from gtts import gTTS
# pip install gtts
from playsound import playsound
# pip install playsound

audio = 'audioTeste.mp3'
language = 'pt'
sp = gTTS(text = "Estou aprendendo o python do jeito certo, será?" ,
            lang= language,slow=False)

sp.save(audio)
playsound(audio)
