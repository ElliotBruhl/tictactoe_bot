def print_board(board):
    print(" ",board[0]," | ",board[1]," | ",board[2])
    print("  -------------")
    print(" ",board[3]," | ",board[4]," | ",board[5])
    print("  -------------")
    print(" ",board[6]," | ",board[7]," | ",board[8])

def get_open_moves(board):
    empty_squares = []
    for i in range(len(board)):
        if board[i] == " ":
            empty_squares.append(i)
    return empty_squares

def win_check(board): #return 0 for tie, 1 for X win, -1 for O win, and False for no win/draw
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
    #draw
    if len(get_open_moves(board)) == 0:
        return 0
    #play on
    return None

def run_game(board):
    print("Board cordinates:")
    print_board([i+1 for i in range(9)])
    print()
    gamestate = None
    while (gamestate is None):
        print_board(board)
        print(("X's" if len(get_open_moves(board))%2 == 1 else "O's"),"turn",end=". ")
        if len(get_open_moves(board))%2 == 1: #for human to go first
            print("(human)")
            board = human_move(board)
        else:
            print("(computer)")
            board = computer_move(board)
        """if len(get_open_moves(board))%2 == 1: #for computer to go first
            print("(computer)")
            board = computer_move(board)
        else:
            print("(human)")
            board = human_move(board)"""
        gamestate = win_check(board)
    print_board(board)
    if gamestate == 1: print("X's win!")
    elif gamestate == -1: print("O's win!")
    else: print("Its a draw!")

def computer_move(board):
    best_node = find_best(Node(board, None, None))
    while best_node.parent.parent is not None: #best move finds best terminal node so this converts to return best next node
        best_node = best_node.parent
    return best_node.value

def human_move(board):
    move = int(input("Enter your move coordinate: "))
    while (move < 1 or move > 9 or board[move-1] != " "):
        move = int(input("You can't move there. Try again: "))
    if len(get_open_moves(board))%2 == 1: board[move-1] = "X"
    else: board[move-1] = "O"
    return board

def find_best(node): #minimax algorithm
    if node.evaluation is not None: return node

    if len(get_open_moves(node.value))%2 == 1: #X's turn, get max eval
        best_eval_X = -2
        for i in node.children:
            test_node = find_best(i)
            if test_node.evaluation > best_eval_X:
                best_eval_X = test_node.evaluation
                best_node_X = test_node
        return best_node_X
    else: #O's turn get min eval
        best_eval_O = 2
        for i in node.children:
            test_node = find_best(i)
            if test_node.evaluation < best_eval_O:
                best_eval_O = test_node.evaluation
                best_node_O = test_node
        return best_node_O

class Node():
    def __init__(self, value, evaluation, parent):
        self.value = value
        self.parent = parent
        self.evaluation = evaluation
        if evaluation is None: #if not a terminal node, create children recursively
            self.children = self.make_children(value)

    def make_children(self, value):
        new_children = []
        for i in get_open_moves(value):
            temp = value.copy()
            temp[i] = "X" if len(get_open_moves(value)) % 2 == 1 else "O"
            result = win_check(temp)
            new_children.append(Node(temp, result, self))
        return new_children

run_game([" " for i in range(9)])
