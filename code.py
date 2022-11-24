board = {'1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9'}

def print_board(board):
    print(board['1'] + " | " + board['2'] + " | " + board['3'])
    print("- - - - - ")
    print(board['4'] + " | " + board['5'] + " | " + board['6'])
    print("- - - - - ")
    print(board['7'] + " | " + board['8'] + " | " + board['9'])


turn = 0
player = 2

for n in range(9):
    if player % 2 ==0:
        letter = "X"
    else: letter = "O"
    print_board(board)
    print("It's player " + letter + " turn. What space do you want to choose?")
    move = input()
    if board[str(move)] != "X" or "O":
        board[move] = letter
    else:
        print("That space is already filled, choose another space.")
    player +=1

