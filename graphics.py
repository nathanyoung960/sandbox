from common import *
from particle import _MetaParticle

canvasSizeX = 800
canvasSizeY = 800
particleSize = 5
#aspectRatio = (canvasSizeX/canvasSizeY)

def renderBackground(app):
    drawRect(0, 0, canvasSizeX, canvasSizeY, fill="black")
    drawLine(0,750,800,750,fill='white')

def renderGame(app):
    pass

def renderParticle(particleToRender: _MetaParticle):
    Rect(particleToRender.pos.x, particleToRender.pos.y, particleToRender.pos.x+particleSize, particleToRender.pos.y+particleSize, fill=particleToRender.color)