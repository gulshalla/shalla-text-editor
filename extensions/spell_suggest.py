import sys
from PyQt5 import QtWidgets, QtPrintSupport, QtGui, QtCore
from PyQt5.QtCore import Qt 

class SpellSuggest(QtWidgets.QDialog):

    def __init__(self, parent):
        QtWidgets.QDialog.__init__(self, parent)
        self.parent = parent 
        
        self.setup_ui()

    #UI generated using PyQt5 designer
    def setup_ui(self):
        self.setObjectName("Spelling Suggestions")
        self.resize(435, 213)
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(10, 20, 411, 171))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("font: 75 22pt \"DejaVu Sans\";")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 1)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Spelling Suggestions"))
        self.label.setText(_translate("Dialog", "text"))
    
    def levenshtein(self, word1, word2):
        '''
        returns the levenshtein distance between two words
        '''
        len1, len2 = len(word1) + 1, len(word2) + 1
        dp = [[0] * len2 for _ in range(len1)]

        for i in range(len1):
            for j in range(len2):
                if i == 0: 
                    dp[i][j] = j 
                elif j == 0: 
                    dp[i][j] = i 
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

        return dp[-1][-1]

    def get_word(self):
        '''
        get the word under the cursor
        '''
        cursor = self.parent.text.textCursor()
        if cursor.hasSelection():
            tc = self.parent.text.textCursor()
            tc.select(QtGui.QTextCursor.WordUnderCursor) 
            self.word = tc.selectedText().lower()
            return 1
        else:
            window = 'Empty string'
            error = 'Make a selection first!'
            popup = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical,
                window, error, QtWidgets.QMessageBox.Ok, self.parent)
            popup.show()

        return 0

    #get suggestions for each prefix
    def find_suggestions(self, root, prefix):
        for char in prefix:
            if char not in root:
                return []
            root = root[char]

        def global_trie_dfs(current, prefix):
            if len(words) > 50: return
            if '$' in current:
                words.append(prefix)
            for node in current:
                if node == '$': continue
                global_trie_dfs(current[node], prefix + node)

        words = []
        global_trie_dfs(root, prefix)
        return words

    #show final suggestions
    def get_suggestions(self):
        if not self.get_word(): return        
        
        if self.word in self.parent.dictionary:
            window = 'Key Error'
            error = 'Spelling is correct!'
            popup = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical,
                window, error, QtWidgets.QMessageBox.Ok, self.parent)
            popup.show()
            return

        if len(self.word) > 20:
            window = 'Key Error'
            error = 'Word is too long!'
            popup = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical,
                window, error, QtWidgets.QMessageBox.Ok, self.parent)
            popup.show()
            return

        #dfs the global trie from every prefix in the word
        result = []
        for i in range(1, len(self.word)):
            words = self.find_suggestions(self.parent.global_trie, self.word[:i])
            result.extend(words)

        #if result is empty return error
        if len(result) == 0:
            window = 'Key Error'
            error = 'No suggestions! Try a different word.'
            popup = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical,
                window, error, QtWidgets.QMessageBox.Ok, self.parent)
            popup.show()
            return

        #calculate the levenshtein distances of all words in result
        distances = []
        for word in result:
            leven = self.levenshtein(word, self.word)
            distances.append((leven, word))

        distances.sort()
        self.label.setText(self.word.capitalize())
        
        #show top 5 suggestions
        for i in range(5):
            self.textEdit.append(distances[i][1])
        self.textEdit.setReadOnly(True)
        self.show()





