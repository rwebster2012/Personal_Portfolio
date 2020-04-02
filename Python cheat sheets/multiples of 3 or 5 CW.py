#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

#Note: If the number is a multiple of both 3 and 5, only count it once.

def sum_of_multiples(limit):
    multiples_of_3 = range(0,limit,3)
    multiples_of_5 = range(0,limit,5)
    non_repeated_multiples = []
    for j in multiples_of_5:
        if j not in non_repeated_multiples:
            non_repeated_multiples.append(j)
    for i in multiples_of_3:
        if i not in non_repeated_multiples:
            non_repeated_multiples.append(i)    
    final_sum = sum(non_repeated_multiples)
    return final_sum




def sum_of_multiples2(limit):
    non_repeated_multiples = range(0,limit,3)
    for j in range(0,limit,5):
        if j not in non_repeated_multiples:
            non_repeated_multiples.append(j)
    final_sum = sum(non_repeated_multiples)
    return final_sum

print(sum_of_multiples2())


#Another solution from code wars

def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)