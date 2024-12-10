from common import Color3, Vector2
from grid import GameGrid
from common import *

class _MetaParticle:
    def __init__(this, gridPos: Vector2, particleColor: Color3 = Color3(0, 0, 0, 255)):
        this.pos = gridPos
        this.gridSingleton = GameGrid.__singleton__()
        this.color = particleColor

    # /* Due to the object-oriented nature of Python, ParticleInstance will be the ticked particle. */
    def __onTick__(particleInstance):
        pass

class Sand(_MetaParticle):
    def __init__(this, gridPos: Vector2, particleColor: Color3 = Color3(0, 0, 0, 255)):
        super().__init__(gridPos, particleColor)
        this.color = Color3(255, 224, 138, 255)

    def __onTick__(particleInstance):
        print(f"I've been ticked and my position is ({particleInstance.pos.x}, {particleInstance.pos.y})")
        return super().__onTick__()
    
class Glass(_MetaParticle):
    def __init__(this, gridPos: Vector2, particleColor: Color3 = Color3(0, 0, 0, 255)):
        super().__init__(gridPos, particleColor)
        this.color = Color3(230, 241, 242, 255)

    def __onTick__(particleInstance):
        return super().__onTick__()