Speech Recognition

# Create a virtual environment
virutalenv speechvenv

# Activate virtual environment
source speechvenv/Scripts/activate

# Need to install these
pip install pyglet
pip install speechrecognition
pip install pyaudio

# Nedd to install these packages for our program to speak
-> For Linux
sudo apt-get install gnustep-gui-runtime

-> For Windows
download PTTS
Here I am using gTTS
pip install gTTS
or 
pip install pyttsx3 
-> the best option is pyttsx3 see documentation
