import sys
from PyQt5 import QtWidgets, QtPrintSupport, QtGui, QtCore
from PyQt5.QtCore import Qt 
import itertools

from extensions import *

class ToolBar(QtWidgets.QMainWindow):

    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self, parent)
        
        #inherit from the Main class
        self.parent = parent
        
        #Initialize the toolbar
        self.setup_toolbar()

    def make_action(self, arg):
            '''
            function to make a new action for the toolbar
            @arg: a list containing [name, icon path, slot_function, shortcut, tip]
            @return: the newly made action
            '''
            action = QtWidgets.QAction(QtGui.QIcon(arg[1]), arg[0], self.parent)
            action.setShortcut(arg[3])
            action.setStatusTip(arg[4])
            action.triggered.connect(arg[2])

            return action

    def setup_toolbar(self):
        # list of action arguments
        actions = [('New', 'icons/new.png', self.parent.new, 'Ctrl+N', 'New document'),
        ('Open', 'icons/open.png', self.open, 'Ctrl+N', 'Open existing file'),
        ('Save', 'icons/save.png', self.save, 'Ctrl+S', 'Save'),
        ('Print', 'icons/print.png', self.print_page, 'Ctrl+P', 'Print'),
        ('Page View', 'icons/page.png', self.preview, 'Ctrl+Shift+P', 'Page View'),
        ('Cut', 'icons/cut.png', self.parent.text.cut, 'Ctrl+X', 'Cut'),
        ('Copy', 'icons/copy.png', self.parent.text.copy, 'Ctrl+C', 'Copy'),
        ('Paste', 'icons/paste.png', self.parent.text.paste, 'Ctrl+V', 'Paste'),
        ('Undo', 'icons/undo.png', self.parent.text.undo, 'Ctrl+Z', 'Undo'),
        ('Redo', 'icons/redo.png', self.parent.text.redo, 'Ctrl+Shift+Z', 'Redo'),
        ('Bullet List', 'icons/bullet.png', self.bullet, 'Ctrl+Shift+B', 'Bullet List'),
        ('Numbered List', 'icons/number.png', self.numbered, 'Ctrl+Shift+N', 'Numbered List'),
        ('Insert table', 'icons/table.png', self.table, 'Ctrl+T', 'Insert table'),
        ('Document statistics', 'icons/words.png', self.document_stats, 'Ctrl + L', 
            'Document statistics')] 

        # create new actions
        counter = itertools.count()
        self.new_action = self.make_action(actions[next(counter)])
        self.open_action = self.make_action(actions[next(counter)])
        self.save_action = self.make_action(actions[next(counter)])
        self.print_action = self.make_action(actions[next(counter)])
        self.preview_action = self.make_action(actions[next(counter)])
        self.cut_action = self.make_action(actions[next(counter)])
        self.copy_action = self.make_action(actions[next(counter)])
        self.paste_action = self.make_action(actions[next(counter)])
        self.undo_action = self.make_action(actions[next(counter)])
        self.redo_action = self.make_action(actions[next(counter)])
        self.bullet_action = self.make_action(actions[next(counter)])
        self.numbered_action = self.make_action(actions[next(counter)])
        self.table_action = self.make_action(actions[next(counter)])
        self.document_statistics_action = self.make_action(actions[next(counter)])


        # add them to the toolbar
        self.toolbar = self.parent.addToolBar("ToolBar")
        self.toolbar.addAction(self.new_action)
        self.toolbar.addAction(self.open_action)
        self.toolbar.addAction(self.save_action)
        self.toolbar.addSeparator()

        self.toolbar.addAction(self.print_action)
        self.toolbar.addAction(self.preview_action)
        self.toolbar.addSeparator()

        self.toolbar.addAction(self.cut_action)
        self.toolbar.addAction(self.copy_action)
        self.toolbar.addAction(self.paste_action)
        self.toolbar.addAction(self.undo_action)
        self.toolbar.addAction(self.redo_action)
        self.toolbar.addSeparator()

        self.toolbar.addAction(self.bullet_action)
        self.toolbar.addAction(self.numbered_action)
        self.toolbar.addAction(self.table_action)
        self.toolbar.addSeparator()

        self.toolbar.addAction(self.document_statistics_action)
        self.parent.addToolBarBreak()


    def open(self):
        '''
        open a new file of type '.shalla' only
        '''
        self.parent.document_name = QtWidgets.QFileDialog.getOpenFileName(
            self.parent, 'Open File', '.', '(*.shalla)')[0]
        if self.parent.document_name:
            with open(self.parent.document_name, 'rt') as doc:
                self.parent.text.setText(doc.read())

    def save(self):
        '''
        save the current document to local disk
        '''
        
        #Make sure we have a filename
        if self.parent.document_name == '':
            self.parent.document_name = QtWidgets.QFileDialog.getSaveFileName(
                self.parent, 'Save File')[0]

        #Make sure .shalla is appended
        if self.parent.document_name:
            if not self.parent.document_name.endswith('.shalla'): 
                self.parent.document_name += '.shalla'

        with open(self.parent.document_name, 'wt') as doc:
            doc.write(self.parent.text.toHtml())

        self.parent.saved = True

    def preview(self):
        '''
        backend function to get a print preview of the current document
        '''
        preview = QtPrintSupport.QPrintPreviewDialog()
        preview.paintRequested.connect(lambda p: self.parent.text.print_(p))
        preview.exec_()

    def print_page(self):
        '''
        backend function for printing the current document
        '''
        print_box = QtPrintSupport.QPrintDialog() 

        if print_box.exec_() == QtWidgets.QDialog.Accepted:
            self.parent.text.document().print_(print_box.printer())


    def numbered(self):
        '''
        backend function to create numbered list
        '''
        cursor = self.parent.text.textCursor()
        cursor.insertList(QtGui.QTextListFormat.ListDecimal)

    def bullet(self):
        '''
        backend function to create bullet list
        '''
        cursor = self.parent.text.textCursor()
        cursor.insertList(QtGui.QTextListFormat.ListDisc)

    def table(self):
        '''
        create table trigger function
        spawns a UI asking for table properties, creates a table and then inserts 
        it into the document
        '''
        
        #create a Table object. Def is in extensions 
        table_object = insert_table.Table(self.parent)
        table_object.show()

    def document_stats(self):
        stats = document_statistics.DocumentStatistics(self.parent)
        stats.process()
        stats.show()

