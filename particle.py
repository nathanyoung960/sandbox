from grid import GameGrid
from common import *

class _MetaParticle:
    def __init__(this, gridPos: Vector2):
        this.pos = gridPos
        this.gridSingleton = GameGrid.__singleton__()

    # /* Due to the object-oriented nature of Python, ParticleInstance will be the ticked particle. */
    def __onTick__(particleInstance):
        pass

class Sand(_MetaParticle):
    def __onTick__(particleInstance):
        print(f"I've been ticked and my position is ({particleInstance.pos.x}, {particleInstance.pos.y})")
        return super().__onTick__()