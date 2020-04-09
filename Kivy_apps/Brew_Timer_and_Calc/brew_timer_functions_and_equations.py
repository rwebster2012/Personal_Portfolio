#write code below to take hop name, alpha acid%,  hop amount, boil time , and batch final volume
#implement a timer to help you remember to add a hops as well as 
#implement a calculator to calculate boil size given desired final batch volume
#implement an IBU calculator
#will need a text document to save recipes for future loading
from decimal import Decimal
import time



#format the hop list such that the key is boil time and the value is hop type and amount
#the below function takes in the above dictionary then gives countdowns to the next hop or 
# ingredient addition 
#at the end of the cycle it will tell you to proceed to the wort cooling step

def countdown_timer_hop_schedule(dictionary_of_hop_and_boil_time, boil_time_in_min = 60):
    
    boil_time_in_sec = boil_time_in_min * 60
    hop_list = dictionary_of_hop_and_boil_time
    profile_dict = {}
    
    for minutes, seconds in hop_list.keys():
        t = (minutes * 60) + seconds
        time_to_next_addition = boil_time_in_sec - t
        profile_dict[time_to_next_addition] = hop_list[(minutes, seconds)]
        
    
    accumulated_time = 0
    for time_to_addition in profile_dict.keys(): 
        t = time_to_addition - accumulated_time
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        accumulated_time += time_to_addition - accumulated_time
        print('Time to add: ' + str(profile_dict[time_to_addition]))
        print('\n\n')
    print('Proceed to wort cooling')

#sample_boil_profile = {(59,50): ('Warrior', '2.5oz'), (59,40): ('Amarillo', '3oz'), (00,15): ('Cascade', '3oz')}
#countdown_timer_hop_schedule(sample_boil_profile)


def boil_size_calculator(final_volume_desired, boil_time_in_min = 60):
    volume_left_in_fermenter = Decimal(1) / Decimal(4)
    volume_left_in_kettle = Decimal(1) / Decimal(3) 
    #assuming 1 gallon boil off per hour
    boil_off_volume = Decimal(boil_time_in_min) / Decimal(60)
    pre_boil_volume = final_volume_desired + volume_left_in_fermenter + volume_left_in_kettle + boil_off_volume
    return round(pre_boil_volume, 2)

#print(boil_size_calculator(5, 60))



#below we need the hop dictionary to also include alpha acid
def IBU_calculator(gravity_of_boil, dictionary_of_hop_and_boil_time, final_volume_desired):
    hop_list = dictionary_of_hop_and_boil_time
    Total_AAU = 0
    for minutes, seconds in hop_list:
        
        e = Decimal(2.71828)
        function_of_gravity = Decimal(1.65) * Decimal(0.000125) ** Decimal((gravity_of_boil - 1))
        
        hop_boil_time_in_minutes = minutes + Decimal(seconds / 60)
        function_of_time = (1 - e ** Decimal((Decimal(-0.04) * Decimal(hop_boil_time_in_minutes)))) / Decimal(4.15)
        
        Utilization = Decimal(function_of_gravity) * Decimal(function_of_time)
        
        Weight = hop_list[minutes, seconds][1]
        Alpha_Acids = hop_list[minutes, seconds][2]
        
        AAU = Decimal(Weight) * Decimal(Alpha_Acids) * Utilization
        # add AAU for all hops in recipe
        Total_AAU += AAU
    
    IBU = Decimal(Total_AAU) * 75 / Decimal(final_volume_desired)
    
    print(' Your {} gallon recipe wil have an IBU value of: {}'.format(final_volume_desired, round(IBU, 2)))
    
#where:
#f(G) = 1.65 x 0.000125^(Gb - 1)
#f(T) = [1 - e^(-0.04 x T)] / 4.15
#AAU = Weight (oz) x % Alpha Acids (whole number)
#IBU = AAU x U x 75 / Vrecipe

#sample_boil_profile format = {(minutes, seconds): ('Name', ounces, Alpha_acids)}
sample_boil_profile = {(59,50): ('Warrior', 1, 15), (59,40): ('Amarillo', 1.5, 10), (00,15): ('Cascade', 3, 6)}
sample_IPA_boil_gravity = 1.051
sample_final_volume = 3

IBU_calculator(sample_IPA_boil_gravity, sample_boil_profile, sample_final_volume)

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:36:39 2020

@author: ryanwebster
"""

