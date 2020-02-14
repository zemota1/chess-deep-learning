from abc import ABC, abstractmethod


class Piece(ABC):

    def __init__(self, position: list, player: str):
        self.__player = player
        self.__position = position
        self.__alive = True

    def is_alive(self):
        return self.__alive

    def killed(self):
        self.__alive = False

    def get_position(self):
        return self.__position

    def set_position(self, position: list):
        self.__position = position

    def get_player(self):
        return self.__player

    @abstractmethod
    def move(self, position):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class Pawn(Piece):

    def __init__(self, position, player):
        super().__init__(position, player)

    def __repr__(self):
        return f"{self.get_player()}6"

    def move(self, position):
        if self.get_player() == 'a':
            if position[0] == self.get_position()[0] + 1:
                self.set_position(position)
            else:
                print("cannot move")
        if self.get_player() == 'b':
            if position[0] == self.get_position()[0] - 1:
                self.set_position(position)
            else:
                print("cannot move")


class King(Piece):

    def __init__(self, position, player):
        super().__init__(position, player)
        self.check = False

    def __repr__(self):
        return f"{self.get_player()}1"

    def move(self, position):
        if (position[0] == (self.get_position()[0] + 1 or self.get_position()[0] - 1 or self.get_position()[0])) \
                or (position[1] == (self.get_position()[1] + 1 or self.get_position()[1] - 1 or self.get_position()[1])):
            self.set_position(position)
        else:
            print("cannot move")

    def set_check(self):
        self.check = True

    def get_check(self):
        return self.check


class Rook(Piece):

    def __init__(self, position, player):
        super().__init__(position, player)

    def __repr__(self):
        return f"{self.get_player()}5"

    def move(self, position):
        if position[0] == self.get_position()[0] or position[1] == self.get_position()[1]:
            self.set_position(position)
        else:
            print("cannot move")


class Bishop(Piece):

    def __init__(self, position, player):
        super().__init__(position, player)

    def __repr__(self):
        return f"{self.get_player()}3"

    def move(self, position):
        if abs(position[0]-self.get_position()[0]) == abs(position[1]-self.get_position()[1]):
            self.set_position(position)
        else:
            print("cannot move")


class Queen(Piece):

    def __init__(self, position, player):
        super().__init__(position, player)

    def __repr__(self):
        return f"{self.get_player()}2"

    def move(self, position):
        if (abs(position[0]-self.get_position()[0]) == abs(position[1]-self.get_position()[1])) \
                or position[0] == self.get_position()[0] \
                or position[1] == self.get_position()[1]:
            self.set_position(position)

        else:
            print("cannot move")


class Knights(Piece):

    def __init__(self, position, player):
        super().__init__(position, player)

    def __repr__(self):
        return f"{self.get_player()}4"

    def move(self, position):
        if ((self.get_position()[0] == (position[0] + 1 or position[0] - 1))
            and (self.get_position()[1] == (position[1] + 2 or position[1] - 2)))  \
                or \
                ((self.get_position()[0] == (position[0] + 2 or position[0] - 2))
                 and (self.get_position()[1] == (position[1] + 1 or position[1] - 1))):\
                self.set_position(position)

        else:
            print("cannot move")
