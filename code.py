board = {'1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9'}
playing = True

def print_board(board):
    print(board['1'] + " | " + board['2'] + " | " + board['3'])
    print("- - - - - ")
    print(board['4'] + " | " + board['5'] + " | " + board['6'])
    print("- - - - - ")
    print(board['7'] + " | " + board['8'] + " | " + board['9'])

def winner():
    if board['1'] == board['2'] == board['3']:
        playing = False
    if board['4'] == board['5'] == board['6']:
        playing = False
    if board['7'] == board['8'] == board['9']:
        playing = False
    if board['1'] == board['4'] == board['7']:
        playing = False
    if board['2'] == board['5'] == board['8']:
        playing = False
    if board['3'] == board['6'] == board['9']:
        playing = False
    if board['1'] == board['5'] == board['9']:
        playing = False
    if board['3'] == board['5'] == board['7']:
        playing = False

player = 2

while playing:
    for n in range(9):
        if player % 2 ==0:
            letter = "X"
        else: letter = "O"
        print_board(board)
        while True:
            move = input("It's player " + letter + "\'s turn. What space do you want to choose?")
            if board[str(move)] != 'X' and board[str(move)] != 'O':
                board[move] = letter
                print(board)
                break
            else:
                print("That space is already filled, choose another space.")
                continue
        player +=1
    print_board(board)
    winner(check)

