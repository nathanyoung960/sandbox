class GameGrid():
    @staticmethod
    def __singleton__():
        return singleton
    
    def __init__(this):
        this.tileArray = []

singleton = GameGrid()