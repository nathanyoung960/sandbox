from grid import GameGrid
from common import Vector2

class Physics:
    def __init__(self):
        self.grid = GameGrid.__singleton__()

    def tickAllParticles(this):
        for p in this.grid.tileArray:
            p.__onTick__()

    def addParticleToGrid(this, particle):
        this.grid.tileArray.append(particle)

    def checkForCollisions(this, particle) -> list[Vector2]:
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

            collisions = []

            if (pX == particleX - 1) or (particleX - 1 <= 0):
                collisions.append(Vector2(-1, 0)) # /* normalized vector for the left */
            
            if (pX == particleX + 1) or (particleX + 1 >= this.grid.extents.x):
                collisions.append(Vector2(1, 0)) # /* normalized vector for the right */
        
            print(f"Checking particle Y: {pY}, Checking main particle Y: {particleY}, Is Down Collision = {pY == particleY + 1}")
            if (pY == particleY + 1) or (particleY + 1 >= this.grid.extents.y):
                collisions.append(Vector2(0, 1)) # /* normalized vector for down */
            
            if (pY == particleY - 1)  or (particleY - 1 <= 0):
                collisions.append(Vector2(0, -1)) # /* normalized vector for up */

            return collisions
            

    @staticmethod
    def __singleton__():
        return singleton

singleton = Physics()