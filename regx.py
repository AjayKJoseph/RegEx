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


class MyGrid(Widget):
    if os.path.exists("basketList.txt"):
        with open('basketList.txt') as txtFile:
            test = txtFile.read()       
            urs = StringProperty(test)
    else:
        urs = StringProperty()
        
    # name = ObjectProperty(None)
        
    def btn(self):
        x = self.name.text
        
        # re.groups with re.compile
        pattern = re.compile(r"(?<=Bourns).*") # https://www.youtube.com/watch?v=p_6ZhMjh__4
        matches = pattern.finditer(x) 
        for match in matches:
            print("Bourns" + match.group(0))
        
        # # re.compile with findall - [], finditer returns first occurance
        # pattern = re.compile(r"(?<=Molex).*")
        # print(pattern.findall(x))
        
        # # re.search with groupS w/o index = tuple
        # pattern = re.search("(?<=Molex).*", x)
        # print(pattern.groups())            
        
        # # re.search with group with index = string
        # pattern = re.search("(?<=Bourns).*", x)
        # print(pattern.group(1))        

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
    