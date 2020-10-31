import math

from objects.loadable import Loadable


class Barrel(Loadable):

    def __init__(self, diameter, height):
        assert isinstance(diameter, float), diameter
        assert isinstance(height, float), height
        self.diameter = diameter
        self.height = height
        self.perimeter = self.diameter * math.pi
