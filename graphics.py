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
    
    
    drawLabel('Gases',755,435,fill='white',size=20)
    if (app.drawWall1):
        drawRect(50,725,50,50,fill='grey')
    wall=drawRect(720,250,70,70,fill='black',border='white')
    walls=drawLabel('Walls',755,285,fill='white',size=20)
    if (app.drawLiquid1):
        drawRect(50,725,50,50,fill='blue')
    liquid1=drawRect(720,350,70,70,fill='black',border='white')
    drawLabel('liquid',755,385,fill='white',size=20)
physicsSingleton = Physics.__singleton__()
def renderGame(app):
    for p in physicsSingleton.grid.tileArray:
        x = p.pos.x*particleSize
        y = p.pos.y*particleSize
        drawRect(x, y, particleSize, particleSize, fill=p.color.toCMU())