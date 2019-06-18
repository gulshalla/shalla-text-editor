import sys
from PyQt5 import QtWidgets, QtPrintSupport, QtGui, QtCore
from PyQt5.QtCore import Qt 

import json

def wrong_spelling(parent):
    text = parent.text.toPlainText()
    start = end = 0
    word = ''
    font = parent.text.font()
    while end < len(text):
        while end < len(text) and text[end] != ' ' and text[end].isalpha():
            word += text[end]
            end += 1
        while end < len(text) and text[end].isalpha() is False:
            end += 1
        if word.lower() not in parent.dictionary:
            moveCursor(parent, start, end)
            parent.text.setFontUnderline(True)
            parent.text.setTextColor(QtGui.QColor('red'))
        word = ''
        start = end
    
    moveCursor(parent, start , end + 1)
    parent.text.setFontUnderline(False)
    parent.text.setTextColor(QtGui.QColor('000000'))


def moveCursor(parent, start, end):
    cursor = parent.text.textCursor()
    cursor.setPosition(start)

    cursor.movePosition(QtGui.QTextCursor.Right,QtGui.QTextCursor.KeepAnchor, end - start)
    parent.text.setTextCursor(cursor)
