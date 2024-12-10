# Handle central game logic

from common import *
import graphics
from physics import Physics
from particle import *

physicsHandler = Physics.__singleton__()

for x in range(1, 6):
    physicsHandler.addParticleToGrid(Sand(Vector2(x, x), Color3(255, 202, 105, 255)))

def onAppStart(app):
    app.mouseX = 0
    app.mouseY = 0

def redrawAll(app):
    graphics.renderBackground()
    graphics.renderGame(app)

def onStep(app):
    physicsHandler.tickAllParticles()

def onMouseMove(app, mouseX, mouseY):
    app.mouseX = mouseX
    app.mouseY = mouseY

def onMouseDrag(app, mouseX, mouseY):
    app.mouseX = mouseX
    app.mouseY = mouseY
    
cmu_graphics.runApp(width = graphics.canvasSizeX, height = graphics.canvasSizeY)