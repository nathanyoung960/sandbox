class Color3:
    def __init__(this, r: int, g: int, b: int, a: int):
        this.r = r*(a/255)
        this.g = g*(a/255)
        this.b = b*(a/255)