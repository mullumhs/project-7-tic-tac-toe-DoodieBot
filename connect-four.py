def main():
    # MY code has gone here \|/
    board = initialiseBoard()
    displayBoard(board)
    #user input to try
    while True:
        user_input1=("pls enter the collom u want to place in.")
            
        board[3][4] = 'X'
        board[2][5] = 'O'
        displayBoard(board)
    
    
#this is board
def initialiseBoard():
    board = []
    for _ in range(6):
        row = ['-','-','-','-','-','-','-']
        board.append(row)
    return board
    
def displayBoard(board):
    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()
    print()
if __name__ == "__main__":
    main()







  