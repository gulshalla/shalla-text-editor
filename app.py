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
        self.setup_ui()

        self.saved = True

    def setup_ui(self):
        self.setGeometry(1000, 100, 900, 1000)
        self.center()
        self.setWindowTitle('Shalla Editor')

        self.text = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text)


        #initiazile toolbar, statusbar
        self.status_bar = self.statusBar()
        tool_bar.ToolBar(self)
        format_bar.FormatBar(self)

        #request custom context menu
        self.text.setContextMenuPolicy(Qt.CustomContextMenu)
        self.text.customContextMenuRequested.connect(self.custom_menu)
    
    def center(self):
        '''
        make the window appear in the center of the screen
        '''
        frameGm = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(
            QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def new(self):
        '''
        create a new instance of the editor
        '''
        new_window = Main(self)
        new_window.show()

    def custom_menu(self, position):
        '''
        a custon context menu in case of table, hyperlink or string operations
        '''
        cursor = self.text.textCursor()
        table = cursor.currentTable()
        
        #position variable is needed to make sure menu is spawned at click position
        pos = self.text.mapToGlobal(position)
        
        if table:
            #create a new menu and add actions to it
            menu = QtWidgets.QMenu(self)
            append_row_action = QtWidgets.QAction('Append row', self)
            append_row_action.triggered.connect(lambda: table.appendRows(1))

            append_col_action = QtWidgets.QAction('Append column', self)
            append_col_action.triggered.connect(lambda: table.appendColumns(1))
            
            insert_row_action = QtWidgets.QAction('Insert row', self)
            insert_row_action.triggered.connect(lambda: insert_table.insert_row(self))
            
            insert_col_action = QtWidgets.QAction('Insert column', self)
            insert_col_action.triggered.connect(lambda: insert_table.insert_col(self))
            
            remove_row_action = QtWidgets.QAction('Remove row', self)
            remove_row_action.triggered.connect(lambda: insert_table.remove_row(self))
            
            remove_col_action = QtWidgets.QAction('Remove column', self)
            remove_col_action.triggered.connect(lambda: insert_table.remove_col(self))

            menu.addAction(append_row_action)
            menu.addAction(append_col_action)
            menu.addSeparator()
            menu.addAction(insert_row_action)
            menu.addAction(insert_col_action)
            menu.addSeparator()
            menu.addAction(remove_row_action)
            menu.addAction(remove_col_action)

            position = self.mapToGlobal(position)
            
            #create an offset to account for Toolbar
            position.setY(pos.y() + 4)
            
            menu.move(position)
            menu.show()
        else:
            event = QtGui.QContextMenuEvent(QtGui.QContextMenuEvent.Mouse,QtCore.QPoint())
            self.text.contextMenuEvent(event)

        

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()



