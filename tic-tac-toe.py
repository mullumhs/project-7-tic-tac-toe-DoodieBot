
# create board
def initialise_board():
    board=[]
    for i in range(3):
        board.append(["-","-","-",])
    return board
        
def print_board(board):
    print (" a b c")
    for i, row in enumerate(board):
        print (f"{i+1}", end='|')
        for col in row:
            print(col, end='|')
        print()

def is_draw():
    if player_count == 10:
        print("draw")
        return True
    else:
        return False

def horizontal_check(board):
    for row in range(3):
        if board[row][0]==board[row][1]==board[row][2] !="-":
            print("u win !!!")
            break

def vertical_check(board):
    for row in range(3):
        if board[col][0]==board[col][1]==board[col][2] !="-":
            print("u win !!!")
            break

def diagonal_check(board):
    if board[0][0]==board[1][1]==board[2][2] !="-":
        print("u win !!!")
        return(True)
    if board[0][2]==board[1][1]==board[2][0]!="-": 
        print("u win !!!")
        return(True)       
    
 
board=initialise_board()
# player tokens
print_board(board)
player_count = 1
while True: 
    token = 'X'
    if player_count % 2 == 0:
        token = 'O'

    # place token
    col=int(input("Column: "))
    col=col-1
    if col <= 3 and col >=0 :  
    
        row=(input("Row: ").lower())
        if row=='a':
            row = 0
            row = int(row)
    
        if row=='b':
            row = 1
            row = int(row)

        if row=='c':
            row = 2
            row = int(row)
        
    

        if row <= 3 and row >=0 :  
            if board[col][row] == "-":
            
                board[col][row] = token
                player_count+=1
               
        else :      
            print ("error try again, number was too big")
    else:
         print ("error try again, number was too big")
    print_board(board)

    if is_draw():
        board=initialise_board()
        player_count = 1

    diagonal_check(board)

    vertical_check(board)

    horizontal_check(board)  