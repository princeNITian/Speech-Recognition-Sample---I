import pyaudio
import wave
import speech_recognition as sr
import subprocess
from gtts import gTTS 
import os
import pyttsx3


# def say(text):
#     ptts < file.txt
#     echo Hello there|ptts
#     subprocess.call('say',text,shell=True)

def say_with_gtts(mytext, language="en"):
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.wav") 
    # os.system("mpg321 welcome.mp3")

def say_with_pyttsx(text):
    engine = pyttsx3.init()
    engine.say(text)
    # change voice to female
    voices = engine.getProperty('voices')  
    engine.setProperty('voice', voices[1].id)
    #save to a new file
    engine.save_to_file(text,"test.mp3")
    engine.runAndWait()

def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()
    
    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )

    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)
    
    stream.close()
    pa.terminate()


r = sr.Recognizer()

# play_audio("audio/siren.wav")

def initSpeech():
    print('Listening..')

    play_audio('audio/blurp_x.wav')

    with sr.Microphone() as source:
        print("Say something..")
        audio = r.listen(source)

    play_audio("audio/applause3.wav")

    command = ""

    try:
        command = r.recognize_google(audio)
    except:
        print("Couldn't understand you.")

    print('Your command: ')
    print(command)
    # say_with_gtts("You said: "+command)
    # play_audio('welcome.wav')
    say_with_pyttsx("You said: "+command)

initSpeech()