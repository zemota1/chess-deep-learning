import numpy as np

from chessPieces import *

if __name__ == '__main__':

    team_a = {
        Pawn(position=[1, 0], team='a'), Pawn(position=[1, 1], team='a'),
        Pawn(position=[1, 2], team='a'), Pawn(position=[1, 3], team='a'),
        Pawn(position=[1, 4], team='a'), Pawn(position=[1, 5], team='a'),
        Pawn(position=[1, 6], team='a'), Pawn(position=[1, 7], team='a'),
        Rook(position=[0, 0], team='a'), Rook(position=[0, 7], team='a'),
        Knights(position=[0, 1], team='a'), Knights(position=[0, 6], team='a'),
        Bishop(position=[0, 2], team='a'), Bishop(position=[0, 5], team='a'),
        King(position=[0, 4], team='a'), Queen(position=[0, 3], team='a')
    }

    team_b = {
        Pawn(position=[6, 0], team='b'), Pawn(position=[6, 1], team='b'),
        Pawn(position=[6, 2], team='b'), Pawn(position=[6, 3], team='b'),
        Pawn(position=[6, 4], team='b'), Pawn(position=[6, 5], team='b'),
        Pawn(position=[6, 6], team='b'), Pawn(position=[6, 7], team='b'),
        Rook(position=[7, 0], team='b'), Rook(position=[7, 7], team='b'),
        Knights(position=[7, 1], team='b'), Knights(position=[7, 6], team='b'),
        Bishop(position=[7, 2], team='b'), Bishop(position=[7, 5], team='b'),
        King(position=[7, 4], team='b'), Queen(position=[7, 3], team='b')
    }

    board = np.empty([8, 8], dtype=object)

    for team in [team_a, team_b]:
        for piece in team:
            position = piece.get_position()
            board[tuple(position)] = piece

    print(board)
