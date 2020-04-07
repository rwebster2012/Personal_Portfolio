import kivy
kivy.require('1.11.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout

class MyGrid(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)
    btn = ObjectProperty(None)
    
    
    def btn(self):
        print("Name: ", self.name.text, 'Email: ', self.email.text)
        self.name.text = ''
        self.email.text = '' 
    
    def on_touch_down(self, touch):
        print("Mouse Down", touch)
        self.btn.opacity = 0.5
    
    def on_touch_move(self, touch):
        print("Mouse Move", touch)
    
    def on_touch_up(self, touch):
        print("Mouse UP", touch)
        self.btn.opacity = 1


class MyApp(App):

    def build(self):
        return MyGrid()

if __name__ == '__main__':
    MyApp().run() 