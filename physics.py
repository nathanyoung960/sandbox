from grid import GameGrid
from common import Vector2
from enum import Enum
import threading
import random
import time
particleSize = 15

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
        dispatchThreads(this)

    def addParticleToGrid(this, particle):
        this.grid.tileArray.append(particle)

    def getParticleAtPos(this, pos: Vector2):
        for p in this.grid.tileArray:
            if (p.pos.x == pos.x) and (p.pos.y == pos.y):
                return p
        return None

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
            pX = p.pos.x
            pY = p.pos.y

            if (pX - particleX >= 2 or particleX - pX <= -2):
                continue
            if (pY - particleY >= 2 or particleY - pY <= -2):
                continue

            if ((pY - particleY == dir.value.y) and (pX - particleX == dir.value.x)) or outOfBounds(particle.pos, this.grid, dir):
                return True
        return False
            

    @staticmethod
    def __singleton__():
        return singleton

chunkSize = 15
def chunked_list(lst, chunk_size: int = chunkSize):
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]

def dispatchThreads(this: Physics):
    def tickAssignedParticles(this: Physics, particleList):
        for p in particleList:
            p.__onTick__()
            time.sleep(random.uniform(0.005, 0.2))

    for list in chunked_list(this.grid.tileArray):
        threading.Thread(target=tickAssignedParticles, args=(this, list)).start()

singleton = Physics()