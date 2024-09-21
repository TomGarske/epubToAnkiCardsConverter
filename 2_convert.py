from os import path, listdir
from bs4 import BeautifulSoup

def getTextFromSoup(soup):
    # Get the whole body tag
    tag = soup.body
 
    # Print each string recursively
    text = "".join(tag.strings).replace("","")
    text = text.split('\n')
    text = [t for t in text if t is not '']
    return text

def loadFilesFromDir(extract_dir):
    text = {}
    for filename in listdir(extract_dir):
        if filename.endswith("html"):
            with open(path.join(extract_dir, filename), "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f.read(), features="lxml")
                text[filename] = getTextFromSoup(soup)
    return text

extract_dir = "data\\extract\\OPS"
output_dir = "data\\rawtext"

files = loadFilesFromDir(extract_dir)
for key in files.keys():
    with open(path.join(output_dir, key + ".txt"), 'w', encoding='utf-8') as fout:
        fout.write("\n".join(files[key]))