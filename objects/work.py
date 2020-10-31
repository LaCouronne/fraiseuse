from objects.drill import Drill
from objects.barrel import Barrel
from objects.template import Template

from objects.loadable import Loadable


class Work(Loadable):

    def __init__(self, barrel, drill, template):
        assert isinstance(barrel, Barrel)
        assert isinstance(drill, Drill)
        assert isinstance(template, Template)
        self.barrel = barrel
        self.drill = drill
        self.template = template

    def validate(self):
        return True
