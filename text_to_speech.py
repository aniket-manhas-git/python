# pip install pyttsx3
import pyttsx3
text_speech=pyttsx3.init()
text=input("Enter your text : ")
text_speech.say(text)
text_speech.runAndWait()