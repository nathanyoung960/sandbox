from grid import GameGrid
from common import Vector2
from enum import Enum
particleSize = 5

class CollDir(Enum):
    LEFT = Vector2(-1, 0)
    RIGHT = Vector2(1, 0)
    UP = Vector2(0, -1)
    DOWN = Vector2(0, 1)

class Physics:
    def __init__(self):
        self.grid = GameGrid.__singleton__()

    def tickAllParticles(this):
        for p in this.grid.tileArray:
            p.__onTick__()

    def addParticleToGrid(this, particle):
        this.grid.tileArray.append(particle)

    def checkForCollisions(this, particle, dir: Vector2) -> bool:
        # temporary code
        # TODO: make it actually easy to read
        # TODO: make it less brute force, maybe a grid system would be nice
        # to make collision checking faster

        particleX = particle.pos.x
        particleY = particle.pos.y

        for p in this.grid.tileArray:
            if (p == particle):
                continue # /* skip over ourselves so we don't register ourself as a collision */

            # /* helper variables because python hates typecasting */
            # /* python typesafety itself is a oxymoron */
            pX = p.pos.x
            pY = p.pos.y

            if ((pX == particleX - 1) or (particleX - 1 <= 0)) and dir == CollDir.LEFT:
                return True
            
            if ((pX == particleX + 1) or (particleX + 1 >= this.grid.extents.x)) and dir == CollDir.RIGHT:
                return True
        
            if (int(particleY) == (int(pY) - 1)):
                return True
            if (particleY >= (this.grid.extents.y//particleSize)-1) and dir == CollDir.DOWN:
                return True
            
            # if ((pY == particleY - 1)  or (particleY - 1 <= 0)) and dir == CollDir.UP:
            #     return True
            return False
            

    @staticmethod
    def __singleton__():
        return singleton

singleton = Physics()