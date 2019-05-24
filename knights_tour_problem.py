import numpy as np

def open_knights_tour():

    board = np.zeros((8, 8), dtype=int)

    #place knight randomly on the board
    row = np.random.randint(8)    #the randint function returns a random integer between 0 and the number specified - 1 (inclusive)
    column = np.random.randint(8) #in this case that works out to a random integer between 0 and 7 (inclusive)
    board[row, column] = 1

    #generate random coordinates to move knight to a square
    move_to_row = np.random.randint(8)
    move_to_column = np.random.randint(8)

    #Method 1 - Calculate all potential moves for the knight, choose one at random, check if the knight has already been to that square, if not move the knight and repeat.
    #           If it has, choose another potential move and check again if the knight has been to the square. Repeat this until a square is found the knight has not been to.

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

    #Put them all in an array so we can randomly pick one of them
    array_of_moves = [pm1, pm2, pm3, pm4, pm5, pm6, pm7, pm8]


    for i in range(2, 65): #There is a maximum of 63 more moves that can be made.

        #Array that stores invalid moves
        invalid_moves = []

        for j in range(8): #We may have to run through all 8 potential moves before getting a valid one or realizing that this path does not work. EDIT: currently the for loop is set to 30 goes but there is a small chance that in those 30 goes it will not pick all 8 random moves and then terminate the path despite being able to continue going.

            #Choose a random potential move that is not in the invalid_moves array
            valid_moves = [move for move in array_of_moves if move not in invalid_moves]
            rm = valid_moves[np.random.randint(len(valid_moves))] #Choose a random move

            #Compute new theoretical position on board
            row += rm[1]
            column += rm[0]

            #Check if move goes off the board and if the square has not been moved to yet (i.e square value is 0).
            if 0 <= row <= 7 and 0 <= column <= 7:
                if board[row, column] == 0:
                    #Save the knights move and break out of the loop
                    board[row, column] = i
                    break
                else:
                    #Reset position, save move to a list and try again.
                    row -= rm[1]
                    column -= rm[0]
                    invalid_moves.append(rm)
            else:
                #Reset position, save move to a list and try again.
                row -= rm[1]
                column -= rm[0]
                invalid_moves.append(rm)

    return board


def num_of_empty_squares(board):

    count = 0

    for row in board:
        for square in row:
            if square == 0:
                count += 1

    return count

test = open_knights_tour()
print(test)
print(num_of_empty_squares(test))

found_tour = False
while(found_tour == False):
    print("Starting 1000 tours")
    for i in range(1000):
        succesful_tours = []

        test_tour = open_knights_tour()
        if num_of_empty_squares(test_tour) == 0:
            succesful_tours.append(test_tour)
            found_tour = True


for tour in succesful_tours:
    print(tour)
