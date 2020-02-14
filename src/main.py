import numpy as np

from chessPieces import *

if __name__ == '__main__':

    team_a = [
        Pawn(position=[1, 0], player='a'), Pawn(position=[1, 1], player='a'),
        Pawn(position=[1, 2], player='a'), Pawn(position=[1, 3], player='a'),
        Pawn(position=[1, 4], player='a'), Pawn(position=[1, 5], player='a'),
        Pawn(position=[1, 6], player='a'), Pawn(position=[1, 7], player='a'),
        Rook(position=[0, 0], player='a'), Rook(position=[0, 7], player='a'),
        Knights(position=[0, 1], player='a'), Knights(position=[0, 6], player='a'),
        Bishop(position=[0, 2], player='a'), Bishop(position=[0, 5], player='a'),
        King(position=[0, 4], player='a'), Queen(position=[0, 3], player='a')
    ]

    team_b = [
        Pawn(position=[6, 0], player='b'), Pawn(position=[6, 1], player='b'),
        Pawn(position=[6, 2], player='b'), Pawn(position=[6, 3], player='b'),
        Pawn(position=[6, 4], player='b'), Pawn(position=[6, 5], player='b'),
        Pawn(position=[6, 6], player='b'), Pawn(position=[6, 7], player='b'),
        Rook(position=[7, 0], player='b'), Rook(position=[7, 7], player='b'),
        Knights(position=[7, 1], player='b'), Knights(position=[7, 6], player='b'),
        Bishop(position=[7, 2], player='b'), Bishop(position=[7, 5], player='b'),
        King(position=[7, 4], player='b'), Queen(position=[7, 3], player='b')
    ]

    team_b[0].move(position=(5,0))

    board = np.empty([8, 8], dtype=object)

    for team in [team_a, team_b]:
        for piece in team:
            position = piece.get_position()
            board[tuple(position)] = piece

    print(board)
