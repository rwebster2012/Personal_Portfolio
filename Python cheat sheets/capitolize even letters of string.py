def capitalize(s):
    new_string = ''
    new_string2 = ''
    for index in range(len(s)):
        if index % 2 != 1:
            new_string = new_string + s[index].upper()
        elif index % 2 == 1:
            new_string = new_string + s[index]
    
    for index in range(len(s)):
        if index % 2 != 1:
            new_string2 = new_string2 + s[index]
        elif index % 2 == 1:
            new_string2 = new_string2 + s[index].upper()
    final_list = [new_string, new_string2]
    print(final_list)

capitalize('lkjnsfghnsg')


"""
Created on Wed Mar 25 17:34:34 2020

@author: Deborah
"""

