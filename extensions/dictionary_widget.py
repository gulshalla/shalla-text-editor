import sys
from PyQt5 import QtWidgets, QtPrintSupport, QtGui, QtCore
from PyQt5.QtCore import Qt 

class DictionaryWidget(QtWidgets.QDialog):

    def __init__(self, parent, word):
        QtWidgets.QDialog.__init__(self, parent)
        self.parent = parent
        self.word = word 
        self.setup_ui()

    #UI generated using PyQt5 designer
    def setup_ui(self):
        self.setObjectName("English Dictionary")
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
        Dialog.setWindowTitle(_translate("Dialog", "English Dictionary"))
        self.label.setText(_translate("Dialog", "text"))


    def get_meaning(self):
        self.label.setText(self.word.capitalize())
        self.label.setFont(QtGui.QFont("Times",weight=QtGui.QFont.Bold))
        self.textEdit.textCursor().insertHtml(self.parent.dictionary[self.word][0])
        self.textEdit.setReadOnly(True)

    
        