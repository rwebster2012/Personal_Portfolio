#depth first search


from __future__ import print_function
import time
start_time = time.time()

puzzle = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
]
puzzle2 = [[9, 0, 0, 0, 8, 0, 0, 0, 1],
 [0, 0, 0, 4, 0, 6, 0, 0, 0],
 [0, 0, 5, 0, 7, 0, 3, 0, 0],
 [0, 6, 0, 0, 0, 0, 0, 4, 0],
 [4, 0, 1, 0, 6, 0, 5, 0, 8],
 [0, 9, 0, 0, 0, 0, 0, 2, 0],
 [0, 0, 7, 0, 3, 0, 2, 0, 0],
 [0, 0, 0, 7, 0, 5, 0, 0, 0],
 [1, 0, 0, 0, 4, 0, 0, 0, 7]]


# below function used to print out the board nicely for easy viewing

def print_board(board):
    for i in range(len(board[0])):
        #splitting board by horizontal groups of 3
        if i % 3 == 0 and i != 0:
            print(' + + + + + + +  ')
        
        #splitting board by vertical groups of 3
        for j in range(len(board[0])):
            if j % 3 == 0 and j!= 0:
                print(' | ', end ="")
            
            # printing last element in row
            if j == 8:
                print(board[i][j])
            
            #prints remaining elements in row    
            else:
                print(str(board[i][j]) + '', end="")
                


def find_empty(board):
    #iterate through rows in board
    for i in range(len(board)):
        #iterate through values in each row
        for j in range(len(board[0])):
            #if value is unknown(marked as 0) return the coordinates as a tuple
            if board[i][j] == 0:
                return(i, j)
    return None

def validate_number(board, number, position):
    #imputing the puzzle board, a number in range(10) and the poisition found in find_empty
    
    #check row
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False
    
    #check column
    for i in range(len(board[0])):
        if board[i][position[1]] == number and position[0] != i:
            return False
    
    #check 3x3 box
    
    #using integer division to define ranges to iterate through for each box
    #horizontal_box determines what set of horizontal boxes we are in and vertical_box does the same for vertical boxes
    horizontal_box = position[1] // 3 
    vertical_box = position[0] // 3
    
    #now use the horizontal and vertical box to find the range to check through for the 3x3 box
    
    for i in range(vertical_box * 3, vertical_box * 3 + 3):        
        for j in range(horizontal_box * 3, horizontal_box * 3 + 3):            
            if board[i][j] == number and (i, j) != position:
                return False
    return True

def solve(board):
    
    #makeing the find umpty function easier to write below
    find = find_empty(board)
    
    #makeing sure that when the board is full the function is done
    if not find:
        return True
    
    #if board is not full and there is an unknown we solve below
    else:
        #taking tuple returned from find and redefining the variables
        row, col = find
    
    #testing each number in the determined position
    for i in range(1,10):
        
        #call the validate_number funtion to test if the number works and if it does change the value in the puzzle
        if validate_number(board, i, (row, col)):
            board[row][col] = i
            
            #call the solve function withing for recursion so the process czan reset
            if solve(board):
                return True
            
            #if the number doesnt work this will backtrack and try a new solution
            board[row][col] = 0
    
    #returning false assures recursion        
    return False

print_board(puzzle2)
print()
solve(puzzle2)
print_board(puzzle2)
print("--- %s miliseconds ---" % ((time.time() - start_time) * 1000))  
    
    
    
    
    
    
    
    
    
    