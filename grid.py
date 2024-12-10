from Vector2 import Vector2

class GameGrid():
    @staticmethod
    def __singleton__():
        return singleton
    
    def __init__(this):
        this.tileArray = []
        this.extents = Vector2(700, 700) # top-left to bottom-right

singleton = GameGrid()
