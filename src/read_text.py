import pyttsx3
import os
import tempfile
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
language = 'en'

def read_text_out_2(text):
    gtts_obj = gTTS(text=text, lang=language, slow=False) 
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp_file:
        tmp_filename = tmp_file.name
    gtts_obj.save(tmp_filename)
    playsound(tmp_filename)
    os.remove(tmp_filename)
    print(text)