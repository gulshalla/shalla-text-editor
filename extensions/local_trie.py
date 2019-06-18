import random

class LocalTrie:

    def __init__(self, parent):
        self.trie = {}
        self.size = 0
        self.parent = parent

    def insert(self, word):
        
        def insert_word(word):
            current = self.trie 
            for char in word:
                if char not in current:
                    current[char] = {}
                current = current[char]
            current['$'] = '$'
        
        if self.size < 10000:
            insert_word(word)
            self.size += 1
        else:
            word = self.chose_trie_word()
            self.delete_word_trie(self, word)
            insert_word(word) 
        

    def delete_word_trie(self, word):
        current_dict = self.trie
        path = [current_dict]
        for letter in word:
            current_dict = current_dict.get(letter, None)
            path.append(current_dict)
            if current_dict is None:
                # the trie doesn't contain this word.
                break
        else:
            if not path[-1].get('$', None):
                # the trie doesn't contain this word (but a prefix of it).
                return
            deleted_branches = []
            for current_dict, letter in zip(reversed(path[:-1]), reversed(word)):
                if len(current_dict[letter]) <= 1:
                    deleted_branches.append((current_dict, letter))
                else:
                    break
            if len(deleted_branches) > 0:
                del deleted_branches[-1][0][deleted_branches[-1][1]]
            del path[-1]['$']


    def chose_trie_word(self):
        word = ''
        current = self.trie
        while True:
            if '$' in current: break
            if not current: break
            key = next(iter(current))
            word += key 
            current = current[key]

        return word

    def get_words(self, prefix):
        
        def dfs(current, word, index):
            if len(words[index]) > 50:
                return
            if '$' in current:
                words[index].append(word)
            for char in current:
                if char == '$': continue
                dfs(current[char], word + char, index)
        
        def build_words(current):
            for char in prefix:
                if char not in current:
                    break
                current = current[char]
            else:
                index = 0
                for x in current:
                    words.append([])
                    dfs(current[x], prefix + x, index)
                    index += 1
        
        words = []
        build_words(self.trie)
        length = len(set([x for y in words for x in y]))
        if length < 10:
            build_words(self.parent.global_trie)

        words = list(set([x for y in words for x in y]))
        if len(words) <= 10: return words
        return random.sample(words, 10)

