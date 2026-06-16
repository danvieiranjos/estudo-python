
from gtts import gTTS
# pip install gtts
from playsound import playsound
# pip install playsound

audio = 'audioTeste.mp3'
language = 'pt'
sp = gTTS(text = "Vamos dormir, tá na hora.",
            lang= language,slow=False)

sp.save(audio)
playsound(audio)
