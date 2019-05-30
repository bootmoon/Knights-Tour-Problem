import copy as Copy

board_size = 8
chess_board = [[0 for _ in range(board_size)] for _ in range(board_size)]
moves = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
start_x = 4
start_y = 4

def next_step(board, x, y, depth):
    board[x][y] = 1
    #print_board(board) # prints the board, comment out to remove printing
    for move in moves:
        new_x = x + move[0]
        new_y = y + move[1]
        if closed_loop_found(board, new_x, new_y):
            print('closed loop found at depth ' + (depth+1))
        if out_of_bounds(new_x, new_y) or seen(board, new_x, new_y):
            continue
        new_board = Copy.deepcopy(board)
        next_step(new_board, new_x, new_y, depth + 1)


# helper functions

# returns true if the coordinates given
# are out of bounds
def out_of_bounds(x, y):
    x_bool = x >= 0 and x < board_size
    y_bool = y >= 0 and y < board_size
    return not (x_bool and y_bool)

# returns true if the coordinates given
# have been visited already
def seen(board, x, y):
    return board[x][y]

def closed_loop_found(board, x, y):
    loc_bool = x == start_x and y == start_y
    every_tile_visited_bool = all(all(item == 1 for item in items) for items in board)
    return loc_bool and every_tile_visited_bool
    
def print_board(board):
    for y in range(board_size):
        for x in range(board_size):
            print(board[x][y], end=' ')
        print()
    
next_step(chess_board, start_x, start_y, 0)