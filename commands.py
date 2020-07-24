import subprocess
import os
import pyttsx3
from get_answer import Fetcher

class Commander:
    def __init__(self):
        self.confirm = ["yes", "affirmative", "si", "sure", "do it", "yeah", "confirm"]
        self.cancel = ["no", "negative", "negative soldier", "don't", "wait", "cancel"]

    def discover(self,text):
        if "what" in text and "name" in text:
            if "my" in text:
                self.respond("You haven't told me your name yet.")
            else:
                self.respond("My name is python commander. How are you?")
        
        # if "launch" or "open" in text:
        #     app = text.split(" ",1)[-1]
        #     self.respond('Opening '+app)
        #     os.system("open -a" +app+ '.app')

    def respond(self, response):
        engine = pyttsx3.init()
        print(response)
        engine.say(response)
        engine.runAndWait()
