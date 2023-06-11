import time
import googletrans
from tkinter import *
from googletrans import Translator, constants
translator = Translator()

text = input("Type in text: ")
language = input("Type in source language: ")
fname = input("Type in file name: ")
translations = constants.LANGUAGES

for translation in translations:
    result = translator.translate(text, src=language, dest=translation)
    print("Translating to",constants.LANGUAGES[translation].capitalize(), "...")
    file = open("output\\t" + fname + ".txt", "a", encoding="utf-8")
    file.write('\n' + text + " in "+ constants.LANGUAGES[translation].capitalize() + " -> " + result.text)

time.sleep(2)
print("Done!")



    







