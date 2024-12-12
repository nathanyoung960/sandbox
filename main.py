# Handle central game logic

from common import *
import graphics
from physics import Physics
from particle import *

physicsHandler = Physics.__singleton__()

def onAppStart(app):
    for x in range(6):
        for y in range(6):
            physicsHandler.addParticleToGrid(Sand(Vector2(x, y*2)))
    # physicsHandler.addParticleToGrid(Sand(Vector2(50, 60)))
    # physicsHandler.addParticleToGrid(Sand(Vector2(50, 50)))
    # physicsHandler.addParticleToGrid(Sand(Vector2(50, 40)))

def redrawAll(app):
    graphics.renderBackground(app)
    graphics.renderGame(app)

def onStep(app):
    physicsHandler.tickAllParticles()

# app.width = graphics.canvasSizeX
# app.height = graphics.canvasSizeY
runApp(width = graphics.canvasSizeX, height = graphics.canvasSizeY)