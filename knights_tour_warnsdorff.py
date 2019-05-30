import numpy as np

n, m = 8, 8 #board size

#Potential move 1 - Go 2 squares up and 1 to the right
pm1 = [1, 2]
#Potential move 2 - Go 2 squares up and 1 to the left
pm2 = [-1, 2]
#Potential move 3 - Go 1 squares up and 2 to the right
pm3 = [2, 1]
#Potential move 4 - Go 1 squares up and 2 to the left
pm4 = [-2, 1]
#Potential move 5 - Go 1 squares down and 2 to the right
pm5 = [2, -1]
#Potential move 6 - Go 1 squares down and 2 to the left
pm6 = [-2,-1]
#Potential move 7 - Go 2 squares down and 1 to the right
pm7 = [1, -2]
#Potential move 8 - Go 2 squares down and 1 to the left
pm8 = [-1, -2]

#Put them all in an array so we can randomly pick one or iterate through them all
array_of_moves = [pm1, pm2, pm3, pm4, pm5, pm6, pm7, pm8]

def setup_board(n, m): #setup n * m board
    board = np.zeros((n, m), dtype=int)
    return board

def in_bounds(x, y): #checks if the knight is on the board
    return (x >= 0 and y >= 0) and (x < n and y < m)

def is_empty(board, x, y, move): #check if a move is valid
    x_step, y_step = move
    return in_bounds(x+x_step, y+y_step) and board[y+y_step][x+x_step] == 0

def degree(board, x, y): #get the degree of a position on the board
    return len([move for move in array_of_moves if is_empty(board, x, y, move)])

def next_step(board, x, y): #choose next best step using Warnsdorff algorithm
    degree_array = [[move, degree(board, x + move[0], y + move[1])] for move in array_of_moves if is_empty(board, x, y, move)] #array that stores posible next moves along with their degree
    min_degree = 9 #note: highest possible degree is 8

    for item in degree_array:
        if item[1] < min_degree:
            min_degree = item[1]

    next_best_moves = [item[0] for item in degree_array if item[1] == min_degree] #array of next best moves (i.e those that have the fewest possible places to go to)

    return next_best_moves #note if next_best_moves is empty that implies there is no more places for the knight to go!

def is_closed_loop(board, x, y, init_x, init_y): #checks if the knight is one move from the initial position - this will be used to check for closed tours
    for move in array_of_moves:
        x_step, y_step = move
        if x + x_step == init_x and y + y_step == init_y:
            return True
    return False


def tour(n, m, init_x, init_y): #returns a tour and a boolean which indicates whether or not tour is closed

    #setup board and mark the starting position of the knight as 1
    board = setup_board(n, m)
    x = init_x
    y = init_y
    board[y][x] = 1

    for i in range(2, 65):
        moves = next_step(board, x, y) #find next best moves according to the Warnsdorff criterion
        #if no more places for the knight to move
        if len(moves) == 0:
            print("No more moves found on this route, either backtrack or try again.")
            break
        else:
            #pick a move at random
            move = moves[np.random.randint(len(moves))]
            x_step, y_step = move
            #move knight
            x += x_step
            y += y_step
            board[y][x] = i

            #uncomment to see board develop move by move
            #print(board)
            #pause = input()

        #Check for closed loop
        closed_tour = False #assume it is not
        if i == 64: #board is complete
            if is_closed_loop(board, x, y, init_x, init_y):
                closed_tour = True

    return [board, closed_tour]


print(tour(8, 8, 3, 4)[1])

def find_closed_tour(n, m, init_x, init_y, trials):
    for i in range(trials): #try a bunch (trials amount) of tours
        trial_tour = tour(8, 8, 3, 4)
        if trial_tour[1] == True: #check if tour is a closed tour
            closed_tour = trial_tour[0]
            break
        else:
            closed_tour = None
            print(f"Could not find a closed tour in {trials} amount of trials.")
    return closed_tour

print(find_closed_tour(8, 8, 3, 4, 100))
