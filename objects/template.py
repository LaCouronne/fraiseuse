
from objects.loadable import Loadable


class Template(Loadable):

    def __init__(self, width, height, nb_copy):
        assert isinstance(width, float)
        assert isinstance(height, float)
        assert isinstance(nb_copy, int)
        self.width = width      # x
        self.height = height    # y
        self.nb_copy = nb_copy  # nb repetitions motifs


