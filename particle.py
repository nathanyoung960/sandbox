from common import Color3, Vector2
from grid import GameGrid
from common import *
from physics import Physics, CollDir
import random

physicsSingleton = Physics.__singleton__()

def clamp(x: int, min: int, max: int):
    if (x >= max):
        return max
    if (x <= min):
        return min
    return x

class _MetaParticle:
    def __init__(this, gridPos: Vector2, particleColor: Color3 = Color3(0, 0, 0, 255), affectedByGravity: bool = True, colorRandomness: int = 5):
        this.pos = gridPos
        this.gridSingleton = GameGrid.__singleton__()
        this.color = Color3(
            clamp(particleColor.r + random.randint(-colorRandomness, colorRandomness), 0, 255),
            clamp(particleColor.g + random.randint(-colorRandomness, colorRandomness), 0, 255),
            clamp(particleColor.b + random.randint(-colorRandomness, colorRandomness), 0, 255)
        )
        print(f"original color R: {particleColor.g} modified: {this.color.g}")
        this.useGravity = affectedByGravity

    # /* Due to the object-oriented nature of Python, ParticleInstance will be the ticked particle. */
    # /* Handles base logic for particles, i.e. gravity */
    def __onTick__(particleInstance):
        if (particleInstance.useGravity):
            if (physicsSingleton.checkForCollisions(particleInstance, CollDir.DOWN) == False):
                particleInstance.pos.y = particleInstance.pos.y + 1
            else:
                if (physicsSingleton.checkForCollisions(particleInstance, CollDir.DIAGONAL_RIGHT_DOWN) == False):
                    particleInstance.pos.y = particleInstance.pos.y + 1
                    particleInstance.pos.x = particleInstance.pos.x + 1
                elif (physicsSingleton.checkForCollisions(particleInstance, CollDir.DIAGONAL_LEFT_DOWN) == False):
                    particleInstance.pos.y = particleInstance.pos.y + 1
                    particleInstance.pos.x = particleInstance.pos.x - 1

class Sand(_MetaParticle):
    def __init__(this, gridPos: Vector2, particleColor: Color3 = Color3(0, 0, 0, 255)):
        super().__init__(gridPos, particleColor)
        this.color = Color3(255, 224, 138, 255)

    def __onTick__(particleInstance):
        return super().__onTick__()
    
class Glass(_MetaParticle):
    def __init__(this, gridPos: Vector2, particleColor: Color3 = Color3(0, 0, 0, 255)):
        super().__init__(gridPos, particleColor)
        this.color = Color3(230, 241, 242, 255)

    def __onTick__(particleInstance):
        return super().__onTick__()