hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
for price in prices:
  total_price += price
average_price = total_price / len(prices)

print('Average Haircut Price: ' + str(average_price))

new_prices = [new - 5 for new in prices]

print()
print('New Prices: ' + str(new_prices))
print()
print()
print()

total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print('Total Revenue: ' + str(total_revenue))
average_daily_revenue = total_revenue / 7
print()
print('Average Daily Revenue ' + str(average_daily_revenue))

cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i]  < 30 ]
print()
print('Cuts under $30: ' + str(cuts_under_30))

print()
print()
print()

# another example of looping through indices and printing the original value relative to the indice
def odd_indices(lst):
  new_list = [lst[i] for i in range(len(lst)) if i % 2 == 1]
  return new_list


print(odd_indices([4, 3, 7, 10, 11, -2]))

print()
print()
print()

#Write a function named same_values() that takes two lists of numbers of equal size as parameters.

#The function should return a list of the indices where the values were equal in lst1 and lst2.

#For example, the following code should return [0, 2, 3]

#Write your function here
def same_values(lst1, lst2):
  new_list = [i for i in range(len(lst1)) if lst1[i] == lst2[i]  ]
  return new_list

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

print()
print()
print()


#Create a function named reversed_list() that takes two lists of the same size as parameters named lst1 and lst2.

#The function should return True if lst1 is the same as lst2 reversed. The function should return False otherwise.

#For example, reversed_list([1, 2, 3], [3, 2, 1]) should return True.

#Write your function here
def reversed_list(lst1, lst2):
  new_list = []
  for a in range(len(lst1)):
    new_list.append(lst1[-a - 1])
  if new_list == lst2:
    return True
  else:
    return False
  

#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))

#reated on Wed Mar 25 15:18:47 2020

#@author: Deborah
#"""

