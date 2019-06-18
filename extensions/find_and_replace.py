import sys
from PyQt5 import QtWidgets, QtPrintSupport, QtGui, QtCore
from PyQt5.QtCore import Qt 
import itertools

class FindReplace(QtWidgets.QDialog):

    def __init__(self, parent = None):
        QtWidgets.QDialog.__init__(self, parent)
        self.parent = parent
        self.start = -1

        self.setup_ui()

    def setup_ui(self):
        self.setObjectName("FindandReplace")
        self.resize(394, 150)
        self.layoutWidget = QtWidgets.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 371, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.replace_field = QtWidgets.QTextEdit(self.layoutWidget)
        self.replace_field.setObjectName("replace_field")
        self.horizontalLayout_2.addWidget(self.replace_field)
        self.replace_button = QtWidgets.QPushButton(self.layoutWidget)
        self.replace_button.setObjectName("replace_button")
        self.horizontalLayout_2.addWidget(self.replace_button)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.replace_all_button = QtWidgets.QPushButton(self.layoutWidget)
        self.replace_all_button.setObjectName("replace_all_button")
        self.gridLayout.addWidget(self.replace_all_button, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.find_field = QtWidgets.QTextEdit(self.layoutWidget)
        self.find_field.setObjectName("find_field")
        self.horizontalLayout.addWidget(self.find_field)
        self.find_button = QtWidgets.QPushButton(self.layoutWidget)
        self.find_button.setObjectName("find_button")
        self.horizontalLayout.addWidget(self.find_button)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.find_button.clicked.connect(self.find)
        self.replace_button.clicked.connect(self.replace)
        self.replace_all_button.clicked.connect(self.replace_all)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, FindandReplace):
        _translate = QtCore.QCoreApplication.translate
        FindandReplace.setWindowTitle(_translate("FindandReplace", "Find and replace"))
        self.replace_button.setText(_translate("FindandReplace", "Replace"))
        self.replace_all_button.setText(_translate("FindandReplace", "Replace All"))
        self.find_button.setText(_translate("FindandReplace", "Find"))


    def find(self):
        text = self.parent.text.toPlainText()
        search_item = self.find_field.toPlainText()
        
        self.start = text.find(search_item, self.start + 1)

        if self.start >= 0:
            end = self.start + len(search_item)
            self.moveCursor(self.start, end)
        else:
            self.start = -1
            self.parent.text.moveCursor(QtGui.QTextCursor.End)

    def replace(self):
        cursor = self.parent.text.textCursor()

        if cursor.hasSelection():
            cursor.insertText(self.replace_field.toPlainText())
            self.parent.text.setTextCursor(cursor)

    def replace_all(self):
        self.start = 0
        self.find()
        while self.start > -1:
            self.replace()
            self.find()

    def moveCursor(self,start,end):
        cursor = self.parent.text.textCursor()
        cursor.setPosition(start)
        cursor.movePosition(QtGui.QTextCursor.Right,QtGui.QTextCursor.KeepAnchor,end - start)
        self.parent.text.setTextCursor(cursor)
