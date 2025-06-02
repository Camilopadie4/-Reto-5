
from .shape import Shape
from .point import Point
from .line import Line

class Triangle(Shape):
    def __init__(self, vertices: list[Point]):
        if len(vertices) != 3:
            raise ValueError("Un triangulo tiene 3 vertices.")
        super().__init__(vertices)

    def compute_area(self):
        a, b, c = [edge.get_length() for edge in self._edges]
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c))**0.5
        return area
class Equilateral(Triangle):
    def __init__(self, vertices: list[Point]):
        super().__init__(vertices)
        self.set_is_regular(True)

class Isosceles(Triangle):
    def __init__(self, vertices: list[Point]):
        super().__init__(vertices)
        self.set_is_regular(False)

class Scalene(Triangle):
    def __init__(self, vertices: list[Point]):
        super().__init__(vertices)
        self.set_is_regular(False)

class RightTriangle(Triangle):
    def __init__(self, vertices: list[Point]):
        super().__init__(vertices)
        self.set_is_regular(False)


