import sys
from PyQt5 import QtWidgets, QtPrintSupport, QtGui, QtCore
from PyQt5.QtCore import Qt 

class StatusBar(QtWidgets.QMainWindow):

    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.parent = parent
        self.setup_statusbar()
        self.parent.text.cursorPositionChanged.connect(self.status_bar_labels)

    def setup_statusbar(self):
        self.parent.status_bar = self.parent.statusBar()
        self.status_bar = self.parent.status_bar
        self.status_bar.setStyleSheet("background-color: #FFFFFF;")

        # Initialize value for cursor position
        self.status_bar_labels()

    def status_bar_labels(self):
        cursor = self.parent.text.textCursor()
        row = cursor.blockNumber() + 1
        col = cursor.columnNumber() + 1

        self.status_bar.showMessage("Line: {} | Column: {}".format(row, col))
