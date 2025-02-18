import pyttsx3
import sys

text_speech=pyttsx3.init()

path=input("Enter path of the text file e.g(C:\\file.txt) : ")
path=path.replace('\\','\\\\')
try:
    file=open(path)
except:
    print("Error with file path")
    sys.exit()
a=3
while(a<1 or a>2):
    a=int(input('1. Male voice\n2. Female voice\n'))

voices = text_speech.getProperty('voices')
text_speech.setProperty('voice', voices[a-1].id) 

speed=int(input('Enter rate od reading : '))
text_speech.setProperty('rate',speed)

vol=float(input('Enter value between 0.0 - 1.0 for volume level'))
text_speech.setProperty('volume',vol)

text=file.read()
text_speech.say(text)
text_speech.runAndWait()