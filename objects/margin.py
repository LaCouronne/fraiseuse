from objects.loadable import Loadable


class Margin(Loadable):

    def __init__(self, margin_x, margin_y):
       # assert isinstance(margin_x, float)
       # assert isinstance(margin_y, float)

        self.margin_x = margin_x
        self.margin_y = margin_y
