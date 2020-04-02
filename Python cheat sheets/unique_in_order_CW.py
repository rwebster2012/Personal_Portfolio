#unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
#unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
#unique_in_order([1,2,2,3,3])       == [1,2,3]



def unique_in_order3(s):
    output = ''
    for i in range(len(s)):
        if i == 0:
            output = output + str(s[i])
        elif str(s[i]) == output[-1]:
            continue
        else:
            output = output + str(s[i]) 
    try:
        isinstance(s[1], int) == True
        new_list = [int(j) for j in output] 
        return new_list
    except:
        return list(output)



#print(unique_in_order3(''))
        
    
 
# different more straigthforward code from CW    
    
def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result