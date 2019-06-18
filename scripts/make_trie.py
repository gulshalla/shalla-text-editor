import json
import pickle

with open('dictionary.json', 'r') as file:
    dictionary = json.load(file)

with open('wiki-100k.txt', 'r') as file:
    words = file.readlines()

final_words = []
count = 0
for word in words:
    word = word.strip()
    if count < 20000:
        final_words.append(word)
        count += 1
    elif word in dictionary:
        final_words.append(word)

end = '$'
trie = {}

def make_trie(trie, words):
    for word in words:
        current = trie 
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        current[end] = end 

make_trie(trie, final_words)

with open('words_trie.json', 'w') as file:
    json.dump(trie, file)

with open('words_trie.pkl', 'wb') as file:
    pickle.dump(trie, file, protocol=pickle.HIGHEST_PROTOCOL)

