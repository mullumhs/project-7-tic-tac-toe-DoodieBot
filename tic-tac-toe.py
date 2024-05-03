
    # Your code goes here


board = []
def initialise_board():
    for i in range(3):
     board.append(["-","-","-",])
        

def print_board():
    print ("  a b c")
    for i, row in enumerate(board):
        print (f"{i+1}", end='|')
        for col in row:
            print(col, end='|')
        print()

initialise_board()
# player tokens
print_board()
player_count = 1
while True: 
    token = 'X'
    if player_count % 2 == 0:
        token = 'O'

    # place token
    col=int(input("Column: "))
    row=int(input("Row: "))

    if col < 3 and row < 3:
        if board[col][row] == "-":
        
            board[col][row] = token
            player_count+=1
    else :      
        print ("error try again")

    print_board()


# is win?