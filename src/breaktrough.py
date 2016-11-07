def new_board(n, p):
    """int -> int -> list (list int)

    Initialize a fresh new board of n rows and p columns where n > 4
    (adjusted if too low) and returns it.
    """

    # Raising number of rows if it does not match the rules
    if not n > 4:
        n = 5

    empty_board = [[0 for x in range(p)] for y in range(n)]
    first_player_pawns = [[1 for x in range(p)] for y in range(2)]
    second_player_pawns = [[2 for x in range(p)] for y in range(2)]

    return first_player_pawns + empty_board[2:-2] + second_player_pawns

def display_board(board, n, p):
    """list (list int) -> int -> int -> IO

    Iterate the board and display each of its values replaced with
    characters to make it prettier to the user.
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

    Let the designated player choose a valid pawn to move and returns it.
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

    Given coordinates, I will check if there is a pawn there belonging to a
    specified player and if it is able to move.
    """

    # Return true if all rules are respected
    return coordinates_within_board(n, p, x, y) \
           and pawn_exist(board, x, y) \
           and pawn_belong_to_player(board, player, x, y) \
           and pawn_can_move(board, player, x, y)

def coordinates_within_board(board_height, board_width, x, y):
    """int -> int -> int -> int -> bool

    Are the given coordinates inside the board ?
    """

    return x < board_width \
           and y < board_height \
           and x >= 0 \
           and y >= 0

def pawn_exist(board, x, y):
    """list (list int) -> int -> int -> bool

    Is there a pawn at these coordinates ?
    """

    return board[y][x] is not 0

def pawn_belong_to_player(board, player, x, y):
    """list (list int) -> int -> int -> int -> bool

    Does that pawn belongs to the player ?
    """

    return board[y][x] is player

def pawn_can_move(board, player, x, y):
    """list (list int) -> int -> int -> int -> bool

    Is the pawn able to move ?
    """

    facing_squares = pawn_facing_squares(board, player, x, y)
    opponent = 1 if player is 2 else 1

    # Return true if at least one of the square facing the pawn is nor a friend
    # nor outside of the board
    return opponent in facing_squares \
           or 0 in facing_squares

def where(board, n, p, player, i, j):
    """list (list int) -> int -> int -> int -> int -> int -> int

    Ask player where he wants to move the pawn located at i and j.
    High level implementation.
    """

    print("Where do you want to move this pawn ?")
    return where_(board, player, i, j)


def where_(board, player, x, y):
    """list (list int) -> int -> int -> int -> int

    Let player choose to which column he wants to move the pawn present at
    x and y coordinates and return this number if it is valid,
    otherwise re-ask him by re-calling the function.
    Low level implementation of where function.
    """

    available_moves = pawn_available_moves(board, player, x, y)
    choice = int(input("Column number (" + str(available_moves)[1:-1] + "): "))

    if choice in available_moves:
        return choice
    else:
        print("You cannot move it there, please retry.")
        return where_(board, player, x, y)

def pawn_available_moves(board, player, x, y):
    """list (list int) -> int -> int -> int -> list int

    After computing the facing squares of the pawn in x and y,
    return the filtered list of the squares where, according to the rules, this
    pawn can move.
    """

    return [
        square
        for square in pawn_facing_squares(board, player, x, y)
        if square is not player
    ]

def move_direction(player):
    """int -> int

    Return the direction that player's pawns should be moving.
    """

    return 1 if player is 1 else -1

def pawn_facing_squares(board, player, x, y):
    """list (list int) -> int -> int -> int -> list int

    Return the squares that faces a pawn located at x and y. The out of border
    squares are automatically discarded.
    """

    return board[y + move_direction(player)][x-1:x+1]
