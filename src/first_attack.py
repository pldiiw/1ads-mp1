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
            else:
                print('.', end=' ')
        print()

def not_finish(board: Board, n: int) -> bool:
    """Evaluate if the board is still playable or not."""

    return 0 in flatten(board)

def flatten(l: List[List[Any]]) -> List[Any]:
    """Given a two dimensional list, return a one dimensional list being the
    concatenation of all the element inside the original list.
    """

    return [x for y in l for x in y]

def select_square(board: Board, n: int) -> Tuple[int, int]:
    """Ask user the coordinates to input the coordinates of square until his
    selection is valid acoording to the rules.
    """

    print("Select a square where you may want to put a pawn.")
    i = int(input("Its x coordinates: "))
    j = int(input("Its y coordinates: "))

    if square_valid(board, n, i, j):
        return i, j
    else:
        print("You can't put a pawn there, sorry. Please, retry.")
        return select_square(board, n)

def square_valid(board: Board, n: int, i: int, j: int) -> bool:
    """Check if the square at i and j is available to put a pawn on it."""

    return (coordinates_within_board(n, i, j) and
            square_playable(board, i, j))

def coordinates_within_board(n: int, i: int, j: int) -> bool:
    """Are the given coordinates inside the board?"""

    return i < n and j < n and i >= 0 and j >= 0

def square_playable(board: Board, i: int, j: int) -> bool:
    """Can a pawn be placed onto the square at i and j?"""

    return board[j][i] is 0

def update(board: Board, n: int, i: int, j: int) -> None:
    """Procedure that put a pawn at given coordinates and update the board
    accordingly.
    """

    put_pawn_at(board, i, j)
    block_row(board, j)
    block_column(board, i)
    block_diagonals(board, i, j)

def put_pawn_at(board: Board, i: int, j: int) -> None:
    """Place on the board a pawn at i and j."""

    board[j][i] = 1

def block_row(board: Board, j: int) -> None:
    """Change all squares on row j to unplayable."""

    for index, square in enumerate(board[j]):
        board[j][index] = 2 if square is 0 else square

def block_column(board: Board, i: int) -> None:
    """Change all squares on column i to unplayable"""

    for row in board:
        square = row[i]
        row[i] = 2 if square is 0 else square

def block_diagonals(board: Board, i: int, j: int) -> None:
    """Change all squares aligned diagonaly with pawn at i;j to unplayable."""

    for row_index, row in enumerate(board):
        for col_index, square in enumerate(row):
            if abs(row_index-j) is abs(col_index-i) and square is 0:
                row[col_index] = 2

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

    print("This is Player " + str(player) + "'s turn.")
    display(board, n)

    i, j = select_square(board, n)
    update(board, n, i, j)

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
