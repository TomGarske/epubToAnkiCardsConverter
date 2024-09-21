# epubToAnkiCardsConverter
Loads an epub into distinct words, translates from Russian to English, and exports list into ankipro.net flashcard format.

https://ankipro.net/

* '1_unzip.py' extracts the epub into it's xml format
* '2_convert.py' leverages BeautifulSoup to extract rawtext
* '3_flashcards.py' distills the words down to distinct words, translates using googletrans api, and exports in the flashcard format
