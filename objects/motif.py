

class Motif:

    def __init__(self, pos_x, pos_y, template):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.template = template
        self.bool_exp = None

    def set_bool_exp(self, bool_exp):
        self.bool_exp = bool_exp

    def check_point_in_motif(self, x, y):
        if not self.bool_exp:
            raise Exception('Motif\'s boolean expression must be set with set_bool_exp in order to define a point\'s '
                            'position relative to the motif')
        return self.bool_exp(x, y)
