
from position import Position
class Camera():
    def __init__(self, position ,focale = (0,0,5)):
        self.position = position
        self.f = Position(focale)