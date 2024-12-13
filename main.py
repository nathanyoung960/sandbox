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

    if (mouseX >= 720) and (mouseX <= 790) and (mouseY >= 250) and (mouseY <= 320):
        print("Walls")
        app.drawWall1=True
    else:
        app.drawWall1=False
    if (mouseX >= 720) and (mouseX <= 790) and (mouseY >= 350) and (mouseY <= 420):
        print("Liquids")
        app.drawLiquid1=True
    else:
        app.drawLiquid1=False

    for x in range(app.cursorRadius):
        for y in range(app.cursorRadius):
            pos = Vector2(x+(mouseX//particleSize), y+(mouseY//particleSize))
            if (not outOfBounds(pos, physicsHandler.grid, CollDir.CENTER)):
                physicsHandler.addParticleToGrid(Water(pos))

# app.width = graphics.canvasSizeX
# app.height = graphics.canvasSizeY
runApp(width = graphics.canvasSizeX, height = graphics.canvasSizeY)