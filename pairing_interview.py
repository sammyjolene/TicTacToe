import random
board = {'1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9'}
xboard = {'1':'X', '2':'O', '3':'3', '4':'X', '5':'O', '6':'6', '7':'X', '8':'8', '9':'9'}
Oboard = {'1':'X', '2':'O', '3':'3', '4':'X', '5':'O', '6':'6', '7':'O', '8':'O', '9':'9'}
tie = {'1':'O', '2':'X', '3':'X', '4':'X', '5':'O', '6':'O', '7':'O', '8':'X', '9':'X'}
winner = False

#Print the board in Tic Tac Toe grid
def print_board(board):
    print(board['1'] + " | " + board['2'] + " | " + board['3'])
    print("- - - - - ")
    print(board['4'] + " | " + board['5'] + " | " + board['6'])
    print("- - - - - ")
    print(board['7'] + " | " + board['8'] + " | " + board['9'])

#Available Moves Check

def move_options(board):
    available_moves = []
    for key in board:
        if board[key] != "X" and board[key] != "O":
            available_moves.append(key)
    return available_moves

#print(move_options(xboard))
#print(move_options(Oboard))

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
    #my turn
    while winner == False:
        if letter == "X":
            move = input("It's player " + letter + "\'s turn. What space do you want to choose?")
            if board[str(move)] != 'X' and board[str(move)] != 'O':
                board[move] = letter
                break
            else:
                print("That space is already filled, choose another space.")
                continue
        else:
            available_moves = move_options(board)
            move = random.choice(available_moves)
            board[move] = letter
            break
    #computer turn
    player +=1
    if winner_check(board) == True:
        print("Game Over")
        break
print_board(board)