"""The First Attack game."""

from sys import argv
from typing import List, Tuple, Any

Row = List[int]
Board = List[Row]

def new_board(n: int) -> Board:
    """Return a fresh new empty board for a new game."""

    return [[0 for _ in range(n)] for _ in range(n)]

def display(board: Board, n: int) -> None:
    """Display the board in an understable manner to the user."""

    for row in board:
        for square in row:
            if square is 1:
                print("o", end=' ')
            elif square is 3:
                print("x", end=' ')
            else:
                print('.', end=' ')
        print()

def not_finish(board: Board, n: int) -> bool:
    """Evaluate if the board is still playable or not."""

    if int(argv[2]) is 0:
        return 0 in flatten(board)
    else:
        return (0 in flatten(board) or
                0 in empty_squares_with_value(board, 2) or
                0 in empty_squares_with_value(board, 4))

def flatten(l: List[List[Any]]) -> List[Any]:
    """Given a two dimensional list, return a one dimensional list being the
    concatenation of all the element inside the original list.
    """

    return [x for y in l for x in y]

def empty_squares_with_value(board: Board, value: int) -> Row:

    return [
        (0 if square is value else square)
        for row in board
        for square in row
    ]

def select_square(board: Board, n: int, pawn_value: int) -> Tuple[int, int]:
    """Ask user the coordinates to input the coordinates of square until his
    selection is valid acoording to the rules.
    """

    print("Select a square where you may want to put a pawn.")
    i = int(input("Its x coordinates: "))
    j = int(input("Its y coordinates: "))

    if square_valid(board, n, pawn_value, i, j):
        return i, j
    else:
        print("You can't put a pawn there, sorry. Please, retry.")
        return select_square(board, n, pawn_value)

def square_valid(board: Board, n: int, pawn_value: int, i: int, j: int) -> bool:
    """Check if the square at i and j is available to put a pawn on it."""

    return (coordinates_within_board(n, i, j) and
            square_playable(board, pawn_value, i, j))

def coordinates_within_board(n: int, i: int, j: int) -> bool:
    """Are the given coordinates inside the board?"""

    return i < n and j < n and i >= 0 and j >= 0

def square_playable(board: Board, pawn_value: int, i: int, j: int) -> bool:
    """Can a pawn be placed onto the square at i and j?"""

    square = board[j][i]
    opponent_value = 3 if pawn_value is 1 else 1

    if int(argv[2]) is 0:
        return square is 0
    else:
        return (square is not pawn_value and
                square is not pawn_value+1 and # unplayable square for player
                square is not opponent_value and
                square is not 5) # 5 is unplayable for the two players

def update(board: Board, n: int, pawn_value: int, i: int, j: int) -> None:
    """Procedure that put a pawn at given coordinates and update the board
    accordingly.
    """

    put_pawn_at(board, pawn_value, i, j)
    block_row(board, pawn_value, j)
    block_column(board, pawn_value, i)
    block_diagonals(board, pawn_value, i, j)

def put_pawn_at(board: Board, pawn_value: int, i: int, j: int) -> None:
    """Place on the board a player pawn at i and j."""

    board[j][i] = 1 if int(argv[2]) is 0 else pawn_value

def block_row(board: Board, pawn_value: int, j: int) -> None:
    """Change all squares on row j to unplayable for concerned player."""

    for index, _ in enumerate(board[j]):
        block(board, pawn_value, index, j)

def block_column(board: Board, pawn_value: int, i: int) -> None:
    """Change all squares on column i to unplayable for player owning
    pawns with pawn_value.
    """

    for index, _ in enumerate(board):
        block(board, pawn_value, i, index)

def block_diagonals(board: Board, pawn_value: int, i: int, j: int) -> None:
    """Change all squares aligned diagonaly with pawn at i;j to unplayable."""

    for row_index, row in enumerate(board):
        for col_index, _ in enumerate(row):
            if abs(row_index-j) is abs(col_index-i):
                block(board, pawn_value, col_index, row_index)

def block(board: Board, pawn_value: int, i: int, j: int) -> None:
    """Block the square located at i and j, taking into account the player and
    game mode."""

    square = board[j][i]

    if int(argv[2]) is 0:
        if square is 0:
            board[j][i] = 2
    else:
        if square is 0:
            board[j][i] = pawn_value+1
        elif square is 2 or square is 4:
            board[j][i] = 5

def first_attack(n: int) -> None:
    """Main procedure."""

    # Greet the player(s)
    greet()

    # Now, initiate the first turn and the subsequent ones
    winner = turn(new_board(n), n)

    # Congratulate the winner
    congrats(winner)

    # Terminate the process
    exit(0)

def greet():
    """Welcome the player(s)."""

    print("Welcome! Ready to play First Attack? Go!")

def congrats(player: int):
    """Felicitate player for winning the game."""

    print("Congratulations player " + str(player) + "! You have won this game!")

def turn(board: Board, n: int, _round: int = 1) -> int:

    player = 2 - _round % 2
    pawn_value = 1 if player is 1 else 3 # player's pawns value

    print("This is Player " + str(player) + "'s turn.")
    display(board, n)

    i, j = select_square(board, n, pawn_value)
    update(board, n, pawn_value, i, j)

    if not_finish(board, n):
        return turn(board, n, _round+1)
    else:
        display(board, n)
        return player

if __name__ == "__main__":
    # argv[1]: board size
    # argv[2]: unicolor or bicolor game mode

    if len(argv) == 3:
        first_attack(int(argv[1]))
    else:
        print("Invalid arguments.")
        print("Usage:",
              "python3 first_attack.py <board_size> <color_mode>")
        print("Setting the color_mode parameter to 0 will launch the game into",
              "the single color mode and to 1 the bi-color mode.")
        exit(1)
