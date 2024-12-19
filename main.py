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
    app.drawCursor = True
    app.selectedElement = "WATR" # /* SAND, WATR, GLAS */

    graphics.createShapes(app)

    app.setMaxShapeCount(5000)
    b = 5
    s = 30
    for x in range(b, s):
        for y in range(b, s):
            physicsHandler.addParticleToGrid(Sand(Vector2(x, y)))
            
def redrawAll(app):
    graphics.renderBackground(app)
    graphics.renderGame(app)
    
    if (app.drawCursor):
        drawCircle(app.mouseX, app.mouseY, app.cursorRadius*particleSize, fill=None, border="gray")

def onStep(app):
    physicsHandler.tickAllParticles()

def onMouseMove(app, mouseX, mouseY):
    app.mouseX = mouseX
    app.mouseY = mouseY
    if (app.mouseX >= physicsSingleton.grid.extents.x) or (app.mouseY >= physicsSingleton.grid.extents.y):
        app.drawCursor = False
    else:
        app.drawCursor = True

def performCursor(app, mouseX, mouseY, button):
    if button == 2:
        for x in range(app.cursorRadius):
            for y in range(app.cursorRadius):
                pos = Vector2(x+(mouseX//particleSize), y+(mouseY//particleSize))
                particle = physicsSingleton.getParticleAtPos(pos)
                if (particle != None):
                    particle.destroy()
    else:
        for x in range(app.cursorRadius):
            for y in range(app.cursorRadius):
                pos = Vector2(x+(mouseX//particleSize), y+(mouseY//particleSize))
                if (not outOfBounds(pos, physicsSingleton.grid, CollDir.CENTER)) and (physicsSingleton.getParticleAtPos(pos) == None):
                    if (app.selectedElement == "WATR"):
                        physicsHandler.addParticleToGrid(Water(pos))
                    elif (app.selectedElement == "SAND"):
                        physicsHandler.addParticleToGrid(Sand(pos))
                    else:
                        physicsHandler.addParticleToGrid(Glass(pos))

def onMousePress(app, mouseX, mouseY, button):
    app.mouseX = mouseX
    app.mouseY = mouseY
    if (app.sandButton.hits(mouseX,mouseY)):
        app.selectedElement='SAND'
    if (app.waterButton.hits(mouseX,mouseY)):
        app.selectedElement='WATR'
    performCursor(app, mouseX, mouseY, button)
    
def onMouseDrag(app, mouseX, mouseY, buttons):
    app.mouseX = mouseX
    app.mouseY = mouseY
    if (app.drawCursor):
        if (len(buttons) == 1):
            performCursor(app, mouseX, mouseY, buttons[0])

runApp(width = graphics.canvasSizeX, height = graphics.canvasSizeY)