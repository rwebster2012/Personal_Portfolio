#Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.


def snail(array):
    if len(array) == 1:
        new_list = array
    else:
        new_list = []
    def add_top_of_array(array):
        for i in range(len(array[0])):
            new_list.append(array[0][i])
        del array[0]
        return new_list, array
    
    def add_last_elements(array):
        n = len(array)
        for i in range(n):
            new_list.append(array[i][-1])
        for i in range(n):    
            del array[i][-1]
        return new_list, array
    def add_bottum_elements_in_reverse(array):
        for i in range(len(array[-1])):
            new_list.append(array[-1][-1 - i])
        del array[-1]
        return new_list, array
    def add_first_elements_in_reverse(array):
        for i in range(len(array)):
            new_list.append(array[-1 - i][0])
            del array[-1 - i][0]
        return new_list, array
    for i in range(len(array) - 1):
        try:
            add_top_of_array(array)
            add_last_elements(array)
            add_bottum_elements_in_reverse(array)
            add_first_elements_in_reverse(array)
        except:
            try:
                add_top_of_array(array)
            except:
                try:
                    add_last_elements(array)
                    add_bottum_elements_in_reverse(array)
                    add_first_elements_in_reverse(array)
                except:
                    return new_list
    return new_list


print(snail(array))
