#def where(board, n, p, player, i, j):
#    """"""
#def breaktrough(n, p):
#    """"""
#def select_pawn(board, n, p, player):
#    """"""

def new_board(n, p):
    """ n: int
        p: int
        return: list[list[int]]

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
    """ board: list[list[int]]
        n: int
        p: int
        return: nothing

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
