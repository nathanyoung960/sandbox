# Handle central game logic

from common import *
import graphics
from physics import Physics, outOfBounds, CollDir, particleSize
from particle import *

physicsHandler = Physics.__singleton__()

def onAppStart(app):
    app.mouseX = 0
    app.mouseY = 0
    app.cursorRadius = 5

    app.setMaxShapeCount(5000)
    b = 5
    s = 30
    for x in range(b, s):
        for y in range(b, s):
            physicsHandler.addParticleToGrid(Sand(Vector2(x, y)))
            
def redrawAll(app):
    graphics.renderBackground(app)
    graphics.renderGame(app)
    
    drawCircle(app.mouseX, app.mouseY, app.cursorRadius*particleSize, fill=None, border="gray")

def onStep(app):
    physicsHandler.tickAllParticles()

def onMouseMove(app, mouseX, mouseY):
    app.mouseX = mouseX
    app.mouseY = mouseY

def onMousePress(app, mouseX, mouseY, button):
    app.mouseX = mouseX
    app.mouseY = mouseY

    if button == 2:
        for x in range(app.cursorRadius):
            for y in range(app.cursorRadius):
                pos = Vector2(x+(mouseX//particleSize), y+(mouseY//particleSize))
                particle = physicsSingleton.getParticleAtPos(pos)
                if (particle != None):
                    particle
    else:
        for x in range(app.cursorRadius):
            for y in range(app.cursorRadius):
                pos = Vector2(x+(mouseX//particleSize), y+(mouseY//particleSize))
                if (not outOfBounds(pos, physicsHandler.grid, CollDir.CENTER)) and (physicsSingleton.getParticleAtPos(pos) == None):
                    physicsHandler.addParticleToGrid(Water(pos))

runApp(width = graphics.canvasSizeX, height = graphics.canvasSizeY)