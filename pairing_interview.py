board = {'1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9'}
winner = False

#Print the board in Tic Tac Toe grid
def print_board(board):
    print(board['1'] + " | " + board['2'] + " | " + board['3'])
    print("- - - - - ")
    print(board['4'] + " | " + board['5'] + " | " + board['6'])
    print("- - - - - ")
    print(board['7'] + " | " + board['8'] + " | " + board['9'])

#Function to check if there is a winner
def winner_check(board):
    if board['1'] == board['2'] == board['3']:
        won = str(board['1']) 
        print('Player ' + won + ' is the winner!')
        return True
    elif board['4'] == board['5'] == board['6']:
        won = str(board['4'])
        print('Player ' + won + ' is the winner!')
        return True
    elif board['7'] == board['8'] == board['9']:
        won = str(board['7'])
        print('Player ' + won + ' is the winner!')
        return True
    elif board['1'] == board['4'] == board['7']:
        won = str(board['1'])
        print('Player ' + won + ' is the winner!')
        return True
    elif board['2'] == board['5'] == board['8']:
        won = str(board['5'])
        print('Player ' + won + ' is the winner!')
        return True
    elif board['3'] == board['6'] == board['9']:
        won = str(board['3'])
        print('Player ' + won + ' is the winner!')
        return True
    elif board['1'] == board['5'] == board['9']:
        won = str(board['1'])
        print('Player ' + won + ' is the winner!')
        return True
    elif board['3'] == board['5'] == board['7']:
        won = str(board['3'])
        print('Player ' + won + ' is the winner!')
        return True
    else: return False
    
#To start and will increment by 1 each time the program loops
player = 2

#Game play code
for n in range(9):
    if player % 2 ==0:
      letter = "X"
    else: 
      letter = "O"
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