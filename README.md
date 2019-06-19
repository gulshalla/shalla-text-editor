

Shalla Editor
=====================

This repository contains a text editor built using Python and PyQt.

![alt text](https://github.com/gulshalla/shalla-text-editor/blob/master/icons/screen.png "Screen shot")

## Install 

To run the editor you will need Python3 and PyQt5. Install PyQt by running:
```bash
pip3 install --user pyqt5  
sudo apt-get install python3-pyqt5  
sudo apt-get install pyqt5-dev-tools
sudo apt-get install qttools5-dev-tools
```
The app can be started by simply running:

```python3
python3 app.py
```
You will need the dev tools if you want to generate your own UI's using the PyQt Designer. Visit this [link](https://gist.github.com/ujjwal96/1dcd57542bdaf3c9d1b0dd526ccd44ff) for more details. 

Make sure you have the latest version of PyQt(5.1.2). The app has been tested using Python 3.5.2 and Ubuntu 16.04.

## Features

#### Basic formatting
You can set the font, color, size etc. Text can be set to bold, underlined, highlighted and more. Tables and images can be inserted. The behaviour of these features is similar to standard text editors. 

#### Dictionary, thesaurus, spell checking
The editor loads a dictionary stored as pickle file. The key, value pairs of this dictionary is as follows:
```
word(key) -> [definition, synonyms](value)
```
Words stored in the dictionary have been taken from this [link](https://github.com/dwyl/english-words).
Definitions have been taken from this [link](https://github.com/matthewreagan/WebstersEnglishDictionary).
Synonyms have been taken from this [link](https://github.com/zaibacu/thesaurus).

The script to process the files is in the ```scripts``` folder. To save on space the synonyms and definitions of every word have not been included. Also each word has only one definition. These are the approximate sizes of the final lists:

```
Words: 500,000
Synonyms: 40,000
Definitions: 50,000
```

To use the dictionary or thesaurus, select some text and click the respective buttons in the toolbar. You can also right click the selection to open a custom context menu. This will open a dialog box with the result. 

Running spell check will underline and set the font to red for all words not in the dictionary. 

#### Find, replace, partial matches

The behaviour of find and replace is standard. The partial matches widget returns all the words in the document that contain a part of the search word. This is implemented using Rabin Karp pattern matching. The hash function used is the Rabin Karp fingerprint. Tor read more about it check out this [link](https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm). 

#### Autocomplete

While typing, on pressing Ctrl+Space, a drop down menu will open showing the possible matches. On pressing the Tab key, the first word in the menu is selected. Otherwise you can scroll through the menu and press the Return key. Pressing Ctrl+E will directly complete the first choice.

The back end of this feature is implemented using two Tries. You can read about them [here](https://en.wikipedia.org/wiki/Trie). 

![alt text](https://github.com/gulshalla/shalla-text-editor/blob/master/icons/auto.png "Screen shot")

The global trie is created using the words list in this link. The local trie is initially empty. Whenever a space  separated word is typed, the word is inserted into it. The words are also inserted into a queue. If the size of  the trie becomes larger than 10,000, the word at the front of the queue is popped and removed from the trie. 

The suggestions list size can be up to 10 words long. If we can't find 10 matches in the local trie, the global is used. Completion suffixes are selected randomly from the tries.

#### Spelling Suggestions

If a word is not present in the dictionary, the spelling suggestions module will return a list of the top 5 closest matches to it. For every prefix in the search word, the trie is traversed. For example for the word 'truverse' the following prefixes will be searched for in the trie:

```
t
tr
tru
truv
truve
truver
truvers
```

For every search, the limit of the number of words it returns is set to 50. The result of all the words is combined in a list and the Levenshtein distance with the original word is calculated for every word in the list. You can read more about Levenshtein distances [here](https://en.wikipedia.org/wiki/Levenshtein_distance). The 5 words with the least distance are returned.

 

 


