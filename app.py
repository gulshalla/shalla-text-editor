import sys
from PyQt5 import QtWidgets, QtPrintSupport, QtGui, QtCore
from PyQt5.QtCore import Qt 

#Lowercase functions are my own. Upper case functions are from the PyQt Module

class Main(QtWidgets.QMainWindow):

    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setup_ui()

    def setup_ui(self):
        self.setGeometry(100, 100, 1000, 1200)
        self.setWindowTitle('Shalla Editor')


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

