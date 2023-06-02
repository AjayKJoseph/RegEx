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
        
        # x = 'a few unexpected words are to be expected'
        x = re.sub('^(?<!\S)\d(?!\S)(.*?)(available\n)$', "dfffffg", x) # https://www.youtube.com/watch?v=p_6ZhMjh__4
        # print(x)
        
        # x = re.findall('^(?<!\S)\d(?!\S)(.*?)(available\n)$', x)
        print(x)
        # print(type(x))
        

        # print("Name:", self.name.text)
        # self.name.text = ""

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()