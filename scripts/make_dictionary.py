import json_lines 
import json 
import pickle

#english thesaurus -- available at https://github.com/zaibacu/thesaurus
thesaurus = {}
with open('en_thesaurus.jsonl', 'rb') as file:
    for item in json_lines.reader(file):
        thesaurus[item['word']] = item

#english dictionary -- available at https://github.com/matthewreagan/WebstersEnglishDictionary
with open('dictionary.json', 'r') as file:
    dictionary = json.load(file)

#list of english words -- available at https://github.com/dwyl/english-words
with open('words.txt', 'r') as file:
    words = file.readlines()

final_dict = {}

for word in dictionary:
    meaning = dictionary[word]
    meaning = meaning.split(';')
    meaning = meaning[0]
    j = 50
    while j < len(meaning) and meaning[j] != '.':
        j += 1
    if j < len(meaning): meaning = meaning[:j + 1]
    dictionary[word] = meaning

keys = []
for word in dictionary:
    if len(dictionary[word]) > 100:
        keys.append(word)

for key in keys:
    dictionary.pop(key)

for word in dictionary:
    if word in thesaurus:
        final_dict[word] = [dictionary[word], thesaurus[word]['synonyms']]
    else:
        final_dict[word] = dictionary[word]

for word in words:
    word = word.lower().strip()
    if word not in final_dict:
        final_dict[word] = 1

with open('dict_thesaurus.json', 'w') as file:
    json.dump(final_dict, file)

with open('dict_thesaurus.pkl', 'wb') as file:
    pickle.dump(final_dict, file, protocol = pickle.HIGHEST_PROTOCOL)