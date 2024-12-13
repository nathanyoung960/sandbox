# Handle central game logic

from common import *
import graphics
from physics import Physics
from particle import *

physicsHandler = Physics.__singleton__()

def onAppStart(app):
    app.drawWall1 = False
    app.drawLiquid1=False
    for x in range(6):
        for y in range(6):
            physicsHandler.addParticleToGrid(Sand(Vector2(x, y*2)))

def redrawAll(app):
    graphics.renderBackground(app)
    graphics.renderGame(app)

def onStep(app):
    physicsHandler.tickAllParticles()

def onMousePress(app, mouseX, mouseY):
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
# app.width = graphics.canvasSizeX
# app.height = graphics.canvasSizeY
runApp(width = graphics.canvasSizeX, height = graphics.canvasSizeY)