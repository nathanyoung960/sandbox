from common import rgb

class Color3:
    def __init__(this, r: int, g: int, b: int, a: int):
        this.r = r*round(a/255)
        this.g = g*round(a/255)
        this.b = b*round(a/255)

    def toCMU(this):
        return rgb(this.r, this.g, this.b)