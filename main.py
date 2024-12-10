# Handle central game logic

from common import *
import graphics
from physics import Physics
from particle import *

physicsHandler = Physics.__singleton__()

def onAppStart(app):
    for x in range(6):
        physicsHandler.addParticleToGrid(Sand(Vector2(x, x), Color3(255, 224, 138, 255)))

def redrawAll(app):
    graphics.renderBackground(app)
    graphics.renderGame(app)

def onStep(app):
    physicsHandler.tickAllParticles()

# app.width = graphics.canvasSizeX
# app.height = graphics.canvasSizeY
cmu_graphics.runApp(width = graphics.canvasSizeX, height = graphics.canvasSizeY)