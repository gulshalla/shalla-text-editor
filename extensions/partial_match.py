import sys
from PyQt5 import QtWidgets, QtPrintSupport, QtGui, QtCore
from PyQt5.QtCore import Qt 

class RHash():
    
    def __init__(self, s):
        self.val = 0
        self.prime = 101
        self.base = 256
        self.shift = pow(self.base, len(s) - 1, self.prime)
        for c in s: 
            self.append(c)
    
    def append(self, c):
        self.val = (self.val * self.base + ord(c)) % self.prime

    def rmleft(self, c):
        self.val = (self.val - self.shift * ord(c) + self.prime) % self.prime 

    def __eq__(self, other):            
        return self.val == other.val


class PartialMatch(QtWidgets.QDialog):

    def __init__(self, parent):
        QtWidgets.QDialog.__init__(self, parent)
        self.parent = parent 
        self.setup_ui()

    #UI generated using PyQt5 designer
    def setup_ui(self):
        self.setObjectName("Partial matches")
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
        Dialog.setWindowTitle(_translate("Dialog", "Words with partial matches"))
        self.label.setText(_translate("Dialog", "text"))

    def strstr_custom(self, needle, haystack):
        hl, nl = len(haystack), len(needle)
        if not haystack or nl > hl: return -1

        nh, hh = RHash(needle), RHash(haystack[:nl])
        if nh == hh and haystack[:nl] == needle:
            return 0

        for i in range(nl,hl ):
            hh.rmleft(haystack[i-nl])
            hh.append(haystack[i])
            if hh == nh and haystack[i-nl+1:i+1] == needle:
                return i - nl + 1
        
        return -1

    def get_matches(self):
        cursor = self.parent.text.textCursor()
        if cursor.hasSelection():
            tc = self.parent.text.textCursor()
            tc.select(QtGui.QTextCursor.WordUnderCursor) 
            self.word = tc.selectedText()
        else:
            window = 'Empty string'
            error = 'Make a selection first!'
            popup = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical,
                window, error, QtWidgets.QMessageBox.Ok, self.parent)
            popup.show()
            return

        matches = []
        text = self.parent.text.toPlainText()
        for word in text.split():
            if self.strstr_custom(self.word, word) >= 0:
                matches.append(word)

        if len(matches) == 0:
            window = 'Key Error'
            error = 'No partial matches! Try a different word.'
            popup = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical,
                window, error, QtWidgets.QMessageBox.Ok, self.parent)
            popup.show()
            return

        self.label.setText("Partial matches of '" + self.word + "' in:")
        for match in matches:
            self.textEdit.append(match)
        self.textEdit.setReadOnly(True)
        self.show()


