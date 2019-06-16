import sys
from PyQt5 import QtWidgets, QtPrintSupport, QtGui, QtCore
from PyQt5.QtCore import Qt 


class MenuBar(QtWidgets.QMainWindow):

    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.parent = parent
        self.setup_menubar()

    def setup_menubar(self):
        menu_bar = self.parent.menuBar()
        file = menu_bar.addMenu('File')
        edit = menu_bar.addMenu('Edit')
        view = menu_bar.addMenu('View')

        # Toggling actions for the various bars
        toolbar_view = QtWidgets.QAction("Toggle Toolbar",self)
        toolbar_view.triggered.connect(self.toggle_toolbar)

        formatbar_view = QtWidgets.QAction("Toggle Formatbar",self)
        formatbar_view.triggered.connect(self.toggle_formatbar)

        statusbar_view = QtWidgets.QAction("Toggle Statusbar",self)
        statusbar_view.triggered.connect(self.toggle_statusbar)

        file.addAction(self.parent.new_action)
        file.addAction(self.parent.open_action)
        file.addAction(self.parent.save_action)
        file.addAction(self.parent.print_action)
        file.addAction(self.parent.preview_action)

        edit.addAction(self.parent.undo_action)
        edit.addAction(self.parent.redo_action)
        edit.addAction(self.parent.cut_action)
        edit.addAction(self.parent.copy_action)
        edit.addAction(self.parent.paste_action)

        view.addAction(toolbar_view)
        view.addAction(formatbar_view)
        view.addAction(statusbar_view)

    def toggle_toolbar(self):

        state = self.parent.tool_bar.isVisible()

        # Set the visibility to its inverse
        self.parent.tool_bar.setVisible(not state)

    def toggle_formatbar(self):

        state = self.parent.format_bar.isVisible()

        # Set the visibility to its inverse
        self.parent.format_bar.setVisible(not state)

    def toggle_statusbar(self):

        state = self.parent.status_bar.isVisible()

        # Set the visibility to its inverse
        self.parent.status_bar.setVisible(not state)