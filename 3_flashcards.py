from googletrans import Translator
from os import path, listdir
import os
import string
import time

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

def getWordSet(text):
    paragraphs = text.split("\n")
    words = []
    for paragraph in paragraphs:
        words.extend([word.strip(string.punctuation) for word in paragraph.split() if word.strip(string.punctuation).isalnum()])
    wordSet = list(set(words))
    return wordSet

def chunkData(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def createFlashcards(data):
    flashcards = []
    # 15K character Limit and will time out if you hit it too many times
    translations = []
    chunks = list(chunkData(data, 100))
    for count, chunk in enumerate(chunks):
        print(count, "out of", len(chunks))
        translator = Translator()
        result = translator.translate(chunk, src='ru', dest='en')
        translations.extend(result)
    for translation in translations:
        flashcards.append(translation.origin + '|' + translation.text)
    return flashcards

def loadFilesFromDir(dir):
    files = {}
    # TODO: get this to sort human readable - currently it's doing ch1, ch10, ch11 ... 
    for filename in listdir(dir):
        if filename.endswith("txt"):
            with open(path.join(dir, filename), "r", encoding="utf-8") as f:
                text = f.read()
                files[filename] = text.lower()
    return files

def processChapter(text, file, allwords):
    wordSet = getWordSet(text)
    new_words = [w for w in wordSet if w not in allwords]
    flashcards = createFlashcards(new_words)
    writeFile(flashcard_dir, file, flashcards)
    allwords.extend(new_words)
    return allwords

allwords = []
files = loadFilesFromDir(rawtext_dir)
for file in files.keys():
    text = files[file]
    allwords = processChapter(text, file, allwords)
flashcards = createFlashcards(allwords)
writeFile(flashcard_dir, "allwords.txt", flashcards)