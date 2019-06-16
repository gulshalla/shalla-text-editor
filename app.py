import sys
from PyQt5 import QtWidgets, QtPrintSupport, QtGui, QtCore
from PyQt5.QtCore import Qt 

from extensions import *
from layouts import *

#Lowercase functions are my own. Upper case functions are from the PyQt Module

class Main(QtWidgets.QMainWindow):

    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self, parent)
        
        self.document_name = ''
        self.saved = True
        self.document_margin = 50
        self.page_length = 800
        
        self.setup_ui()

    def setup_ui(self):
        self.setGeometry(1000, 100, 900, 1000)
        document.center(self)
        self.setWindowTitle('Shalla Editor')
        self.setWindowIcon(QtGui.QIcon("icons/shalla.png"))

        self.text = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text)


        #initiazile toolbar, statusbar
        tool_bar.ToolBar(self)
        format_bar.FormatBar(self)
        status_bar.StatusBar(self)
        document.setup_document(self)
        menu_bar.MenuBar(self)

        #request custom context menu
        self.text.setContextMenuPolicy(Qt.CustomContextMenu)
        self.text.customContextMenuRequested.connect(lambda position: document.custom_menu(self, position))
        self.text.textChanged.connect(lambda: document.change_made(self))


    def new(self):
        '''
        create a new instance of the editor
        '''
        new_window = Main(self)
        new_window.show()

    #close app only when changes have been saved
    def closeEvent(self, event):
        if self.saved:
            event.accept()
        else:
            popup = QtWidgets.QMessageBox(self)
            popup.setIcon(QtWidgets.QMessageBox.Warning)
            popup.setText("The document has been modified")
            popup.setInformativeText("Do you want to save your changes?")
            popup.setStandardButtons(QtWidgets.QMessageBox.Save   |
                                      QtWidgets.QMessageBox.Cancel |
                                      QtWidgets.QMessageBox.Discard)
            popup.setDefaultButton(QtWidgets.QMessageBox.Save)
            choice = popup.exec_()

            if choice == QtWidgets.QMessageBox.Save: self.save()
            elif choice == QtWidgets.QMessageBox.Discard: event.accept()
            else: event.ignore()

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()



