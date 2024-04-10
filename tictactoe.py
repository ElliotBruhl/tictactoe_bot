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
        print(get_open_moves(current_pos))
    print_board(current_pos)
    if gamestate == 1: print("X's win!")
    elif gamestate == -1: print("O's win!")
    else: print("Its a draw!")

def generate_tree(board): #generates a tree with recursively nested lists. ex [root, [child1, [grandchild1,[g-grandchild1, g-grandchild2], gandchild2], child2,[grandchild2]]]
    tree = [board]
    children = []
    for i in get_open_moves(board):
        temp = board.copy()
        temp[i] = "X" if len(get_open_moves(board)) % 2 == 1 else "O"
        result = win_check(temp)
        if result is not False:
            temp = result
        children.append(temp)
    tree.append(children)
    return tree

def get_deep():
    pass



print(generate_tree(["X"," ","X","O","X","O","X"," ","O"]))

#run_game()