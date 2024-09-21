# epubToAnkiCardsConverter
Loads an epub into distinct words, translates and exports list into ankipro.net flashcard format.

https://ankipro.net/

* '1_unzip.py' extracts the epub into it's xml format
* '2_convert.py' leverages BeautifulSoup to extract rawtext
* '3_flashcards.py' distills the words down to distinct words, translates using googletrans api, and exports in the flashcard format

Flashcards folder holds the results of the Prologue and Chapter 1 as a starting place. Chapter 1 only contains the net new words that were not in the prologue

* Prologue: 201 words
* Chapter 1:
* Total: