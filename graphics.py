from common import *
from particle import _MetaParticle
from physics import Physics, particleSize

canvasSizeX = 800
canvasSizeY = 800
#aspectRatio = (canvasSizeX/canvasSizeY)

def renderBackground(app):
    drawRect(0, 0, canvasSizeX, canvasSizeY, fill='black')
    drawLine(0,700,700,700,fill='white')
    drawLine(700,0,700,700,fill='white')
physicsSingleton = Physics.__singleton__()
def renderGame(app):
    for p in physicsSingleton.grid.tileArray:
        x = p.pos.x*particleSize
        y = p.pos.y*particleSize
        drawRect(x, y, particleSize, particleSize, fill=p.color.toCMU())