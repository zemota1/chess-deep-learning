import numpy as np

from chessPieces import *
from game import *

if __name__ == '__main__':

    game = Game()

    game.add_piece(Pawn(position=[1, 0], player='a'))
    game.add_piece(Pawn(position=[1, 1], player='a'))
    game.add_piece(Pawn(position=[1, 2], player='a'))
    game.add_piece(Pawn(position=[1, 3], player='a'))
    game.add_piece(Pawn(position=[1, 4], player='a'))
    game.add_piece(Pawn(position=[1, 5], player='a'))
    game.add_piece(Pawn(position=[1, 6], player='a'))
    game.add_piece(Pawn(position=[1, 7], player='a'))
    game.add_piece(Rook(position=[0, 0], player='a'))
    game.add_piece(Rook(position=[0, 7], player='a'))
    game.add_piece(Knights(position=[0, 1], player='a'))
    game.add_piece(Knights(position=[0, 6], player='a'))
    game.add_piece(Bishop(position=[0, 2], player='a'))
    game.add_piece(Bishop(position=[0, 5], player='a'))
    game.add_piece(King(position=[0, 4], player='a'))
    game.add_piece(Queen(position=[0, 3], player='a'))

    game.add_piece(Pawn(position=[6, 0], player='b'))
    game.add_piece(Pawn(position=[6, 1], player='b'))
    game.add_piece(Pawn(position=[6, 2], player='b'))
    game.add_piece(Pawn(position=[6, 3], player='b'))
    game.add_piece(Pawn(position=[6, 4], player='b'))
    game.add_piece(Pawn(position=[6, 5], player='b'))
    game.add_piece(Pawn(position=[6, 6], player='b'))
    game.add_piece(Pawn(position=[6, 7], player='b'))
    game.add_piece(Rook(position=[7, 0], player='b'))
    game.add_piece(Rook(position=[7, 7], player='b'))
    game.add_piece(Knights(position=[7, 1], player='b'))
    game.add_piece(Knights(position=[7, 6], player='b'))
    game.add_piece(Bishop(position=[7, 2], player='b'))
    game.add_piece(Bishop(position=[7, 5], player='b'))
    game.add_piece(King(position=[7, 4], player='b'))
    game.add_piece(Queen(position=[7, 3], player='b'))

    game.move(position1=[6, 1], position2=[5, 1], player="b")
    game.move(position1=[5, 1], position2=[4, 1], player="b")
    game.move(position1=[4, 1], position2=[3, 1], player="b")
    game.move(position1=[3, 1], position2=[2, 1], player="b")
    game.move(position1=[2, 1], position2=[1, 1], player="b")

