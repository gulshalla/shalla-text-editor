import random
import collections
# '$' is end character

class LocalTrie:

    def __init__(self, parent):
        self.trie = {}
        self.size = 0
        self.parent = parent
        self.que = collections.deque()

    def insert(self, word):
        
        def insert_word(word):
            current = self.trie 
            for char in word:
                if char not in current:
                    current[char] = {}
                current = current[char]
            current['$'] = '$'
        
        if len(word) > 50: return
        if self.size < 10000:
            insert_word(word)
            self.que.append(word)
            self.size += 1
        else:
            word = que.popleft()
            word = self.chose_trie_word()
            self.delete_word_in_trie(self, word)
            insert_word(word) 
            que.append(word)
        

    def delete_word_in_trie(self, word):
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
        #use this function if you want to use a random word to remove from trie
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
        
        def dfs(current, word, index, words):
            if len(words[index]) > 10:
                return
            if '$' in current:
                words[index].append(word)
            for char in current:
                if char == '$': continue
                dfs(current[char], word + char, index, words)
        
        def build_words(current, words):
            for char in prefix:
                if char not in current:
                    break
                current = current[char]
            else:
                index = 0
                for x in current:
                    if x == '$': continue
                    words.append([])
                    dfs(current[x], prefix + x, index, words)
                    index += 1

        words = []
        words_next = []
        build_words(self.trie, words)
        length = len(set([x for y in words for x in y]))
        if length < 10:
            build_words(self.parent.global_trie, words_next)

        words = list(set([x for y in words for x in y]))
        if len(words) >= 10: return words
        words_next = list(set([x for y in words_next for x in y]))

        sample = random.sample(words_next, min(10 - len(words), len(words_next)))
        return words + sample

    def search_global_trie(self, word):
        current = self.parant.global_trie 
        for char in word:
            if char not in current:
                return False
            current = current[char]
        return '$' in current
