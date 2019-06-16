import sys
from PyQt5 import QtWidgets, QtPrintSupport, QtGui, QtCore
from PyQt5.QtCore import Qt 
import itertools

class FormatBar(QtWidgets.QMainWindow):

    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self, parent)
        
        #inherit from the Main class
        self.parent = parent
        
        #Initialize the toolbar
        self.setup_formatbar()


    def make_action(self, name, icon_path, func, shortcut, tip):
            '''
            function to make a new action for the formatbar
            @arg: a list containing [name, icon path, slot_function, shortcut, tip]
            @return: the newly made action
            '''
            action = QtWidgets.QAction(QtGui.QIcon(icon_path), name, self.parent)
            action.setShortcut(shortcut)
            action.setStatusTip(tip)
            action.triggered.connect(func)

            return action    

    def setup_formatbar(self):
        
        #make formatbar actions
        font_color_action = self.make_action('Choose font color', 'icons/color.png', 
            self.change_color, 'Shift + C', 'Chose font color')
        italic_action = self.make_action('Set italic', 'icons/italic.png', 
            self.set_italic, 'Shift + I', 'Set selection to Italic')
        bold_action = self.make_action('Set bold', 'icons/bold.png', 
            self.set_bold, 'Shift + B', 'Set selection to Bold')
        underline_action = self.make_action('Underline', 'icons/underline.png', 
            self.underline, 'Shift + U', 'Underline')
        strike_action = self.make_action('Strike', 'icons/strike.png', 
            self.strike, 'Shift + S', 'Strike')
        highlight_action = self.make_action('Highlight', 'icons/highlight.png', 
            self.highlight, 'Shift + H', 'Highlight')
        super_action = self.make_action('Super script', 'icons/super.png', 
            self.super_script, 'Ctrl + Shift + U', 'Super Script')
        sub_action = self.make_action('Sub script', 'icons/sub.png', 
            self.sub_script, 'Ctrl + Shift + S', 'Sub script')
        align_left_action = self.make_action('Align Left', 'icons/align_left.png', 
            self.left_justify, 'Shift + L', 'Left justify')
        align_right_action = self.make_action('Align right', 'icons/align_right.png', 
            self.right_justify, 'Shift + R', 'Right justify')
        align_center_action = self.make_action('Align center', 'icons/align_center.png', 
            self.center_justify, 'Shift + C', 'Center justify')
        align_justify_action = self.make_action('Align justify', 'icons/align_justify.png', 
            self.justify, 'Shift + J', 'Justify')
        indent_action = self.make_action('Indent', 'icons/indent.png', 
            self.indent, 'Ctrl + Shift + I', 'Indent')
        dedent_action = self.make_action('Dedent', 'icons/dedent.png', 
            self.dedent, 'Ctrl + Shift + D', 'Dedent')

        font_bar = QtWidgets.QFontComboBox(self.parent)
        font_bar.currentFontChanged.connect(lambda font: self.parent.text.setCurrentFont(font))

        font_size = QtWidgets.QSpinBox(self.parent)
        font_size.valueChanged.connect(lambda size: self.parent.text.setFontPointSize(size))
        font_size.setValue(14)

        self.formatbar = self.parent.addToolBar('Format Bar')

        self.formatbar.addWidget(font_bar)
        self.formatbar.addWidget(font_size)
        self.formatbar.addSeparator()
        self.parent.addToolBarBreak()

        self.formatbar.addAction(font_color_action)
        self.formatbar.addAction(highlight_action)
        self.formatbar.addSeparator()
        self.parent.addToolBarBreak()
        
        self.formatbar.addAction(italic_action)
        self.formatbar.addAction(bold_action)
        self.formatbar.addAction(strike_action)
        self.formatbar.addAction(underline_action)
        self.formatbar.addAction(sub_action)
        self.formatbar.addAction(super_action)
        self.formatbar.addSeparator()
        self.parent.addToolBarBreak()

        self.formatbar.addAction(align_left_action)
        self.formatbar.addAction(align_right_action)
        self.formatbar.addAction(align_center_action)
        self.formatbar.addAction(align_justify_action)
        self.formatbar.addAction(indent_action)
        self.formatbar.addAction(dedent_action)
        self.formatbar.addSeparator()
        self.parent.addToolBarBreak()
    
        


    #functions that are triggered when a button is pressed

    def set_italic(self):
        italic = self.parent.text.fontItalic()
        self.parent.text.setFontItalic(not italic)

    def set_bold(self):
        if self.parent.text.fontWeight() == QtGui.QFont.Bold:
            self.parent.text.setFontWeight(QtGui.QFont.Normal)
        else: self.parent.text.setFontWeight(QtGui.QFont.Bold)

    def underline(self):
        underline = self.parent.text.fontUnderline()
        self.parent.text.setFontUnderline(not underline)

    def strike(self):
        strike_status = self.parent.text.currentCharFormat()
        strike_status.setFontStrikeOut(not strike_status.fontStrikeOut())
        self.parent.text.setCurrentCharFormat(strike_status)
    
    def sub_script(self):
        sub_status = self.parent.text.currentCharFormat()
        align = sub_status.verticalAlignment()

        if align == QtGui.QTextCharFormat.AlignNormal:
            sub_status.setVerticalAlignment(QtGui.QTextCharFormat.AlignSubScript)
        else:
            sub_status.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)

        self.parent.text.setCurrentCharFormat(sub_status)

    def super_script(self):
        super_status = self.parent.text.currentCharFormat()
        align = super_status.verticalAlignment()

        if align == QtGui.QTextCharFormat.AlignNormal:
            super_status.setVerticalAlignment(QtGui.QTextCharFormat.AlignSuperScript)
        else:
            super_status.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)

        self.parent.text.setCurrentCharFormat(super_status)

    def highlight(self):
        color = QtWidgets.QColorDialog.getColor()
        self.parent.text.setTextBackgroundColor(color)

    def change_color(self):
        color = QtWidgets.QColorDialog.getColor()
        self.parent.text.setTextColor(color)

    def left_justify(self):
        self.parent.text.setAlignment(Qt.AlignLeft)

    def right_justify(self):
        self.parent.text.setAlignment(Qt.AlignRight)

    def center_justify(self):
        self.parent.text.setAlignment(Qt.AlignCenter)

    def justify(self):
        self.parent.text.setAlignment(Qt.AlignJustify)

    #indent and dedent work only when the function is called within document size 
    def indent(self):
        cursor = self.parent.text.textCursor()

        if cursor.hasSelection():
            #calculate the diff between start and end of selection
            temp = cursor.blockNumber()
            cursor.setPosition(cursor.anchor())
            diff = cursor.blockNumber() - temp
            direction = QtGui.QTextCursor.Up if diff > 0 else QtGui.QTextCursor.Down

            #Go through all the lines in the diff
            for n in range(abs(diff) + 1):
                cursor.movePosition(QtGui.QTextCursor.StartOfLine)
                cursor.insertText("\t")
                cursor.movePosition(direction)
        #In case there is no selection, insert tab
        else:
            cursor.insertText("\t")

    def dedent(self):
        cursor = self.parent.text.textCursor()

        if cursor.hasSelection():
            #calculate the diff between start and end of selection
            temp = cursor.blockNumber()
            cursor.setPosition(cursor.anchor())
            diff = cursor.blockNumber() - temp
            direction = QtGui.QTextCursor.Up if diff > 0 else QtGui.QTextCursor.Down

            #iterate over all lines
            for n in range(abs(diff) + 1):
                #move to start of line, insert tab, then move back up
                cursor.movePosition(QtGui.QTextCursor.StartOfLine)
                line = cursor.block().text()
                if line.startswith("\t"):
                    cursor.deleteChar()
                else:
                    for char in line[:8]:
                        if char != " ": break
                        cursor.deleteChar()
                
                cursor.movePosition(direction)
        else:
            cursor.movePosition(QtGui.QTextCursor.StartOfLine)
            line = cursor.block().text()

            if line.startswith("\t"):
                cursor.deleteChar()
            else:
                for char in line[:8]:
                    if char != " ": break
                    cursor.deleteChar()



