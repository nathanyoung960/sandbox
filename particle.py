from common import Color3, Vector2
from grid import GameGrid
from common import *
from physics import Physics

physicsSingleton = Physics.__singleton__()

class _MetaParticle:
    def __init__(this, gridPos: Vector2, particleColor: Color3 = Color3(0, 0, 0, 255), affectedByGravity: bool = True):
        this.pos = gridPos
        this.gridSingleton = GameGrid.__singleton__()
        this.color = particleColor
        this.useGravity = affectedByGravity

    # /* Due to the object-oriented nature of Python, ParticleInstance will be the ticked particle. */
    # /* Handles base logic for particles, i.e. gravity */
    def __onTick__(particleInstance):
        if (particleInstance.useGravity):
            foundCollision = False
            for collisionPos in physicsSingleton.checkForCollisions(particleInstance):
                if collisionPos.y == 1:
                    foundCollision = True
                    break

            if (not foundCollision):
                particleInstance.pos.y = particleInstance.pos.y + 1

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