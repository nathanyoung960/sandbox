# Handle central game logic

from common import *
import graphics
from physics import Physics
from particle import *

physicsHandler = Physics.__singleton__()
graphics.renderBackground()

for x in range(6):
    physicsHandler.addParticleToGrid(Sand(Vector2(x, x), Color3(255, 224, 138, 255)))

def onStep():
    physicsHandler.tickAllParticles()
    graphics.renderGame()

app.width = graphics.canvasSizeX
app.height = graphics.canvasSizeY
cmu_graphics.run()