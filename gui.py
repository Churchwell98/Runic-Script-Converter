'''
Runic Script Converter
Creator: Dylan Church
Creation Date: 10/2/2023
This is the GUI
text box needs to be self (idk why)
Works, success!

ᚱᚢᚾᛁᚳ ᛋᚳᚱᛁᛈᛏ ᚳᚩᚾᚢᛖᚱᛏᛖᚱ
ᚳᚱᛠᛏᚩᚱ: ᛞᚣᛚᚪᚾ ᚳᚻᚢᚱᚳᚻ
ᚳᚱᛠᛏᛁᚩᚾ ᛞᚪᛏᛖ: 10/2/2023
ᚦᛁᛋ ᛁᛋ ᚦᛖ ᚷᚢᛁ
ᛏᛖᛉᛏ ᛒᚩᛉ ᚾᛟᛞᛋ ᛏᚩ ᛒᛖ ᛋᛖᛚᚠ (ᛁᛞᛱ ᚹᚻᚣ)
ᚹᚩᚱᛱᛋ, ᛋᚢᚳᚳᛖᛋᛋ!
'''

#Import
import sys# Only needed for access to command line arguments
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, 
                             QLabel, QComboBox, QTextEdit)
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont
import la_to_ru,ru_to_la#Import script conversion functions

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()#ALWAYS required when you subclass a Qt class

        #Declaration
        self.current_input_script="Latin"
        self.current_output_script="Latin"
        self.current_language="English"

        self.setWindowTitle("Runic Script Converter")
        self.setMinimumSize(QSize(1200,1000))#Set Window Size
        
        #Create layouts (refer to app_layout_stack.py and stacked layout demo)
        layout_window = QHBoxLayout()#Create Horizontal Layout for window
        layout_left=QVBoxLayout()#Layout for left side
        layout_middle=QVBoxLayout()#Layout for Middle
        layout_right=QVBoxLayout()#Layout for right side

        #Fonts
        left_font=QFont()
        left_font.setPointSize(20)#Set font size
        middle_font=QFont()
        middle_font.setPointSize(16)#Set font size
        text_font=QFont()
        text_font.setPointSize(14)

        #Left Layout
        left_label=QLabel("Input Script")#Label (see label.py)
        left_label.setFont(left_font)
        input_script=QComboBox()#Drop down list (see app_widget.py)
        input_script.setFont(text_font)
        input_script.addItems(["Latin","Runic"])
        input_script.currentTextChanged.connect(self.input_script_changed)
        self.input_text = QTextEdit(self,
			plainText="Input text",
			acceptRichText= False,
			#lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
			#lineWrapColumnOrWidth=75,
			#placeholderText="Hello World!",
			readOnly=False,
			)#Text box (see textbox.py)
        self.input_text.setFont(text_font)
        layout_left.addWidget(left_label)
        layout_left.addWidget(input_script)
        layout_left.addWidget(self.input_text)

        #Middle Layout
        middle_lable=QLabel("Select language")#Label
        middle_lable.setFont(middle_font)
        language=QComboBox()#Drop down list
        language.setFont(text_font)
        language.addItems(["English","Swedish"])
        language.currentTextChanged.connect(self.language_changed)
        button=QPushButton("Convert")#Button (see hello_world.py)
        button.setCheckable(True)
        button.clicked.connect(self.button_clicked)
        button.setFont(text_font)
        layout_middle.addWidget(middle_lable)
        layout_middle.addWidget(language)
        layout_middle.addWidget(button)

        #Right Layout
        right_label=QLabel("Output Script")#Label
        right_label.setFont(left_font)#Set font (same as left)
        output_script=QComboBox()#Drop down list
        output_script.setFont(text_font)
        output_script.addItems(["Latin","Runic"])
        output_script.currentTextChanged.connect(self.output_script_changed)
        self.output_text = QTextEdit(self,
			#plainText="Input text",
			acceptRichText= False,
			#lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
			#lineWrapColumnOrWidth=75,
			#placeholderText="Hello World!",
			readOnly=False,
			)#Text box
        self.output_text.setFont(text_font)
        layout_right.addWidget(right_label)
        layout_right.addWidget(output_script)
        layout_right.addWidget(self.output_text)

        #Add layouts
        layout_window.addLayout(layout_left)
        layout_window.addLayout(layout_middle)
        layout_window.addLayout(layout_right)

        widget = QWidget()
        widget.setLayout(layout_window)
        self.setCentralWidget(widget)

    def button_clicked(self):#Convert button clicked
        #self.output_text.setPlainText(self.input_text.toPlainText())
        if self.current_input_script=="Latin" and self.current_output_script=="Runic":
            print("Converting from Latin to Runic script")#Convert from Latin to Runic
            if self.current_language=="English":
                print("English")#Convert English
                converted_text=la_to_ru.convert_Eng(self.input_text.toPlainText())
                self.output_text.setPlainText(converted_text)
            elif self.current_language=="Swedish":
                print("Swedish")#Convert Swedish
                converted_text=la_to_ru.convert_Swe(self.input_text.toPlainText())
                self.output_text.setPlainText(converted_text)
            else:
                print("Invalid")
        elif self.current_input_script=="Runic" and self.current_output_script=="Latin":
            print("Converting from Runic to Latin script")#Convert from Runic to Latin
            if self.current_language=="English":
                print("English")#Convert English
                converted_text=ru_to_la.convert_Eng(self.input_text.toPlainText())
                self.output_text.setPlainText(converted_text)
            elif self.current_language=="Swedish":
                print("Swedish")#Convert Swedish
                converted_text=ru_to_la.convert_Swe(self.input_text.toPlainText())
                self.output_text.setPlainText(converted_text)
            else:
                print("Invalid")
        else:
            print("Invalid")

    def input_script_changed(self,s):#s is a string
        self.current_input_script=s
        print(s)#Placeholder

    def output_script_changed(self,s):#s is a string
        self.current_output_script=s
        print(s)#Placeholder

    def language_changed(self,s):#s is a string
        self.current_language=s
        print(self.current_language)#Placeholder

app = QApplication(sys.argv)#Create QApplication instance

window = MainWindow()#Create QT widget as main window
window.show()#Show window (windows are HIDDEN by default)

app.exec()#Start event loop