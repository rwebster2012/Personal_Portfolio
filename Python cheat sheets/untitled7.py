def unique_in_order(s):
    output = ''
    for i in range(len(s)):
        if i == 0:
            output = output + str(s[i])
        elif s[i] == output[-1]:
            continue
        else:
            output = output + str(s[i])
    return list(output)

print(unique_in_order('ABBCcAD'))
"""
Created on Wed Mar 25 21:39:41 2020

@author: Deborah
"""

