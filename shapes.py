createdShapes = []

class _Rect():
    # /* X and Y are the coordinates for the TOP LEFT CORNER */
    def __init__(this, x: int, y: int, width: int, height: int, fill = None, visible: bool = True):
        this.x = x
        this.y = y
        this.width = width
        this.height = height
        this.fill = fill
        this.visible = visible
        createdShapes.append(this)

    def hits(this, posX: int, posY: int) -> bool:
        if (posX >= this.x) and (posX <= this.x+this.width):
            # /* Passed X check */
            if (posY >= this.y) and (posY <= this.y+this.height):
                # /* Passed Y check */
                return True
        return False