from common import *
from particle import _MetaParticle
from physics import Physics, particleSize
from shapes import _Rect

canvasSizeX = 800
canvasSizeY = 800
#aspectRatio = (canvasSizeX/canvasSizeY)

def createShapes(app):
    _Rect(500, 500, 200, 200, fill='white')

def renderBackground(app):
    drawRect(0, 0, canvasSizeX, canvasSizeY, fill='black')
    drawLine(0,700,700,700,fill='white')
    drawLine(700,0,700,700,fill='white')
    
    
    drawRect(200,725,50,50,fill=Color3(0, 0, 0, 255).toCMU())
    drawRect(125,725,50,50,fill=Color3(255, 224, 138, 255).toCMU())
    drawRect(50,725,50,50,fill='blue')

    for shape in createdShapes:
        if (type(shape).__name__ == "_Rect"):
            if (shape.fill != None) and (shape.visible):
                drawRect(shape.x, shape.y, shape.width, shape.height, fill=shape.fill)

physicsSingleton = Physics.__singleton__()
def renderGame(app):
    for p in physicsSingleton.grid.tileArray:
        x = p.pos.x*particleSize
        y = p.pos.y*particleSize
        drawRect(x, y, particleSize, particleSize, fill=p.color.toCMU())