import numpy as np
from chessPieces import *


class Game:

    def __init__(self):
        self.__board = np.empty([8, 8], dtype=object)
        self.__board[:] = 0
        self.__pieces = {'a': [], 'b': []}

    def get_board(self):
        return self.__board

    def get_pieces(self):
        return self.__pieces

    def get_piece(self, position):
        if self.get_board()[tuple(position)] != 0:
            return self.get_board()[tuple(position)]
        else:
            return False

    def add_piece(self, piece: Piece):
        self.__board[tuple(piece.get_position())] = piece
        self.__pieces[piece.get_player()].append(piece)

    def move(self, position1: list, position2: list, player: str):
        piece_1 = self.get_piece(position1)
        if piece_1.get_player() == player and piece_1.is_alive():
            piece_2 = self.get_piece(position=position2)
            if piece_2:
                piece_2.killed()
                piece_2.set_position(position=None)

            self.__board[tuple(piece_1.get_position())] = 0
            piece_1.move(position=position2)
            self.__board[tuple(piece_1.get_position())] = piece_1

        else:
            print("wrong piece selected")
            pass

    def __repr__(self):
        return str(self.__board)
