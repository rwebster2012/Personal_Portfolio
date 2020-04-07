
#below code is using float layout as well as showinf how to change font and background

<Button>:
    font_size: 40
    color: 0.1,0.5,0.6,1
    size_hint: 0.5,0.5

<FloatLayout>:
    Button:
        text: "Tech With"
        pos_hint: {"x":0.5, "top":1}

    Button:
        id: btn
        text:"Tim" if btn.state == "normal" else "down"
        
        
#Below is code for chasnging windows and creating window classes (Separate lesson from above)
        
        
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

#This builder allows you to load any kv file you need
kv = Builder.load_file("my.kv")


class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()
    
    
# Below is the kv file
    
WindowManager:
    MainWindow:
    SecondWindow:

<MainWindow>:
    name: "main"

    GridLayout:
        cols:1

        GridLayout:
            cols: 2

            Label:
                text: "Password: "

            TextInput:
                id: passw
                multiline: False

        Button:
            text: "Submit"
            on_release:
                app.root.current = "second" if passw.text == "tim" else "main"
                root.manager.transition.direction = "left"


<SecondWindow>:
    name: "second"

    Button:
        text: "Go Back"
        on_release:
            app.root.current = "main"
            root.manager.transition.direction = "right"