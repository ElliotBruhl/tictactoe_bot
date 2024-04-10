current_pos = [" " for i in range(9)]

def print_board(board):
    print(" ",board[0]," | ",board[1]," | ",board[2])
    print("  -------------")
    print(" ",board[3]," | ",board[4]," | ",board[5])
    print("  -------------")
    print(" ",board[6]," | ",board[7]," | ",board[8])

def move():
    move = int(input("Enter your move coordinate: "))
    while (move < 1 or move > 9 or current_pos[move-1] != " "):
        move = int(input("You can't move there. Try again: "))
    if len(get_open_moves(current_pos))%2 == 1: current_pos[move-1] = "X"
    else: current_pos[move-1] = "O"

def get_open_moves(board):
    empty_squares = []
    for i in range(len(board)):
        if board[i] == " ":
            empty_squares.append(i)
    return empty_squares

def win_check(board): #return 0 for tie, 1 for X win, -1 for O win, and False for no win/draw
    #draw
    if len(get_open_moves(board)) == 0:
        return 0
    #rows
    for i in range(0,9,3):
        if board[i] == " " or board[i+1] == " " or board[i+2] == " ":
            pass
        elif board[i] == board[i+1] and board[i] == board[i+2]:
            return 1 if board[i] == "X" else -1
    #cols
    for i in range(3):
        if board[i] == " " or board[i+3] == " " or board[i+6] == " ":
            pass
        elif board[i] == board[i+3] and board[i] == board[i+6]:
            return 1 if board[i] == "X" else -1
    #diagonals
    if board[0] == " " or board[4] == " " or board[8] == " ":
        pass
    elif board[0] == board[4] and board[0] == board[8]:
        return 1 if board[0] == "X" else -1
    if board[6] == " " or board[4] == " " or board[2] == " ":
        pass
    elif board[6] == board[4] and board[6] == board[2]:
        return 1 if board[6] == "X" else -1
    #play on
    return False

def run_game():
    print("Board cordinates:")
    print_board([i+1 for i in range(9)])
    gamestate = False #more efficent to call win_check once per interation
    while (gamestate is False): #gotta be careful with 0==false/1==true
        print(("X's" if len(get_open_moves(current_pos))%2 == 1 else "O's"),"turn.")
        print_board(current_pos)
        move()
        gamestate = win_check(current_pos)
    print_board(current_pos)
    if gamestate == 1: print("X's win!")
    elif gamestate == -1: print("O's win!")
    else: print("Its a draw!")

def computer_move(board):
    tree = Node(board)
    return find_best(tree)

def find_best(node):
    if node.value() == 0: return 0
    elif node.value() == 1: return 1
    elif node.value() == -1: return -1

    if len(get_open_moves(node.value()))%2 == 1: #X's turn, get max
        best_move_X = -2
        for i in node.children():
            test_move = find_best(i)
            best_move_X = max(best_move_X, test_move)
        return best_move_X
    else: #O's turn get min
        best_move_O = 2
        for i in node.children():
            test_move = find_best(i)
            best_move_O = min(best_move_O, test_move)
        return best_move_O

class Node():
    def __init__(self, value):
        self.value = value
        children = make_children(value)

        def make_children(value):
            new_children = []
            for i in get_open_moves(value):
                temp = value.copy()
                temp[i] = "X" if len(get_open_moves(value)) % 2 == 1 else "O"
                result = win_check(temp)
                if result is not False:
                    temp = result
                    new_children.append(temp)
                else:
                    new_children.append(temp)
                    node = Node(temp)
            return new_children  

run_game()
