#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class
import time
import speech_recognition as sr
import pyaudio
import threading
from pygame import  mixer
from Customer import Customer

mixer.init(8000)
mixer.music.load('C:\SoundBoard\Cheryl\INTRO\AUTOINTRO.mp3')
mixer.music.play()

# this is called from the background thread

def Respond(speech):
    cust = Customer()
    cust.IProvider = speech
    print()
    if "not interested" in speech:
        print("Recognized you aren't interested")
    else:
        print("Cusetomer said insurance was: " + cust.IProvider)

        mixer.init(8000)
        mixer.music.load('C:\SoundBoard\Cheryl\REBUTTALS\cheryl Long rebuttal.mp3')
        mixer.music.play()


def callback(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        s = recognizer.recognize_google(audio)
        print("Google Speech Recognition thinks you said " + s)
        Respond(s)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source) # we only need to calibrate once, before we start listening

# start listening in the background (note that we don't have to do this inside a `with` statement)
stop_listening = r.listen_in_background(m, callback)
# `stop_listening` is now a function that, when called, stops background listening
# do some other computation for 5 seconds, then stop listening and keep doing other computations


while True:
    time.sleep(0.1) # we're still listening even though the main thread is doing other things




