# Import gTTS and os library

from gtts import gTTS 
import os
# Reading the text file and store into object called text. My file name is “text.txt”

file = open("text.txt", encoding='utf8').read().replace("\n", " ")

# Passing the text file into gTTS module and store into speech

speech = gTTS(text = str(file), lang = 'vi', slow = False)

#Saving the converted audio in a mp3 file named called ‘voice.mp3’

speech.save("voice.mp3")
# Playing the mp3 file
# os.system("start voice.mp3")