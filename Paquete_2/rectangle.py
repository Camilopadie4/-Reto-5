from .shape import Shape
from .point import Point
from .line import Line

class Rectangle(Shape):
    def __init__(self, vertices: list[Point]):
        if len(vertices) != 4:
            raise ValueError("Un rectangulo debe tener 4 vertices.")
        super().__init__(vertices)
        self.set_is_regular(False)

    def compute_area(self):
        base = self._edges[0].get_length()
        height = self._edges[1].get_length()
        return base * height
class Square(Rectangle):
    def __init__(self, vertices: list[Point]):
        super().__init__(vertices)
        self.set_is_regular(True)
