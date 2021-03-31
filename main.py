# Import Module Googe Translate
# https://pypi.org/project/googletrans/
# Created By Mohammad Haselmehri
from googletrans import Translator
import speech_recognition as sr
import moviepy.editor as mp

# Create Instance From Class Translator
# Open Your Video
clip = mp.VideoFileClip(r"Your_file.mp4")

clip.audio.write_audiofile(r"converted.wav")
r = sr.Recognizer()
audio = sr.AudioFile("converted.wav")
with audio as source:
    audio_file = r.record(source)
result = r.recognize_google(audio_file)
with open('recognized.txt', mode='w') as file:
    file.write("\n")
    file.write(result)
    print("ready!")
translator = Translator()
eng_txt = open('recognized.txt', 'r')
converted_file = open('converted_language.txt', 'w+')
for eng_line in eng_txt.readlines():
    translation = translator.translate(eng_line, dest="fa")
    converted_file.write(translation.text + '\n')
converted_file.close()
