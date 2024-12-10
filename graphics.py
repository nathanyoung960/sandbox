from common import *
from particle import _MetaParticle

canvasSizeX = 800
canvasSizeY = 800
particleSize = 5
#aspectRatio = (canvasSizeX/canvasSizeY)

def renderBackground():
    Rect(0,0,canvasSizeX,canvasSizeY,fill='black')
    Line(0,375,400,375,fill='white')
def renderGame():
    pass

def renderParticle(particleToRender: _MetaParticle):
    Rect(particleToRender.pos.x, particleToRender.pos.y, particleToRender.pos.x+particleSize, particleToRender.pos.y+particleSize, fill=particleToRender.color)