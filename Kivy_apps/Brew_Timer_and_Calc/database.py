import datetime
import csv

class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.recipes = None
        self.file = None
        self.load()

    def load(self):
        self.recipe = {}
        self.recipe_information = {}
        with open(self.filename, newline='') as csvfile:
            self.file = csv.DictReader(csvfile, delimiter = '$')
        
       
            for line in self.file:
                print(line)
       
        
        #if self.file['Recipe Name'] == 'recipe1':
#            self.recipe = line
#        print(self.recipe)
#            recipe_name, recipe_profile  = line.strip().split("$")
#            self.recipes[recipe_name] = (recipe_profile)
#            for recipe in self.recipes:
#                recipe.strip().split(";")
#                
#        
#        self.file.close()
#
#    def get_user(self, email):
#        if email in self.users:
#            return self.users[email]
#        else:
#            return -1
#
#    def add_user(self, email, password, name):
#        if email.strip() not in self.users:
#            self.users[email.strip()] = (password.strip(), name.strip(), DataBase.get_date())
#            self.save()
#            return 1
#        else:
#            print("Email exists already")
#            return -1
#
#    def validate(self, email, password):
#        if self.get_user(email) != -1:
#            return self.users[email][0] == password
#        else:
#            return False
#
#    def save(self):
#        with open(self.filename, "w") as f:
#            for user in self.users:
#                f.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + ";" + self.users[user][2] + "\n")
#
#    @staticmethod
#    def get_date():
#        return str(datetime.datetime.now()).split(" ")[0]

recipes = DataBase('recipes.csv')
#recipes.load()


#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 17:20:36 2020

@author: ryanwebster
"""

