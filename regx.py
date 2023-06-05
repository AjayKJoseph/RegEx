from kivy.app import App
from kivy.uix.widget import Widget
import re
from kivy.properties import StringProperty
import os
from kivy.core.window import Window

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder

Window.size = (600, 800)

Builder.load_file('myapp.kv')

class MyGrid(Widget):
    if os.path.exists("basketList.txt"):
        # https://docs.python.org/3/howto/unicode.html - Reading Unicode from a file
        with open('basketList.txt', encoding='utf-8') as txtFile: 
            test = txtFile.read()       
            urs = StringProperty(test)
    else:
        urs = StringProperty()
        
        
    def btn(self):
        txtInput = self.name.text
        
        # https://youtu.be/_uPsxnIg0uU?t=128 - look ahead/behind or leading/trailing        
        # https://youtu.be/_uPsxnIg0uU?t=128 - look ahead/behind or leading/trailing
        # https://betterprogramming.pub/demystifying-look-ahead-and-look-behind-in-regex-4a604f99fb8c
        patrn1 = r"(Each)|(Total)|((£).*)|(([\b−\b].*)(\n\w+)|([\b+\b]))"
        patrn2 = r".*(?=available)" # Positive look-ahead for "available" keyword
        patrn3 = r".*(?=(\d+/\d+/\d+))" # Positive look-ahead for date dd/mm/yyyy
        patrn4 = r"(\d+/\d+/\d+)"
        patrn5 = r"(No\.\n)"
        patrn6 = r""
        
        
        filteredTxt = re.sub(patrn1, "", txtInput) 
        filteredTxt = re.sub(patrn2 + "|available", "\n", filteredTxt)
        filteredTxt = re.sub(patrn3, "", filteredTxt)
        filteredTxt = re.sub(patrn4, "\n", filteredTxt)
        filteredTxt = re.sub(patrn5, "No. ", filteredTxt)
        # # https://stackoverflow.com/questions/3711856/how-to-remove-empty-lines-with-or-without-whitespace-in-python
        filteredTxt = re.sub(r'\s{2}', '', filteredTxt) 
        filteredTxt = re.sub(r'^(Mfr).*', '\n', filteredTxt)
        
        print(filteredTxt)
        
        self.ids.label_output.text = filteredTxt
        # StringProperty(self.output.text)       

class MyApp(MDApp):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
    