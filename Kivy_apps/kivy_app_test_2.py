import kivy
kivy.require('1.11.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class LoginScreen(GridLayout):

    # **kwargs is telling the constructor to accept an unlimited and unknown amount of inputs
    def __init__(self, **kwargs):
        #use super() here to call the constructor of the inherited class GridLayout
        super(LoginScreen, self).__init__(**kwargs)
        #amount of columns 
        self.cols = 1
        #creating a grid layout to put in the main grid layout (inception)
        self.inside = GridLayout()
        self.inside.cols = 2
        
        #adding First Name label and text box
        self.inside.add_widget(Label(text='Name: '))
        #only want one line of text
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)
        
        #adding Last Name Label and text box
        self.inside.add_widget(Label(text='Last Name: '))
        self.LastName = TextInput(multiline=False)
        self.inside.add_widget(self.LastName)
        
        #adding email label and text box
        self.inside.add_widget(Label(text='Email: '))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)
        
        #This adds the self.inside gridlayout to the main grid layout as a widget
        self.add_widget(self.inside)
        
        #add submit button
        self.submit = Button(text = 'Submit', font_size = 40)
        self.submit.bind(on_press = self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        name = self.name.text
        last = self.LastName.text
        email = self.email.text
        
        print("Name: ", name, 'Last Name: ', last, 'Email: ', email)
        self.name.text = ''
        self.LastName.text = ''
        self.email.text = ''
        
        
        
class MyApp(App):

    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run() 