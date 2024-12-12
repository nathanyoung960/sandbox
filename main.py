# Handle central game logic

from common import *
import graphics
from physics import Physics
from particle import *

physicsHandler = Physics.__singleton__()

def onAppStart(app):
    b = 5
    s = 25
    for x in range(b, s):
        for y in range(b, s):
            physicsHandler.addParticleToGrid(Sand(Vector2(x, y)))
def redrawAll(app):
    graphics.renderBackground(app)
    graphics.renderGame(app)

def onStep(app):
    physicsHandler.tickAllParticles()

# app.width = graphics.canvasSizeX
# app.height = graphics.canvasSizeY
runApp(width = graphics.canvasSizeX, height = graphics.canvasSizeY)