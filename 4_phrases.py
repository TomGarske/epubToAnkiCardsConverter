from googletrans import Translator
from os import path
import os
import string

rawtext_dir = "data\\rawtext"
flashcard_dir = "data\\flashcards"

def writeFile(dir, file, data):
    if not os.path.exists(dir):
        os.makedirs(dir)
    with open(path.join(dir,file), 'w', encoding='utf-8') as fout:
        fout.write("\n".join(data))

def readFile(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
        text = text.lower()
    return text

text = readFile("data\\rawtext\\ch1-3.xhtml.txt")
paragraphs = [p for p in text.split("\n")]
sentences = [s for s in ".".join(paragraphs).split(".")]
phrases = [ph for ph in ",".join(sentences).split(",")]

wordlookup = {}
for phrase in phrases:
    words = [word.strip(string.punctuation) for word in phrase.split() if word.strip(string.punctuation).isalnum()]
    for word in words:
        if word not in wordlookup.keys():
            wordlookup[word] = phrase.strip()

words = [key + "\n" + wordlookup[key] for key in wordlookup.keys()]

translator = Translator()
translations = translator.translate(words, src='ru', dest='en')

flashcards = []
for translation in translations:
    flashcards.append(translation.origin + '|' + translation.text)
flashcards = ";".join(flashcards)
writeFile(flashcard_dir, "prologue_phrases.txt", flashcards)