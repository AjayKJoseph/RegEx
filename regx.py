import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
import re
from kivy.properties import StringProperty
import os
import unicodedata # https://youtu.be/Dkh0nFoEwLs?t=638 - not useful


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
        # patrn = r"(?<=Bourns).*" - Works to identify the line with keyword
        patrn = r"(Each)|(−)|(\+)|(Total)|((£).*)"
                #  ^^^^^^ - look for keyword "Each" OR
                #        ^^^^ - dash symbol OR
                #            ^^^^^ - "+" symbol OR
                #                 ^^^^^^^^ - keyword "Total" OR
                #                         ^^^^^^^^ - "£" and until new line OR
                #                                 ^^^^ - any new line characters (optional)
        
        # https://youtu.be/_uPsxnIg0uU?t=128 - look ahead/behind or leading/trailing
        # https://betterprogramming.pub/demystifying-look-ahead-and-look-behind-in-regex-4a604f99fb8c
        patrn2 = r".*(?=available)" # Positive look-ahead for "available" keyword
        patrn3 = r".*(?=(\d+/\d+/\d+))" # Positive look-ahead for date dd/mm/yyyy
        patrn4 = r"(\d+/\d+/\d+)"
        patrn5 = r"(No\.\r\n)*"
        # patrn4 = r"[(\n)\d(\n)+]"

        #################################################################################        
        # # re.groups with re.compile
        # pattern = re.compile(patrn) # https://www.youtube.com/watch?v=p_6ZhMjh__4
        # matches = pattern.finditer(txtInput) 
        # for match in matches:
        #     print("Bourns" + match.group(0))
        #################################################################################
        
        # # re.compile with findall - [], finditer returns first occurance
        # pattern = re.compile(r"(?<=Molex).*")
        # print(pattern.findall(txtInput))
        #################################################################################
        
        # # re.search with groupS w/o index = tuple
        # pattern = re.search("(?<=Molex).*", txtInput)
        # print(pattern.groups())            
        #################################################################################
        
        # # re.search with group with index = string
        # pattern = re.search("(?<=Bourns).*", txtInput)
        # print(pattern.group(1))
        #################################################################################
        
        # re.sub to replace 
        
        filteredTxt = re.sub(patrn, "", txtInput)
        filteredTxt = re.sub(patrn2 + "|available", "", filteredTxt)
        filteredTxt = re.sub(patrn3, "", filteredTxt)
        filteredTxt = re.sub(patrn4, "", filteredTxt)
        filteredTxt = re.sub(patrn5, "", filteredTxt)
        # # https://stackoverflow.com/questions/3711856/how-to-remove-empty-lines-with-or-without-whitespace-in-python
        filteredTxt = re.sub(r'\s{2}', '', filteredTxt) 
        print(filteredTxt)
        
        # re.sub(((\d+ Available).*)|((\d+ In).*), )
        
        
        

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
    