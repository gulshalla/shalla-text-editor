import sys
from PyQt5 import QtWidgets, QtPrintSupport, QtGui, QtCore
from PyQt5.QtCore import Qt 

class DocumentStatistics(QtWidgets.QDialog):

    def __init__(self, parent = None):
        QtWidgets.QDialog.__init__(self, parent)
        self.parent = parent 
        self.setup_ui()

    #UI generated using PyQt5 designer
    def setup_ui(self):
        self.setObjectName("Statistics")
        self.resize(231, 134)
        self.layoutWidget = QtWidgets.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 21, 241, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_7)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Statistics"))
        self.label.setText(_translate("Dialog", "  Number Count:"))
        self.label_3.setText(_translate("Dialog", "text"))
        self.label_2.setText(_translate("Dialog", "     Letter Count:"))
        self.label_5.setText(_translate("Dialog", "text"))
        self.label_6.setText(_translate("Dialog", "       Word Count:"))
        self.label_4.setText(_translate("Dialog", "text"))
        self.label_8.setText(_translate("Dialog", "Character Count:"))
        self.label_7.setText(_translate("Dialog", "text"))

    def process(self):
        words = self.parent.text.toPlainText()
        words = words.split()

        alpha = nums = chars = 0
        for word in words:
            for char in word:
                if char.isalpha(): alpha += 1 
                else: nums += 1
                chars += 1

        self.label_5.setText(str(alpha))
        self.label_3.setText(str(nums))
        self.label_4.setText(str(len(words)))
        self.label_7.setText(str(chars))
        self.label.setStyleSheet("font-weight:bold; font-size: 15px;")
        self.label_2.setStyleSheet("font-weight:bold; font-size: 15px;")
        self.label_6.setStyleSheet("font-weight:bold; font-size: 15px;")
        self.label_8.setStyleSheet("font-weight:bold; font-size: 15px;")




