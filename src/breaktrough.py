"""The Breaktrough game."""

import sys

def new_board(n, p):
    """int -> int -> list (list int)

    Initialize a fresh new board of n rows and p columns and returns it.
    """

    empty_board = [[0 for x in range(p)] for y in range(n)]
    first_player_pawns = [[1 for x in range(p)] for y in range(2)]
    second_player_pawns = [[2 for x in range(p)] for y in range(2)]

    return first_player_pawns + empty_board[2:-2] + second_player_pawns

def display_board(board, n, p):
    """list (list int) -> int -> int -> IO

    Iterate the board and display each of its values as characters to make it
    prettier to the user.
    """

    for y in board:
        for x in y:
            if x == 0:
                print('.', end='')
            elif x == 1:
                print('x', end='')
            else:
                print('o', end='')
        # Do not forget to carriage return !
        print()

def select_pawn(board, n, p, player):
    """list (list int) -> int -> int -> int -> int, int

    Let the player choose a pawn that is able to move and returns it.
    """

    print("Choose the pawn you want to move.")
    x = int(input("Its x coordinates: "))
    y = int(input("Its y coordinates: "))

    if pawn_valid(board, n, p, player, x, y):
        return x, y
    else:
        print("These coordinates are invalid, please retry.")
        return select_pawn(board, n, p, player)

def pawn_valid(board, n, p, player, x, y):
    """list (list int) -> int -> int > int -> int -> int -> bool

    Given coordinates, I will check if there is a pawn there belonging to
    player and if it is able to move.
    """

    # Return true if all rules are respected
    return coordinates_within_board(n, p, x, y) \
           and pawn_exist(board, x, y) \
           and pawn_belong_to_player(board, player, x, y) \
           and pawn_can_move(board, player, x, y)

def coordinates_within_board(board_height, board_width, x, y):
    """int -> int -> int -> int -> bool

    Are the given coordinates inside the board?
    """

    return x < board_width \
           and y < board_height \
           and x >= 0 \
           and y >= 0

def pawn_exist(board, x, y):
    """list (list int) -> int -> int -> bool

    Is there a pawn at these coordinates?
    """

    return board[y][x] is not 0

def pawn_belong_to_player(board, player, x, y):
    """list (list int) -> int -> int -> int -> bool

    Does that pawn belong to the player?
    """

    return board[y][x] is player

def pawn_can_move(board, player, x, y):
    """list (list int) -> int -> int -> int -> bool

    Is the pawn able to move?
    """

    facing_squares = pawn_facing_squares(board, player, x, y)
    opponent = 1 if player is 2 else 1

    # Return true if at least one of the square facing the pawn is not a friend
    # nor outside of the board
    return opponent in facing_squares \
           or 0 in facing_squares

def where(board, n, p, player, i, j):
    """list (list int) -> int -> int -> int -> int -> int -> int

    Ask player where he wants to move the pawn located at i and j.
    High level implementation.
    """

    print("Where do you want to move this pawn ?")
    return where_(board, p, player, i, j)


def where_(board, board_width, player, x, y):
    """list (list int) -> int -> int -> int -> int -> int

    Let player choose to which column he wants to move the pawn present at
    x and y coordinates and return this number if it is valid,
    otherwise re-ask him by re-calling the function.
    Low level implementation of where function.
    """

    available_moves = pawn_available_moves(board, board_width, player, x, y)
    choice = int(input("Column number (" + str(available_moves)[1:-1] + "): "))

    if choice in available_moves:
        return choice
    else:
        print("You cannot move it there, please retry.")
        return where_(board, board_width, player, x, y)

def pawn_available_moves(board, board_width, player, x, y):
    """list (list int) -> int -> int -> int -> int -> list int

    After computing the squares in front of the pawn in x and y,
    return the filtered list of the columns numbers where, according to the
    rules, this pawn can move.
    """

    facing_columns = pawn_facing_columns(board_width, x)
    facing_squares = pawn_facing_squares(board, player, x, y)

    return [
        square[0]
        for square in zip(facing_columns, facing_squares)
        if square[1] is not player
    ]

def move_direction(player):
    """int -> int

    Return the direction that player's pawns should be moving.
    """

    return 1 if player is 1 else -1

def pawn_facing_squares(board, player, x, y):
    """list (list int) -> int -> int -> int -> list int

    Return the squares that faces a pawn located at x and y. The out of border
    squares are discarded.
    """

    return board[y + move_direction(player)][(x-1 if x-1 > 0 else 0):x+2]

def pawn_facing_columns(board_width, x):
    """int -> int -> list int

    Return columns number that faces a pawn located at x and y.
    """

    return [
        column
        for column in [x-1, x, x+1]
        if column >= 0 and column < board_width
    ]

def breaktrough(n, p):
    """int -> int -> IO

    This is the main procedure of the game.
    """

    # Raising number of rows if it does not match the rules
    if not n > 4:
        n = 5

    # Greet the player(s)
    greet()

    # Now, initiate the first turn and the subsequent ones
    winner = turn(new_board(n, p), n, p, 1) # 1 because whites start first

    # Congratulate the winner
    congrats(winner)

    # Terminate the process
    exit(0)

def greet():
    """IO -> IO

    Welcome the player(s).
    """

    print("Welcome! Ready to play breaktrough? Go!")

def turn(board, n, p, player):
    """list (list int) -> int -> int -> int -> int

    Resolve player's turn.
    """

    print("This is player " + str(player) + "'s turn.")
    display_board(board, n, p)

    x, y = select_pawn(board, n, p, player)
    selected_column_to_move_to = where(board, n, p, player, x, y)
    move_pawn(board, x, y, selected_column_to_move_to)

    if someone_won(board):
        # Display board one last time to show its final state
        display_board(board, n, p)
        return player
    else:
        return turn(board, n, p, 3-player)

def move_pawn(board, x, y, dest_column):
    """list (list int) -> int -> int -> int -> IO

    Move the pawn located at x and y to dest_column in the direction it faces.
    Lists love side-effects.
    """

    pawn = board[y][x]
    board[y + move_direction(pawn)][dest_column] = pawn
    board[y][x] = 0 # Empty the square where the pawn was located before moving

def someone_won(board):
    """list (list int) -> bool

    Check if, according to the rules, one of the players won.
    """

    return (not still_has_pawns(board, 1)
            or not still_has_pawns(board, 2)
            or 2 in board[0] # Has a black pawn reached the white starting line?
            or 1 in board[-1]) # Has a white pawn reached the black starting
                               # line?

def still_has_pawns(board, player):
    """list (list int) -> int -> bool

    Does player still have at least one pawn?
    """

    return player in flatten(board)

def flatten(l):
    """list (list *) -> list

    Given a two dimensional list, return a one dimensional list being the
    concatenation of all the element inside the original list.
    """

    return [x for y in l for x in y]

def congrats(player):
    """int -> IO

    Felicitate player for winning the game.
    """

    print("Congratulations player " + str(player) + "! You have won this game!")

if __name__ == "__main__":
    breaktrough(int(sys.argv[1]), int(sys.argv[2]))
