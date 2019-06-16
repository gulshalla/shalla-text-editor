import sys
from PyQt5 import QtWidgets, QtPrintSupport, QtGui, QtCore
from PyQt5.QtCore import Qt 

class Table(QtWidgets.QDialog):

    def __init__(self, parent = None):
        QtWidgets.QDialog.__init__(self, parent)
        
        #Parent is needed as we are performing operations on the parents TextField
        self.parent = parent 
        
        self.setup_ui()

    def setup_ui(self):
        self.setObjectName("Insert Table")
        self.resize(340, 177)
        

        #UI features. Generated using PyQT5 Designer
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.columns = QtWidgets.QSpinBox(self)
        self.columns.setObjectName("columns")
        self.gridLayout.addWidget(self.columns, 1, 2, 1, 1)
        self.spacing = QtWidgets.QSpinBox(self)
        self.spacing.setObjectName("spacing")
        self.gridLayout.addWidget(self.spacing, 3, 2, 1, 1)
        self.rows = QtWidgets.QSpinBox(self)
        self.rows.setObjectName("rows")
        self.gridLayout.addWidget(self.rows, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.padding = QtWidgets.QSpinBox(self)
        self.padding.setObjectName("padding")
        self.gridLayout.addWidget(self.padding, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.insert)
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 3)
        self.padding.setValue(10)
        self.rows.setValue(5)
        self.columns.setValue(5)

        
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, InsertTable):
        _translate = QtCore.QCoreApplication.translate
        InsertTable.setWindowTitle(_translate("InsertTable", "Insert Table"))
        self.label_3.setText(_translate("InsertTable", "  Number of Columns:"))
        self.label_4.setText(_translate("InsertTable", "                Cell Spacing:"))
        self.label_2.setText(_translate("InsertTable", "                 Cell Padding:"))
        self.label.setText(_translate("InsertTable", "        Number of Rows:"))
        self.pushButton.setText(_translate("InsertTable", "Insert Table"))


    def insert(self):
        cursor = self.parent.text.textCursor()
        rows = self.rows.value()
        cols = self.columns.value()
        padding = self.padding.value()
        spacing = self.spacing.value()

        #Check for invalid row, col inputs
        if not rows or not cols:
            error = 'Row and Column cannot be zero'
            popup = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, 
                error, error, QtWidgets.QMessageBox.Ok, self)
            popup.show()
        else:
            table_format = QtGui.QTextTableFormat()
            table_format.setCellPadding(padding)
            table_format.setCellSpacing(spacing)
            cursor.insertTable(rows, cols, table_format)

            self.close()


#add, remove rows and cols from a created table
def insert_row(parent):
    cursor = parent.text.textCursor()
    table = cursor.currentTable()
    cell = table.cellAt(cursor)
    table.insertRows(cell.row(), 1)
    
def insert_col(parent):
    cursor = parent.text.textCursor()
    table = cursor.currentTable()
    cell = table.cellAt(cursor)
    table.insertColumns(cell.column(), 1)

def remove_row(parent):
    cursor = parent.text.textCursor()
    table = cursor.currentTable()
    cell = table.cellAt(cursor)
    table.removeRows(cell.row(), 1)

def remove_col(parent):
    cursor = parent.text.textCursor()
    table = cursor.currentTable()
    cell = table.cellAt(cursor)
    table.removeColumns(cell.column(), 1)


