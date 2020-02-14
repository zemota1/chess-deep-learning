from abc import ABC, abstractmethod

class Piece(ABC):

    def __init__(self, position: list, team: str):
        self.team = team
        self.position = position
        self.alive = True

    def is_alive(self):
        return self.alive

    def killed(self):
        self.alive = False

    def get_position(self):
        return self.position

    def set_position(self, position: list):
        self.position = position

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class Pawn(Piece):

    def __init__(self, position, team):
        super().__init__(position, team)

    def __repr__(self):
        return f"{self.team}6"

    def move(self, position):
        if self.team == 'a':
            if position[1] == self.position[1] + 1:
                self.position[1] = self.position[1] + 1
            else:
                print("cannot move")
        if self.team == 'b':
            if position[1] == self.position[1] - 1:
                self.position[1] = self.position - 1
            else:
                print("cannot move")


class King(Piece):

    def __init__(self, position, team):
        super().__init__(position, team)
        self.check = False

    def __repr__(self):
        return f"{self.team}1"

    def move(self, position):
        if (position[0] == (self.position[0] + 1 or self.position[0] + 1 or self.position[0])) \
                or (position[1] == (self.position[1] + 1 or self.position[1] + 1 or self.position[1])):
            self.position = position
        else:
            print("cannot move")

    def set_check(self):
        self.check = True

    def get_check(self):
        return self.check


class Rook(Piece):

    def __init__(self, position, team):
        super().__init__(position, team)

    def __repr__(self):
        return f"{self.team}5"

    def move(self, position):
        if position[0] == self.position[0] or position[1] == self.position[1]:
            self.position = position
        else:
            print("cannot move")


class Bishop(Piece):

    def __init__(self, position, team):
        super().__init__(position, team)

    def __repr__(self):
        return f"{self.team}3"

    def move(self, position):
        if abs(position[0]-self.position[0]) == abs(position[1]-self.position[1]):
            self.position = position
        else:
            print("cannot move")


class Queen(Piece):

    def __init__(self, position, team):
        super().__init__(position, team)

    def __repr__(self):
        return f"{self.team}2"

    def move(self, position):
        if (abs(position[0]-self.position[0]) == abs(position[1]-self.position[1])) \
                or position[0] == self.position[0] \
                or position[1] == self.position[1]:
            self.position = position

        else:
            print("cannot move")


class Knights(Piece):

    def __init__(self, position, team):
        super().__init__(position, team)

    def __repr__(self):
        return f"{self.team}4"

    def move(self, position):
        if ((self.position[0] == (position[0] + 1 or position[0] - 1))
            and (self.position[1] == (position[1] + 2 or position[1] - 2)))  \
                or \
                ((self.position[0] == (position[0] + 2 or position[0] - 2))
                 and (self.position[1] == (position[1] + 1 or position[1] - 1))):\
                self.position = position

        else:
            print("cannot move")
