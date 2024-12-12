from cmu_graphics import rgb

class Color3:
    def __init__(this, r: int, g: int, b: int, a: int = 255):
        this.r = r*(a/255)
        this.g = g*(a/255)
        this.b = b*(a/255)

    def toCMU(this):
        return rgb(this.r, this.g, this.b)