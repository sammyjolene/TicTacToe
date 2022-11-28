board = {'1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9'}

def print_board(board):
    print(board['1'] + " | " + board['2'] + " | " + board['3'])
    print("- - - - - ")
    print(board['4'] + " | " + board['5'] + " | " + board['6'])
    print("- - - - - ")
    print(board['7'] + " | " + board['8'] + " | " + board['9'])

winner = False

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
    
