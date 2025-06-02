
from .point import Point
from .line import Line
class Shape:
    def __init__(self, vertices: list[Point]):
        self._vertices = vertices
        self._edges = self.compute_edges()
        self._inner_angles = []
        self._is_regular = False
    def get_vertices(self):
        return self._vertices

    def get_edges(self):
        return self._edges

    def get_inner_angles(self):
        return self._inner_angles

    def get_is_regular(self):
        return self._is_regular

    def set_vertices(self, vertices: list[Point]):
        self._vertices = vertices
        self._edges = self.compute_edges()

    def set_is_regular(self, value: bool):
        self._is_regular = value 

    def compute_edges(self):
        edges = []
        for i in range(len(self._vertices)):
            start = self._vertices[i]
            end = self._vertices[(i + 1) % len(self._vertices)]
            edges.append(Line(start, end))
        return edges
    
    def compute_perimeter(self):
        return sum(edge.get_length() for edge in self._edges)

    def compute_inner_angles(self):
        pass  

    def compute_area(self):
        raise NotImplementedError("Este método debe ser aplicado por las subclases.") 