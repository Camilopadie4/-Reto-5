from .point import Point
import math

class Line:
    def __init__(self, start_point: Point, end_point: Point):
        self._start_point = start_point
        self._end_point = end_point
        self._length = self.compute_length()

    def get_start_point(self):
        return self._start_point

    def get_end_point(self):
        return self._end_point

    def get_length(self):
        return self._length

    def set_start_point(self, point: Point):
        self._start_point = point
        self._length = self.compute_length()

    def set_end_point(self, point: Point):
        self._end_point = point
        self._length = self.compute_length()

    def compute_length(self):
        return self._start_point.compute_distance(self._end_point) 