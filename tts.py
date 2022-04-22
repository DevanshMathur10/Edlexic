from gtts import gTTS 
from playsound import playsound
import os

def speak(obj):
    
    t1 = gTTS(text=str(obj), lang='en', slow=False)  
    t1.save("welcome.mp3")
    playsound("welcome.mp3")
    os.remove("welcome.mp3")

#speak(input())