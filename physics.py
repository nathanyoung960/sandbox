from grid import GameGrid
from particle import _MetaParticle
from common import Vector2

class Physics:
    def __init__(self):
        self.grid = GameGrid.__singleton__()

    def tickAllParticles(this):
        for p in this.grid.tileArray:
            p.__onTick__()

    def addParticleToGrid(this, particle: _MetaParticle):
        this.grid.tileArray.append(particle)

    def checkForCollisions(this, particle: _MetaParticle) -> list[Vector2]:
        # temporary code
        # TODO: make it actually easy to read
        # TODO: make it less brute force, maybe a grid system would be nice
        # to make collision checking faster
        for p in this.grid:
            if (p == particle):
                continue # /* skip over ourselves so we don't register ourself as a collision */

            # /* helper variables because python hates typecasting */
            # /* python typesafety itself is a oxymoron */
            pX = p.pos.x
            pY = p.pos.y
            particleX = particle.pos.x
            particleY = particle.pos.y

            collisions = []

            if (pX == particleX - 1) or (pX - 1 <= 0):
                collisions.append(Vector2(-1, 0)) # /* normalized vector for the left */
            
            if (pX == particleX + 1) or (pX + 1 >= this.grid.extents.x):
                collisions.append(Vector2(1, 0)) # /* normalized vector for the right */
            
            if (pY == particleY + 1) or (pY + 1 >= this.grid.extents):
                collisions.append(Vector2(0, 1)) # /* normalized vector for down */
            
            if (pY == particleY - 1)  or (pY - 1 <= 0):
                collisions.append(Vector2(0, -1)) # /* normalized vector for up */

            return collisions
            

    @staticmethod
    def __singleton__():
        return singleton

singleton = Physics()