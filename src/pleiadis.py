"""The Pleiadis game."""

from sys import argv
from typing import List, Tuple, Any

Row = List[int]
Board = List[Row]

def new_board(n: int) -> Board:
    """Return an empty game board."""

    return [[0 for _ in range(n)] for _ in range(n)]

def display(board: Board) -> None:
    """Log the board to the user in a pretty format."""

    for row in board:
        for square in row:
            if square is 1:
                print("x", end=' ')
            elif square is 2:
                print("o", end=' ')
            else:
                print('.', end=' ')
        print()

def select_square(board: Board, n: int, player: int) -> Tuple[int, int]:
    """Let user choose a square where he may wants to put a pawn in. This square
    should be valid under the rules of the game, otherwise it will propose user
    to pick another one.
    """

    print("Select a square where you may want to put a pawn in.")
    x = int(input("Its x coordinates: "))
    y = int(input("Its y coordinates: "))

    if square_valid(board, n, player, x, y):
        return x, y
    else:
        print("You can't put a pawn there, sorry. Please, retry.")
        return select_square(board, n, player)

def square_valid(board: Board, n: int, player: int, x: int, y: int) -> bool:
    """Evaluate if the square at x and y can receive one of player's pawns."""

    return (coordinates_within_board(n, x, y) and
            is_empty(board, x, y) and
            respect_adjacency_rule(board, player, x, y))

def coordinates_within_board(n: int, x: int, y: int) -> bool:
    """Are the given coordinates inside the board?"""

    return x < n and y < n and x >= 0 and y >= 0

def is_empty(board: Board, x: int, y: int) -> bool:
    """Is the given square empty?"""

    return board[y][x] is 0

def respect_adjacency_rule(board: Board, player: int, x: int,
                           y: int) -> bool:
    """Does the square located at x and y would respect the rules about adjacent
    pawns if there was a pawn belonging to player there?"""

    adjacent_squares = get_adjacent_squares(board, x, y)
    opponent = 3 - player

    return count(adjacent_squares, player) >= count(adjacent_squares, opponent)

def get_adjacent_squares(board: Board, x: int, y: int) -> Row:
    """Return a list containing the adjacent squares to the [x;y] one."""

    return [
        square
        for row_index, row in enumerate(board)
        for col_index, square in enumerate(row)
        if (abs(row_index - y) <= 1 and
            abs(col_index - x) <= 1 and
            [row_index, col_index] != [y, x]) # We don't want the square itself.
    ]

def count(l: List[Any], e: Any) -> int:
    """Count how many elements e there is inside l."""

    return len([v for v in l if v == e])

def put_pawn_at(board: Board, pawn: int, x: int, y: int) -> None:
    """Place on the board a player pawn at x and y."""

    board[x][y] = pawn

def pleiadis(n: int) -> None:
    """Main procedure."""

    # Greet the player(s)
    greet()

    # Now, initiate the first turn and the subsequent ones
    winner = turn(new_board(n), n)

    # Congratulate the winner
    congrats(winner)

    # Terminate the process
    exit(0)

def greet() -> None:
    """Welcome the player(s)."""

    print("Welcome! Ready to play Pleiadis? Go!")

def congrats(player: int) -> None:
    """Felicitate player for winning the game."""

    print("Congratulations player " + str(player) + "! You have won this game!")

def turn(board: Board, n: int, _round: int = 1) -> int:
    """Execute one turn of the game. If no winner is found, goes recursive."""

    player = 2 - _round % 2

    print("This is Player " + str(player) + "'s turn.")
    display(board)

    x, y = select_square(board, n, player)
    put_pawn_at(board, player, x, y)

    if not_finish(board, n):
        return turn(board, n, _round+1)
    else:
        display(board)
        return player

def not_finish(board: Board, n: int) -> bool:
    """Evaluate if the board is still playable or not. If the two players can
    still play, then the game is not over yet.
    """

    return can_still_play(board, n, 1) and can_still_play(board, n, 2)

def can_still_play(board: Board, n: int, player: int, _x: int = 0,
                   _y: int = 0) -> bool:
    """Is player still able to play?"""

    # If at least one square is playable for player, then he can still play.
    if square_valid(board, n, player, _x, _y):
        return True
    # If no playable square has been found when we iterate over the end of the
    # board, it means that player can't play anymore.
    elif _x is n-1 and _y is n-1:
        return False
    # Test next square if current one is not playable for player.
    else:
        return can_still_play(board, n, player, (0 if _x is n-1 else _x+1),
                              (_y+1 if _x is n-1 else _y))

if __name__ == "__main__":
    # argv[1]: board size
    # argv[2]: enable or not ai

    if len(argv) == 3:
        pleiadis(int(argv[1]))
    else:
        print("Invalid arguments.")
        print("Usage:",
              "python3 pleiadis.py <board_size> <enable_ai>")
        print("Setting enable_ai to 1 will enable AI. Use 0 to disable it.")
        exit(1)
