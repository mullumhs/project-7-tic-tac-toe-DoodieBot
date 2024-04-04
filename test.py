board = []
def initialise_board():
    for i in range(6):
        board.append(["-","-","-","-","-","-","-",])
        

def print_board():
    print (" 1 2 3 4 5 6 7")
    for row in board:
        print ("", end='|')
        for col in row:
            print(col, end='|')
        print()

initialise_board()
print_board()
player_count = 1
while True: 
    token = 'X'
    if player_count % 2 == 0:
        token = 'O'
#validate that input.
    choice = input("Input colum number between 1 and 7: ")
    while True:
        if choice.isdigit():
            choice = int(choice)
            if choice>=1 and choice <=7:
                break
            else: 
                choice = input("Input colum number between 1 and 7: ")
        else: 
            choice = input("Input colum number between 1 and 7: ")
    choice -= 1
    for i in range(5, -1, -1):
        if board[i][choice] == '-':
            board[i][choice] = token   
            player_count += 1
            break
        
    print_board()
