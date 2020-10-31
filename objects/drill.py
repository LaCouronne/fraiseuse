
from objects.loadable import Loadable


class Drill(Loadable):

    def __init__(self, diameter):
        assert isinstance(diameter, float)
        self.diameter = diameter
