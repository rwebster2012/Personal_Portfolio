# below is .py file for kivy app demonstrating popup function

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup


class Widgets(Widget):
    def btn(self):
        show_popup()

class P(FloatLayout):
    pass


class MyApp(App):
    def build(self):
        return Widgets()


def show_popup():
    show = P()

    popupWindow = Popup(title="Popup Window", content=show, size_hint=(None,None),size=(400,400))

    popupWindow.open()


if __name__ == "__main__":
    MyApp().run()
    
    
#below is .kv file for above 
    
    <Widgets>:
    Button:
        text: "Press me"
        on_release: root.btn()

<P>:
    Label:
        text: "You pressed the button"
        size_hint: 0.6, 0.2
        pos_hint: {"x":0.2, "top":1}

    Button:
        text: "You pressed the button"
        size_hint: 0.8, 0.2
        pos_hint: {"x":0.1, "y":0.1}