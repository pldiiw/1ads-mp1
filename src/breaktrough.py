"""The Breaktrough game."""

from sys import argv
from typing import List, Any, Tuple
from random import choice

Row = List[int]
Board = List[Row]

def new_board(n: int, p: int) -> Board:
    """Initialize a fresh new board of n rows and p columns and returns it."""

    empty_board = [[0 for x in range(p)] for y in range(n)]
    first_player_pawns = [[1 for x in range(p)] for y in range(2)]
    second_player_pawns = [[2 for x in range(p)] for y in range(2)]

    return first_player_pawns + empty_board[2:-2] + second_player_pawns

def display(board: Board) -> None:
    """Iterate the board and display each of its values as characters to make it
    prettier to the user.
    """

    for row in board:
        for square in row:
            if square is 0:
                print('.', end=' ')
            elif square is 1:
                print('x', end=' ')
            else:
                print('o', end=' ')
        # Do not forget to carriage return !
        print()

def select_pawn(board: Board, n: int, p: int, player: int) -> Tuple[int, int]:
    """Let the player choose a pawn that is able to move and returns it."""

    print("Choose the pawn you want to move.")
    x = int(input("Its x coordinates: "))
    y = int(input("Its y coordinates: "))

    if pawn_valid(board, n, p, player, x, y):
        return x, y
    else:
        print("These coordinates are invalid, please retry.")
        return select_pawn(board, n, p, player)

def pawn_valid(board: Board, n: int, p: int, player: int, x: int,
               y: int) -> bool:
    """Given coordinates, I will check if there is a pawn there belonging to
    player and if it is able to move.
    """

    # Return true if all rules are respected
    return (coordinates_within_board(n, p, x, y) and
            pawn_exist(board, x, y) and
            pawn_belong_to_player(board, player, x, y) and
            pawn_can_move(board, n, player, x, y))

def coordinates_within_board(n: int, p: int, x: int, y: int) -> bool:
    """Are the given coordinates inside the board?"""

    return y < n and x < p and x >= 0 and y >= 0

def pawn_exist(board: Board, x: int, y: int) -> bool:
    """Is there a pawn at these coordinates?"""

    return board[y][x] is not 0

def pawn_belong_to_player(board: Board, player: int, x: int, y: int) -> bool:
    """Does that pawn belong to the player?"""

    return board[y][x] is player

def pawn_can_move(board: Board, n: int, player: int, x: int,
                  y: int) -> bool:
    """Is the pawn able to move?"""

    facing_squares = pawn_facing_squares(board, n, player, x, y)
    opponent = 3 - player

    # Return true if at least one of the square facing the pawn is not a friend
    # nor outside of the board
    return (opponent in facing_squares or
            0 in facing_squares)

def pawn_facing_squares(board: Board, n: int, player: int, x: int,
                        y: int) -> Row:
    """Return the squares that faces a pawn located at x and y. The out of
    border squares are discarded.
    """

    # If pawn is not on an horizontal edge of board
    if player is 1 and y != n-1 or player is 2 and y != 0:
        return board[y + move_direction(player)][(x-1 if x-1 > 0 else 0):x+2]
    else:
        return []

def move_direction(player: int) -> int:
    """Return the direction that player's pawns should be moving."""

    return 1 if player is 1 else -1

def where(board: Board, n: int, p: int, player: int, i: int, j: int) -> int:
    """Ask player where he wants to move the pawn located at i and j.
    High level implementation.
    """

    print("Where do you want to move this pawn ?")
    return where_(board, n, p, player, i, j)

def where_(board: Board, n: int, p: int, player: int, x: int, y: int) -> int:
    """Let player choose to which column he wants to move the pawn present at
    x and y coordinates and return this number if it is valid, otherwise re-ask
    him by re-calling the function.
    Low level implementation of where function.
    """

    available_moves = pawn_available_moves(board, n, p, player, x, y)
    pick = int(input("Column number (" + str(available_moves)[1:-1] + "): "))

    if pick in available_moves:
        return pick
    else:
        print("You cannot move it there, please retry.")
        return where_(board, n, p, player, x, y)

