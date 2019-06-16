import sys
from PyQt5 import QtWidgets, QtPrintSupport, QtGui, QtCore
from PyQt5.QtCore import Qt 

from extensions import *

#Main document setup functions 

def setup_document(parent):
    doc = parent.text.document()

    # Set initial margin
    frame = doc.rootFrame()
    frame_format = frame.frameFormat()

    frame_format.setMargin(parent.document_margin)
    frame.setFrameFormat(frame_format)

def custom_menu(parent, position):
        '''
        a custon context menu in case of table, hyperlink or string operations
        '''
        cursor = parent.text.textCursor()
        table = cursor.currentTable()
        
        #position variable is needed to make sure menu is spawned at click position
        pos = parent.text.mapToGlobal(position)
        
        if table:
            #create a new menu and add actions to it
            menu = QtWidgets.QMenu(parent)
            append_row_action = QtWidgets.QAction('Append row', parent)
            append_row_action.triggered.connect(lambda: table.appendRows(1))

            append_col_action = QtWidgets.QAction('Append column', parent)
            append_col_action.triggered.connect(lambda: table.appendColumns(1))
            
            insert_row_action = QtWidgets.QAction('Insert row', parent)
            insert_row_action.triggered.connect(lambda: insert_table.insert_row(parent))
            
            insert_col_action = QtWidgets.QAction('Insert column', parent)
            insert_col_action.triggered.connect(lambda: insert_table.insert_col(parent))
            
            remove_row_action = QtWidgets.QAction('Remove row', parent)
            remove_row_action.triggered.connect(lambda: insert_table.remove_row(parent))
            
            remove_col_action = QtWidgets.QAction('Remove column', parent)
            remove_col_action.triggered.connect(lambda: insert_table.remove_col(parent))

            menu.addAction(append_row_action)
            menu.addAction(append_col_action)
            menu.addSeparator()
            menu.addAction(insert_row_action)
            menu.addAction(insert_col_action)
            menu.addSeparator()
            menu.addAction(remove_row_action)
            menu.addAction(remove_col_action)

            position = parent.mapToGlobal(position)
            
            #create an offset to account for Toolbar
            position.setY(pos.y() + 4)
            
            menu.move(position)
            menu.show()
        else:
            event = QtGui.QContextMenuEvent(QtGui.QContextMenuEvent.Mouse,QtCore.QPoint())
            parent.text.contextMenuEvent(event)


def center(parent):
        '''
        make the window appear in the center of the screen
        '''
        frameGm = parent.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(
            QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        parent.move(frameGm.topLeft())

def change_made(parent):
    parent.saved = False
