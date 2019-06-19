import sys
from PyQt5 import QtWidgets, QtPrintSupport, QtGui, QtCore
from PyQt5.QtCore import Qt 


class MyTextEdit(QtWidgets.QTextEdit):

    def __init__(self, parent = None):
        #*args to set parent
        QtWidgets.QLineEdit.__init__(self, parent)
        font=QtGui.QFont()
        font.setPointSize(12)
        self.setFont(font)
        self.parent = parent
        self.completer = None
        self.prev_word = []

    def setCompleter(self, completer):
        if self.completer:
            self.completer.insertText.disconnect()
        if not completer:
            return

        completer.setWidget(self)
        completer.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.completer = completer
        self.completer.insertText.connect(self.insertCompletion)

    def insertCompletion(self, completion):
        tc = self.textCursor()
        extra = (len(completion) -
            len(self.completer.completionPrefix()))
        tc.movePosition(QtGui.QTextCursor.Left)
        tc.movePosition(QtGui.QTextCursor.EndOfWord)
        tc.insertText(completion[-extra:])
        self.setTextCursor(tc)

    def textUnderCursor(self):
        tc = self.textCursor()
        tc.select(QtGui.QTextCursor.WordUnderCursor)
        return tc.selectedText()

    def focusInEvent(self, event):
        if self.completer:
            self.completer.setWidget(self);
        QtWidgets.QTextEdit.focusInEvent(self, event)

    def keyPressEvent(self, event):
        # add previous word to trie if space is pressed
        if event.text().isalpha(): self.prev_word.append(event.text())
        if event.key() == QtCore.Qt.Key_Backspace: self.prev_word.pop()
        if event.text() == ' ': 
            self.parent.local_trie.insert(''.join(self.prev_word))
            self.prev_word = []

        if self.completer and self.completer.popup() and self.completer.popup().isVisible():
            if event.key() in (
            QtCore.Qt.Key_Enter,
            QtCore.Qt.Key_Return,
            QtCore.Qt.Key_Escape,
            QtCore.Qt.Key_Tab,
            QtCore.Qt.Key_Backtab,
            QtCore.Qt.Key_Space):
                event.ignore()
                return
        ## has ctrl-Space been pressed??
        isShortcut = (event.modifiers() == QtCore.Qt.ControlModifier and event.key() == QtCore.Qt.Key_Space)
        ## modifier to complete suggestion inline ctrl-e
        inline = (event.modifiers() == QtCore.Qt.ControlModifier and event.key() == QtCore.Qt.Key_E)
        ## if inline completion has been chosen
        if inline or isShortcut:
            #self.completer = None
            words = self.parent.local_trie.get_words(self.textUnderCursor())
            completer_new = MyDictionaryCompleter(words)
            self.setCompleter(completer_new)


        if inline:
            # set completion mode as inline
            self.completer.setCompletionMode(QtWidgets.QCompleter.InlineCompletion)
            completionPrefix = self.textUnderCursor()
            if (completionPrefix != self.completer.completionPrefix()):
                self.completer.setCompletionPrefix(completionPrefix)
            self.completer.complete()

            # set the current suggestion in the text box
            self.completer.insertText.emit(self.completer.currentCompletion())
            # reset the completion mode
            self.completer.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
            return
        if (not self.completer or not isShortcut):
            pass
            QtWidgets.QTextEdit.keyPressEvent(self, event)

        ctrlOrShift = event.modifiers() in (QtCore.Qt.ControlModifier ,QtCore.Qt.ShiftModifier)
        if ctrlOrShift and event.text()== '':
            return
        eow = "~!@#$%^&*+{}|:\"<>?,./;'[]\\-=" #end of word

        hasModifier = ((event.modifiers() != QtCore.Qt.NoModifier) and not ctrlOrShift)

        completionPrefix = self.textUnderCursor()

        if not isShortcut :
            if self.completer.popup():
                self.completer.popup().hide()
            return

        self.completer.setCompletionPrefix(completionPrefix)
        popup = self.completer.popup()
        popup.setCurrentIndex(
            self.completer.completionModel().index(0,0))
        cr = self.cursorRect()
        cr.setWidth(self.completer.popup().sizeHintForColumn(0)
            + self.completer.popup().verticalScrollBar().sizeHint().width())
        self.completer.complete(cr) ## popup it up!


class MyDictionaryCompleter(QtWidgets.QCompleter):
    insertText = QtCore.pyqtSignal(str)

    def __init__(self, myKeywords=None):       
        QtWidgets.QCompleter.__init__(self, myKeywords)
        self.activated.connect(self.changeCompletion)
    
    def changeCompletion(self, completion):
        print(completion)
        if completion.find("(") != -1:
            completion = completion[:completion.find("(")]
        print(completion)
        self.insertText.emit(completion)
