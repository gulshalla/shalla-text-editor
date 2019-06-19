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
        
        #Initialize the parent.tool_bar
        self.setup_toolbar()

    def make_action(self, arg):
            '''
            function to make a new action for the parent.tool_bar
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
        ('Open', 'icons/open.png', self.open, 'Ctrl+O', 'Open existing file'),
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
            'Document statistics'), 
        ('English Dictionary', 'icons/dict.png', self.dictionary_check, 'Ctrl + Shift + D',
            'English Dictionary'), 
        ('Insert image', 'icons/image.png', self.insert_image, 'Ctrl + Shift + I', 'Insert image'),
        ('Find and Replace', 'icons/find_replace.png', self.find_replace, 'Ctrl + F', 'Find and Replace'),
        ('Spell Check', 'icons/spell_check.png', self.spellcheck, 'Ctrl + Shift + S', 'Spell Check'),
        ('Thesaurus', 'icons/thesaurus.png', self.thesaurus, 'Ctrl + Shift + T', 'Thesaurus'),
        ('Spelling Suggestions', 'icons/spelling.png', self.spelling, 'Ctrl + Shift + C', 'Spelling suggestions'),
        ('Partial Matches', 'icons/partial.png', self.partial, 'Ctrl + Shift + M', 'Partial matches'), 
        ('Shortcuts', 'icons/shortcuts.png', self.shortcuts, 'Ctrl + Alt + S', 'Shortucts')] 

        # create new actions
        counter = itertools.count()
        self.parent.new_action = self.make_action(actions[next(counter)])
        self.parent.open_action = self.make_action(actions[next(counter)])
        self.parent.save_action = self.make_action(actions[next(counter)])
        self.parent.print_action = self.make_action(actions[next(counter)])
        self.parent.preview_action = self.make_action(actions[next(counter)])
        self.parent.cut_action = self.make_action(actions[next(counter)])
        self.parent.copy_action = self.make_action(actions[next(counter)])
        self.parent.paste_action = self.make_action(actions[next(counter)])
        self.parent.undo_action = self.make_action(actions[next(counter)])
        self.parent.redo_action = self.make_action(actions[next(counter)])
        self.parent.bullet_action = self.make_action(actions[next(counter)])
        self.parent.numbered_action = self.make_action(actions[next(counter)])
        self.parent.table_action = self.make_action(actions[next(counter)])
        self.parent.document_statistics_action = self.make_action(actions[next(counter)])
        self.parent.dictionary_action = self.make_action(actions[next(counter)])
        self.parent.insert_image_action = self.make_action(actions[next(counter)])
        self.parent.find_replace_action = self.make_action(actions[next(counter)])
        self.parent.spell_check_action = self.make_action(actions[next(counter)])
        self.parent.thesaurus_action = self.make_action(actions[next(counter)])
        self.parent.spelling_action = self.make_action(actions[next(counter)])
        self.parent.partial_action = self.make_action(actions[next(counter)])
        self.parent.shortcuts_action = self.make_action(actions[next(counter)])
        

        # add them to the parent.tool_bar
        self.parent.tool_bar = self.parent.addToolBar("ToolBar")
        self.toolbar = self.parent.tool_bar
        self.toolbar.addAction(self.parent.new_action)
        self.toolbar.addAction(self.parent.open_action)
        self.toolbar.addAction(self.parent.save_action)
        self.toolbar.addSeparator()

        self.toolbar.addAction(self.parent.print_action)
        self.toolbar.addAction(self.parent.preview_action)
        self.toolbar.addSeparator()

        self.toolbar.addAction(self.parent.cut_action)
        self.toolbar.addAction(self.parent.copy_action)
        self.toolbar.addAction(self.parent.paste_action)
        self.toolbar.addAction(self.parent.undo_action)
        self.toolbar.addAction(self.parent.redo_action)
        self.toolbar.addSeparator()

        self.toolbar.addAction(self.parent.insert_image_action)
        self.toolbar.addAction(self.parent.bullet_action)
        self.toolbar.addAction(self.parent.numbered_action)
        self.toolbar.addAction(self.parent.table_action)
        self.toolbar.addSeparator()

        self.toolbar.addAction(self.parent.find_replace_action)
        self.toolbar.addAction(self.parent.partial_action)
        self.toolbar.addAction(self.parent.document_statistics_action)
        self.toolbar.addAction(self.parent.spell_check_action)
        self.toolbar.addAction(self.parent.dictionary_action)
        self.toolbar.addAction(self.parent.thesaurus_action)
        self.toolbar.addAction(self.parent.spelling_action)
        self.toolbar.addSeparator()
        
        self.toolbar.addAction(self.parent.shortcuts_action)
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

        if self.parent.document_name:
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

    def insert_image(self):
        image_file = QtWidgets.QFileDialog.getOpenFileName(self.parent, 
            'Insert image', '.', 'Images (*.png *.jpg *.bmp *.gif)')[0]

        if image_file:
            image = QtGui.QImage(image_file)
            print(type(image))
            cursor = self.parent.text.textCursor()
            print(type(cursor))
            if image.isNull():
                error = 'Image could not load'
                popup = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical,
                    error, error, QtWidgets.QMessageBox.Ok, self.parent)
                popup.show()
            else:
                cursor = self.parent.text.textCursor()
                cursor.insertImage(image, image_file)

    def dictionary_check(self):
        cursor = self.parent.text.textCursor()
        if cursor.hasSelection():
            tc = self.parent.text.textCursor()
            tc.select(QtGui.QTextCursor.WordUnderCursor) 
            word = tc.selectedText().lower()
            if word in self.parent.dictionary and self.parent.dictionary[word] != 1:
                dictionary_app = dictionary_widget.DictionaryWidget(self.parent, tc.selectedText().lower())
                dictionary_app.get_meaning()
                dictionary_app.show()
            else:
                window = 'Key Error'
                error = 'Word not in dictionary!'
                popup = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical,
                    window, error, QtWidgets.QMessageBox.Ok, self.parent)
                popup.show()

        else:
            window = 'Empty string'
            error = 'Make a selection first!'
            popup = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical,
                window, error, QtWidgets.QMessageBox.Ok, self.parent)
            popup.show()

    def find_replace(self):
        find = find_and_replace.FindReplace(self.parent)
        find.show()

    def spellcheck(self):
        spell_check.wrong_spelling(self.parent)

    def thesaurus(self):
        thesaurus_widget = thesaurus.Thesaurus(self.parent)
        thesaurus_widget.get_synonyms()

    def spelling(self):
        obj = spell_suggest.SpellSuggest(self.parent)
        obj.get_suggestions()

    def partial(self):
        obj = partial_match.PartialMatch(self.parent)
        obj.get_matches()        

    def shortcuts(self):
        obj = shortcuts.Shortcuts(self.parent)
        obj.show()

