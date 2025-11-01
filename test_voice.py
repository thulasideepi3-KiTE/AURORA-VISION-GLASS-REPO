from gtts import gTTS
import os

text = "Hi Deepa! Your text to speech system is working perfectly!"
tts = gTTS(text=text, lang='en')
tts.save("test.mp3")
os.system("start test.mp3")
