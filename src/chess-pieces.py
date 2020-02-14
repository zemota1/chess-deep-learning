from abc import ABC, abstractmethod


class Piece(ABC):

    def __init__(self, position:list, team:str):
        self.team = team
        self.position = position
        self.alive = True

    def is_alive(self):
        return self.alive

    def killed(self):
        self.alive = False

    def get_position(self):
        return self.position

    def set_position(self, position:tuple):
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
        string = {f'Piece idx = {8}. Position = {self.position}. Is alive = {self.alive}'}
        return str(string)

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
        return str(1)

    def move(self, position):
        if (position[0] == (self.position[0] + 1 or self.position[0] + 1 or self.position[0])) \
                or (position[1] == (self.position[1] + 1 or self.position[1] + 1 or self.position[1])):
            self.position = position

    def set_check(self):
        self.check = True

    def get_check(self):
        return self.check


if __name__ == '__main__':

    p1 = Pawn(position=[1, 1], team='a')
    p1.move(position=[1, 2])
    print(p1)
