from common import *
from grid import GameGrid
from particle import _MetaParticle

canvasSizeX = 800
canvasSizeY = 800
particleSize = 5
#aspectRatio = (canvasSizeX/canvasSizeY)

def renderBackground():
    pass
    drawLine(0, 400, canvasSizeX, 400, fill="black")

def renderGame(app):
    for p in GameGrid.__singleton__().tileArray:
        x1 = p.pos.x*particleSize
        y1 = p.pos.y*particleSize
        drawRect(x1, y1, (x1+particleSize)-x1, (y1+particleSize)-y1, fill=p.color.toCMU())
    
    # /* Render our cursor */
    drawCircle(app.mouseX, app.mouseY, 50, fill=None, border="gray")