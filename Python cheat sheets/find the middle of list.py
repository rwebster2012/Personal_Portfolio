#function finds middle of a list with odd # of indicies and averagde of two middle with even indicies
def middle_element(lst):
  if len(lst) % 2 != 0:
    middle_index = ((len(lst) - 1) / 2)    
    middle_element = lst[int(middle_index)]
    return middle_element
  else:
    index1 = int((len(lst) / 2))
    index2 = int((len(lst) / 2) - 1)
    value1 = lst[index1]
    value2 = lst[index2]
    average = (value1 + value2) / 2
    return average


#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))
"""
Created on Wed Mar 25 12:48:14 2020

@author: Deborah
"""

