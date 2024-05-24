import matplotlib.pyplot as plt
import matplotlib.patches
from .MObject import MObject

class Rectangle(MObject):

    def __init__(self, x, y, width, height, _axes=None):
        super().__init__(_axes)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        rect = matplotlib.patches.Rectangle(
            (self.x, self.y),
            self.width,
            self.height,
            edgecolor='r',
            facecolor='b'
        )
        self.axes.add_patch(rect)
        return self.axes

if __name__ == "__main__":
    a = Rectangle(1, 1, 2, 3)
    a.draw()
    a.show()
