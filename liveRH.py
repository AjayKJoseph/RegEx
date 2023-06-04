from kaki.app import App
from kivy.factory import Factory
import os
from kivymd.app import MDApp

class LiveRH(App, MDApp): # variable class name
    CLASSES = {
        # requires exact main class and file name from .py(main)
        "MyGrid" : "regx" 
    }
    
    KV_FILES = {
        # requires exact kivy file name (.kv)
        os.path.join(os.getcwd(), "myapp.kv")
    }
    
    AUTORELOADER_PATHS = [
        # Always set this True
        (".", {"recursive" : True}) 
    ]
    
    # Use build_app() function instead of build()
    def build_app(self): 
        print("inside asdfas")
        return Factory.MyGrid() # Include the exact .py(main) class name with ()

LiveRH().run()