import sys
from PyQt5 import QtWidgets, QtPrintSupport, QtGui, QtCore
from PyQt5.QtCore import Qt 

class Thesaurus(QtWidgets.QDialog):

    def __init__(self, parent):
        QtWidgets.QDialog.__init__(self, parent)
        self.parent = parent
     
        self.setup_ui()

    #UI generated using PyQt5 designer
    def setup_ui(self):
        self.setObjectName("Thesaurus")
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
        Dialog.setWindowTitle(_translate("Dialog", "Thesaurus"))
        self.label.setText(_translate("Dialog", "text"))

    def get_synonyms(self):
        cursor = self.parent.text.textCursor()
        if cursor.hasSelection():
            tc = self.parent.text.textCursor()
            tc.select(QtGui.QTextCursor.WordUnderCursor) 
            word = tc.selectedText().lower()
            if (word in self.parent.dictionary and self.parent.dictionary[word] != 1 and 
                    len(self.parent.dictionary[word]) == 2):
                self.label.setText(word.capitalize())
                syns = self.parent.dictionary[word][1]
                for word in syns:
                    self.textEdit.append(word)
                self.textEdit.setReadOnly(True)
                self.show()
            else:
                window = 'Key Error'
                error = 'Word not in Thesaurus!'
                popup = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical,
                    window, error, QtWidgets.QMessageBox.Ok, self.parent)
                popup.show()
        else:
            window = 'Empty string'
            error = 'Make a selection first!'
            popup = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical,
                window, error, QtWidgets.QMessageBox.Ok, self.parent)
            popup.show()            

