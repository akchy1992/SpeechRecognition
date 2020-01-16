# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Speak something....')
    audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio)
        print('You said : {}'.format(text))
    except:
        print('Sorry not recognised')
        
    
        
        