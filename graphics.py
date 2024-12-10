from common import *
from particle import _MetaParticle

canvasSizeX = 800
canvasSizeY = 800
particleSize = 5
#aspectRatio = (canvasSizeX/canvasSizeY)

def renderBackground(app):
    pass

def renderGame(app):
    pass

def renderParticle(particleToRender: _MetaParticle):
    Rect(particleToRender.pos.x, particleToRender.pos.y, particleToRender.pos.x+particleSize, particleToRender.pos.y+particleSize, fill=particleToRender.color)