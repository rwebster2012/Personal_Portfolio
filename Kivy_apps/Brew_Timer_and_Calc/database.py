import datetime
import csv

class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.recipes = None
        self.hops = None
        self.file = None
        self.load()

    def load(self):
        self.recipes = {}
        self.file = open(self.filename, "r")
        
        for line in self.file:
            recipename, finalvolume, preboilgravity, boiltime = line.strip().split("$")
            self.recipes[recipename] = (finalvolume, preboilgravity, boiltime)
    
    def add_recipe(self, recipename, finalvolume, preboilgravity, boiltime):
        if recipename.strip() not in self.recipes:
            self.recipes[recipename.strip()] = (finalvolume.strip(), preboilgravity.strip(), boiltime.strip())
            self.save()
            return 1
        else:
            print("Recipe Name Already Exists")
            return -1
    
    def save(self):
        with open(self.filename, "w") as f:
            for recipe in self.recipes:
                f.write(recipe + "$" + self.recipes[recipe][0] + "$" + self.recipes[recipe][1] + "$" + self.recipes[recipe][2] + "\n")   
                
    
#    def loadhops(self):
#        self.hops = {}
#        self.file = open(self.filename, "r")
#        
#        for line in self.file:
#            line.strip().split("$")
#            recipename = line[0]
#            self.hops[recipename] = line[1:]
#       
#    
#    def add_hops(self, recipename, hopname, hoptiming, hopweight, hopacid):
#        self.loadhops()
#        if recipename.strip() not in self.recipes:
#            self.recipes[recipename.strip()] = (finalvolume.strip(), preboilgravity.strip(), boiltime.strip())
#            self.save()
#            return 1
#        else:
#            print("Recipe Name Already Exists")
#            return -1
         
                
         
#class DataBase:
#    def __init__(self, filename):
#        self.filename = filename
#        self.users = None
#        self.file = None
#        self.load()
#
#    def load(self):
#        self.file = open(self.filename, "r")
#        self.users = {}
#
#        for line in self.file:
#            email, password, name, created = line.strip().split(";")
#            self.users[email] = (password, name, created)
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
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 17:20:36 2020

@author: ryanwebster
"""

