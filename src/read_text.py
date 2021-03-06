import pyttsx3
import os
engine = pyttsx3.init('sapi5')
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
engine.setProperty('volume',1.0)

def read_text_out(text):
    engine.say(text)
    print(text)
    engine.runAndWait()
    # engine.stop()

from gtts import gTTS 
from playsound import playsound
import os
language = 'en'

def read_text_out_2(text):
    gtts_obj = gTTS(text=text, lang=language, slow=False) 
    gtts_obj.save("morning.mp3") 
    playsound("morning.mp3")
    os.remove("morning.mp3")
    print(text)