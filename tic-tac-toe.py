
    # Your code goes here


board = []
def initialise_board():
    for i in range(3):
     i =+ 1
     board.append([i,"-","-","-",])
        

def print_board():
    print (" a b e")
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
