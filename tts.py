from gtts import gTTS 
from playsound import playsound

def speak(obj):
    t1 = gTTS(text=str(obj), lang='en-in', slow=False)  
    t1.save("welcome.mp3")
    playsound("welcome.mp3")

#speak(input())