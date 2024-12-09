from grid import GameGrid
from particle import _MetaParticle

class Physics:
    def __init__(self):
        self.grid = GameGrid.__singleton__()

    def tickAllParticles(this):
        for p in this.grid.tileArray:
            p.__onTick__()

    def addParticleToGrid(this, particle: _MetaParticle):
        this.grid.tileArray.append(particle)

    @staticmethod
    def __singleton__():
        return singleton

singleton = Physics()