from resources import print_board, winner_check

board = {'1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9'}
winner = False
player = 2


for n in range(9):
    if player % 2 ==0:
        letter = "X"
    else: letter = "O"
    print_board(board)
    while winner == False:
        move = input("It's player " + letter + "\'s turn. What space do you want to choose?")
        if board[str(move)] != 'X' and board[str(move)] != 'O':
            board[move] = letter
            break
        else:
            print("That space is already filled, choose another space.")
            continue
    player +=1
    if winner_check(board) == True:
        print("Game Over")
        break
print_board(board)