def pawn_available_moves(board: Board, n: int, p: int, player: int, x: int,
                         y: int) -> Row:
    """After computing the squares in front of the pawn in x and y, return the
    filtered list of the columns numbers where, according to the rules, this
    pawn can move.
    """

    facing_columns = pawn_facing_columns(p, x)
    facing_squares = pawn_facing_squares(board, n, player, x, y)
    opponent = 3 - player

    return [
        col_index
        for col_index, square in zip(facing_columns, facing_squares)
        if square is not player and (col_index, square) != (x, opponent)
    ]

def pawn_facing_columns(p: int, x: int) -> Row:
    """Return columns indexes that faces a pawn located at x and y."""

    return [
        column
        for column in [x-1, x, x+1]
        if column >= 0 and column < p
    ]

def breaktrough(n: int, p: int):
    """This is the main procedure of the game."""

    # Raising number of rows if it does not match the rules
    if not n > 4:
        n = 5

    # Greet the player(s)
    greet()

    # Now, initiate the first turn and the subsequent ones
    winner = turn(new_board(n, p), n, p)

    # Congratulate the winner
    congrats(winner)

    # Terminate the process
    exit(0)

def greet() -> None:
    """Welcome the player(s)."""

    print("Welcome! Ready to play breaktrough? Go!")

def congrats(player: int) -> None:
    """Felicitate player for winning the game."""

    print("Congratulations player " + str(player) + "! You have won this game!")

def turn(board: Board, n: int, p: int, _round: int = 1) -> int:
    """Compute a turn."""

    player = 2 - _round % 2

    print("This is player " + str(player) + "'s turn.")
    display(board)

    if int(argv[3]) is player:
        ai_turn(board, n, p, player)
    else:
        player_turn(board, n, p, player)

    if not someone_won(board):
        return turn(board, n, p, _round+1)
    else:
        display(board)
        return player

def player_turn(board: Board, n: int, p: int, player: int) -> None:
    """Resolve player's turn."""

    x, y = select_pawn(board, n, p, player)
    selected_column_to_move_to = where(board, n, p, player, x, y)

    move_pawn(board, x, y, selected_column_to_move_to)

def ai_turn(board: Board, n: int, p: int, player: int) -> None:
    """Process AI's turn. The IA solely chooses a random pawn and moves it in a
    random square in front of it.
    """

    print("(AI's turn.)")

    x, y = select_random_pawn(board, n, p, player)
    pawn_dest_column = choice(pawn_available_moves(board, n, p, player, x, y))

    print("Move pawn [", x, ";", y, "] to [", pawn_dest_column, ";",
          y+move_direction(player), "]")

    move_pawn(board, x, y, pawn_dest_column)

def move_pawn(board: Board, x: int, y: int, dest_column: int) -> None:
    """Move the pawn located at x and y to dest_column in the direction it
    faces.
    Lists love side-effects.
    """

    pawn = board[y][x]
    board[y + move_direction(pawn)][dest_column] = pawn
    board[y][x] = 0 # Empty the square where the pawn was located before moving


def select_random_pawn(board: Board, n: int, p: int,
                       player: int) -> Tuple[int, int]:
    """Select a random pawn owned by player and able to move and return its
    coordinates.
    """

    return choice([
        (x, y)
        for y, row in enumerate(board)
        for x, _ in enumerate(row)
        if pawn_valid(board, n, p, player, x, y)
    ])

def someone_won(board: Board) -> bool:
    """Check if, according to the rules, one of the players won."""

    return (not still_has_pawns(board, 1) or
            not still_has_pawns(board, 2) or
            2 in board[0] or # Has a black pawn reached the white starting line?
            1 in board[-1]) # Has a white pawn reached the black starting line?

def still_has_pawns(board: Board, player: int) -> bool:
    """Does player still have at least one pawn?"""

    return player in flatten(board)

def flatten(l: List[List[Any]]) -> List[Any]:
    """Given a two dimensional list, return a one dimensional list being the
    concatenation of all the element inside the original list.
    """

    return [x for y in l for x in y]

if __name__ == "__main__":
    # argv[1]: board height
    # argv[2]: board width
    # argv[3]: ai's player number

    if len(argv) == 4:
        breaktrough(int(argv[1]), int(argv[2]))
    else:
        print("Invalid arguments.")
        print("Usage:",
              "python3 breaktrough.py <board_height> <board_width> <ai_color>")
        print("board_height: Set board's height")
        print("board_width: Set board's width")
        print("ai_color: Setting this parameter to 1 will let AI play as the",
              "white pawns, 2 as the black pawns and anything else will",
              "disable it.")
        exit(1)
