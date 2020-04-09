from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase
from kivy.uix.dropdown import DropDown
from kivy.base import runTouchApp
from kivy.uix.button import Button


class WelcomeWindow(Screen):
    
    
    def Create(self):
        sm.current = "Create Recipe"
    def Load(self):
        sm.current = "Load"

class LoadPreviousRecipe(Screen):
    
    
    def RecipeStats(self):
        sm.current = "stats"
    def ReturnHome(self):
        sm.current = "Welcome"

class CreateRecipeWindow(Screen):
    recipename = ObjectProperty(None)
    finalvolume = ObjectProperty(None)
    preboilgravity = ObjectProperty(None)
    boiltime = ObjectProperty(None)
    
    def ReturnHome(self):
        sm.current = "Welcome"
        
    def submit(self):
        if self.recipename.text != "" and self.finalvolume.text != "" and self.preboilgravity.text != '' and self.boiltime.text != '':
            db1.add_recipe(self.recipename.text, self.finalvolume.text, self.preboilgravity.text, self.boiltime.text)
            current_recipe_name = self.recipename.text
            self.reset()
            sm.current = "Add Hops"
        else:
            invalidForm()
    
    def reset(self):
        self.recipename.text = ""
        self.finalvolume.text = ""
        self.preboilgravity.text = ""
        self.boiltime.text = ""

class AddHopsWindow(Screen):
    recipename = current_recipe_name
    hopname = ObjectProperty(None)
    hoptiming = ObjectProperty(None)
    hopweight = ObjectProperty(None)
    hopacid = ObjectProperty(None)
    
    def submithop(self):
        if self.hopname.text != "" and self.hoptiming.text != "" and self.hopweight.text != '' and self.hopacid.text != '':
            db2.add_hops(recipename, self.hopname.text, self.hoptiming.text, self.hopweight.text, self.hopacid.text)
            self.reset()
            sm.current = "Add Hops"
        else:
            invalidForm()
    
    def submitrecipe(self):
        sm.current = "stats"
        
    
    def reset(self):
        self.hopname.text = ""
        self.hoptiming.text = ""
        self.hopweight.text = ""
        self.hopacid.text = ""
    
    def RecipeStats(self):
        sm.current = "stats"
    def ReturnHome(self):
        sm.current = "Welcome"

class TimerWindow(Screen):
    
    
    def RecipeStats(self):
        sm.current = "stats"
    def ReturnHome(self):
        sm.current = "Welcome"
        
        
class RecipeStatsWindow(Screen):
    
    def RecipeStats(self):
        sm.current = "stats"
    def ReturnHome(self):
        sm.current = "Welcome"

class HopListWindow(Screen):
    
    def RecipeStats(self):
        sm.current = "stats"
    def ReturnHome(self):
        sm.current = "Welcome"



class WindowManager(ScreenManager):
    pass

class CustomDropDown(DropDown):
    pass

dropdown = CustomDropDown()
mainbutton = Button(text='Hello', size_hint=(None, None))
mainbutton.bind(on_release=dropdown.open)
dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))



def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()




kv = Builder.load_file("my.kv")

sm = WindowManager()
db1 = DataBase("recipestats.txt")
db2 = DataBase("recipehops.txt")

screens = [HopListWindow(name='HopList'), CreateRecipeWindow(name="Create Recipe"), TimerWindow(name="Timer"), RecipeStatsWindow(name="stats"), WelcomeWindow(name="Welcome"), LoadPreviousRecipe(name="Load"), AddHopsWindow(name="Add Hops")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "Welcome"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 17:19:44 2020

@author: ryanwebster
"""

