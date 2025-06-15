import math

X = "X"
O = "O"
EMPTY = None  

WIN_CONDITIONS = [
    # Linhas
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    # Colunas
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    # Diagonais
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
]

def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    if x_count == o_count:
        return X
    else:
        return O

def actions(board):
    possible_actions = set()
    for r in range(3):
        for c in range(3):
            if board[r][c] == EMPTY:
                possible_actions.add((r, c))
    return possible_actions

def result(board, action):
    if action not in actions(board):
        raise Exception("Ação inválida")

    player_to_move = player(board)
    new_board = [row[:] for row in board]  
    r, c = action
    new_board[r][c] = player_to_move
    return new_board

def winner(board):
    for condition in WIN_CONDITIONS:
        (r1, c1), (r2, c2), (r3, c3) = condition
        if (board[r1][c1] == board[r2][c2] == board[r3][c3]) and board[r1][c1] is not EMPTY:
            return board[r1][c1]
    return None

def terminal(board):
    if winner(board) is not None:
        return True
    for r in range(3):
        for c in range(3):
            if board[r][c] == EMPTY:
                return False  
    return True 

def utility(board):
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:  # Empate
        return 0
    
def minimax(board):
    if terminal(board):
        return None 

    current_player = player(board)

    if current_player == X:
        best_value = -math.inf
        best_action = None
        for action in actions(board):
            v = min_value(result(board, action))
            if v > best_value:
                best_value = v
                best_action = action
        return best_action
    else:
        best_value = math.inf
        best_action = None
        for action in actions(board):
            v = max_value(result(board, action))
            if v < best_value:
                best_value = v
                best_action = action
        return best_action

def max_value(board):
    if terminal(board):
        return utility(board)

    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)

    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def map_input_to_coords(user_input):
    mapping = {
        '1': (0, 0), '2': (0, 1), '3': (0, 2),
        '4': (1, 0), '5': (1, 1), '6': (1, 2),
        '7': (2, 0), '8': (2, 1), '9': (2, 2)
    }
    return mapping.get(user_input)

def print_board(board):
    print("-------------")
    for r in range(3):
        print(f"| {board[r][0] if board[r][0] is not EMPTY else ' '} | {board[r][1] if board[r][1] is not EMPTY else ' '} | {board[r][2] if board[r][2] is not EMPTY else ' '} |")
        print("-------------")