#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 16:42:18 2021

@author: ridhikhurana
"""

from flask import Flask
from flask import request, render_template
from translate import Translator
from google_trans_new import google_translator

# importing the pyttsx library
import pyttsx3

# initialisation
engine = pyttsx3.init()
import gtts  
from playsound import playsound  


app = Flask(__name__)

@app.route("/")
def translate_text():
    
    translator = google_translator()
    input_text = request.args.get("input_text", "")
    value= translator.translate(input_text, lang_src='en', lang_tgt=request.args.get('language'))
    print(value)
    t1 = gtts.gTTS("welcome")
    t1.save("welcome.mp3")   
    playsound("welcome.mp3")
           
    return render_template('translator.html', value=value)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8081, debug=True)
    

    