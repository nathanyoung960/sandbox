from grid import GameGrid
from common import Vector2
from enum import Enum
particleSize = 10

class CollDir(Enum):
    CENTER = Vector2(0, 0)
    LEFT = Vector2(-1, 0)
    RIGHT = Vector2(1, 0)
    UP = Vector2(0, -1)
    DOWN = Vector2(0, 1)
    DIAGONAL_RIGHT_DOWN = Vector2(1, 1)
    DIAGONAL_LEFT_DOWN = Vector2(-1, 1)

def outOfBounds(pos: Vector2, grid: GameGrid, dir: CollDir = None):
    if (dir != None):
        d = dir.value
    else:
        d = CollDir.CENTER

    if (d.x == 1 and (pos.x >= grid.extents.x//particleSize)) or (d.x == -1 and (pos.x <= 0)) or (d.y == 1 and (pos.y + 1 >= grid.extents.y//particleSize)) or (d.y == -1 and (pos.y <= 0)):
        return True

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
        particleY = round(particle.pos.y)

        for p in this.grid.tileArray:
            if (p == particle):
                continue # /* skip over ourselves so we don't register ourself as a collision */

            # /* helper variables because python hates typecasting */
            # /* python typesafety itself is a oxymoron */
            pX = round(p.pos.x)
            pY = round(p.pos.y)

            if ((pY - particleY == dir.value.y) and (pX - particleX == dir.value.x)) or outOfBounds(particle.pos, this.grid, dir):
                return True
        return False
            

    @staticmethod
    def __singleton__():
        return singleton

singleton = Physics()