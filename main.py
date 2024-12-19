# Handle central game logic

from common import *
import graphics
from physics import Physics, outOfBounds, CollDir, particleSize
from particle import *

physicsHandler = Physics.__singleton__()

def onAppStart(app):
    app.mouseX = 0
    app.mouseY = 0
    app.cursorRadius = 15
    app.drawWall = False

    app.stepsPerSecond = 15
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

def onMousePress(app, mouseX, mouseY):
    app.mouseX = mouseX
    app.mouseY = mouseY



    for x in range(app.cursorRadius):
        for y in range(app.cursorRadius):
            pos = Vector2(x+(mouseX//particleSize), y+(mouseY//particleSize))
            if (not outOfBounds(pos, physicsHandler.grid, CollDir.CENTER)):
                physicsHandler.addParticleToGrid(Water(pos))

# app.width = graphics.canvasSizeX
# app.height = graphics.canvasSizeY
runApp(width = graphics.canvasSizeX, height = graphics.canvasSizeY)