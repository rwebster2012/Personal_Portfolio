def ground(package_weight):
    if package_weight <= 2:
        price = 20 + 1.50 * package_weight
    elif package_weight > 2 and package_weight <= 6:
        price = 20 + 3.00 * package_weight
    elif package_weight > 6 and package_weight <= 10:
        price = 20 + 4.00 * package_weight
    elif package_weight > 10:
        price = 20 + 4.7 * package_weight
    return price

def drone(package_weight):
    if package_weight <= 2:
        price = 4.50 * package_weight
    elif package_weight > 2 and package_weight <= 6:
        price = 9.00 * package_weight
    elif package_weight > 6 and package_weight <= 10:
        price = 12.00 * package_weight
    elif package_weight > 10:
        price = 14.25 * package_weight
    return price




def shipping_selector(package_weight):
    if ground(package_weight) < drone(package_weight) and ground(package_weight) < 125:
        return "The cheapest shipping method for your selected package is Ground Shipping at $" + str(ground(package_weight))
    elif drone(package_weight) < ground(package_weight) and drone(package_weight) < 125:
        return "The cheapest shipping method for your selected package is Drone Shipping at $" + str(drone(package_weight))
    else:
        return "The cheapest shipping method for your selected package is Premium Ground Shipping at $125.00"
  
print(shipping_selector(25))


#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 14:06:19 2020

@author: Deborah
"""

