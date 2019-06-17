# Created by: Aden Rao
# Created on: June 17, 2019
# This program has two example suduku boards which it takes the soduko boards and solves them.


# Imports copy for deep copy and shallow copy which creates bindings between a target and an object (copies of objects)
import copy

# Board number 1
board = [
    ".........",
    "5.3.67...",
    "9..3421..",
    ".....4...",
    "..1...72.",
    "..2.1....",
    ".3......9",
    ".8.1..2..",
    "...75.8.6"
]

# Board number 2
# board = [
#     "6..874.1.",
#     "..9.36...",
#     "...19.8..",
#     "7946.....",
#     "..1.894..",
#     "...41..69",
#     ".7..5..9.",
#     ".539.76..",
#     "9.2.61.47"
# ]

# Defines main funtion
def main():
    # Gloabal variable
    global board
    # Partial setup for the board
    for idx,line in enumerate(board):
        board[idx] = list(line)
    # Goes to solve function
    solve()
    # Prin board function
    printBoard()
    
# Created solve function
def solve():
    # Board variable
    global board
    
    # Excutes that peice of code and goes to the fillAllObvious function
    try:
        fillAllObvious()
    except:
    # If there is an expecton run this code
        return False
    
    if isComplete():
        return True
    
# Possibilities for the board to solve
    i,j = 0,0
    for rowIdx,row in enumerate(board):
        for colIdx,col in enumerate(row):
            if col == ".":
                i,j = rowIdx, colIdx
                
    possibilities = getPossibilities(i,j)
    for value in possibilities:
        snapshot = copy.deepcopy(board)
    
        board[i][j] = value
        result = solve()
        if result == True:
            return True
        else:
            board = copy.deepcopy(snapshot)
            
    return False

def fillAllObvious():
    global board
    while True:
        somethingChanged = False
        for i in range(0,9):
            for j in range(0,9):
                possibilities = getPossibilities(i,j)
                if possibilities == False:
                    continue
                if len(possibilities) == 0:
                    raise RuntimeError("No moves left")
                if len(possibilities) == 1:
                    board[i][j] = possibilities[0]
                    somethingChanged = True
                    
        if somethingChanged == False:
            return
                
def getPossibilities(i,j):
    global board
    if board[i][j] != ".":
        return False
        
    possibilities = {str(n) for n in range(1,10)}
    #for loop used to solve the sudoku puzzle
    for val in board[i]:
        # Sets values
        possibilities -= set(val)
    #for loop used to solve the sudoku puzzle    
    for idx in range(0,9):
        # Sets board
        possibilities -= set( board[idx][j] )
        
    iStart = (i // 3) * 3
    jStart = (j // 3) * 3
    
    subboard = board[iStart:iStart+3]
    #for loop used to solve the sudoku puzzle
    for idx,row in enumerate(subboard):
        subboard[idx] = row[jStart:jStart+3]
    #for loop used to solve the sudoku puzzle
    for row in subboard:
        for col in row:
            # Sets colums
            possibilities -= set(col)

    # Possiblilites
    return list(possibilities)

# Prints board
def printBoard():
    global board
    for row in board:
        for col in row:
            print(col, end="")
        print("")
        
def isComplete():
    for row in board:
        for col in row:
            if (col == "."):
                return False
                
    return True
    
main()