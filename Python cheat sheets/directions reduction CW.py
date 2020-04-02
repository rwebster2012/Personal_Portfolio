

def dirReduc(arr):
    new_list = []
    for i in range(len(arr)):
        print(arr[i])
        
        if i > 0 and arr[i] == "NORTH" and arr[i - 1] != "SOUTH":
            new_list.append(arr[i])
        elif i > 0 and arr[i] == "SOUTH" and new_list[-1] != "NORTH":
            new_list.append(arr[i])
            print('True2')
        elif i > 0 and arr[i] == "EAST" and new_list[-1] != "WEST":
            new_list.append(arr[i])
        elif i > 0 and arr[i] == "WEST" and new_list[-1] != "EAST":
            new_list.append(arr[i])
        
    return new_list


    
    
#print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
    
#a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
#test.assert_equals(dirReduc(a), ['WEST'])



def overall_reduce(arr): 
    final_list = []
    def dirReduc2(arr, n = 0):
        new_list = arr
        indici_list = []
        for i in range(n, len(new_list) - 1, 2):
            if arr[i] == "NORTH" and arr[i + 1] == "SOUTH":
                indici_list.append(i)
                indici_list.append(i + 1)
            elif arr[i] == "EAST" and arr[i + 1] == "WEST":
                indici_list.append(i)
                indici_list.append(i + 1)
            elif arr[i] == "SOUTH" and arr[i + 1] == "NORTH":
                indici_list.append(i)
                indici_list.append(i + 1)
            elif arr[i] == "WEST" and arr[i + 1] == "EAST":
                indici_list.append(i)
                indici_list.append(i + 1)
        for i in range(len(indici_list)):
            del new_list[indici_list[i] - i]
        return new_list
    new_function = dirReduc2(arr)
    for i in range(len(arr)):
        if i % 2 != 1:
            dirReduc2(new_function, 1)
        else:
            dirReduc2(new_function, 0)
            
    return dirReduc2(new_function)



        
print(overall_reduce(['NORTH', 'NORTH', 'EAST', 'NORTH', 'EAST', 'NORTH', 'NORTH', 'EAST', 'WEST']))

#print(overall_reduce(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))


#Better code wars algorithm

opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

def dirReduc(plan):
    new_plan = []
    for d in plan:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return new_plan