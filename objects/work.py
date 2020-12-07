from objects.drill import Drill
from objects.barrel import Barrel
from objects.template import Template
from objects.motif import Motif


from objects.loadable import Loadable


motif_margin_x = 5.
motif_margin_y = 5.


class Work(Loadable):

    def __init__(self, barrel, drill, template):
        assert isinstance(barrel, Barrel)
        assert isinstance(drill, Drill)
        assert isinstance(template, Template)
        self.barrel = barrel
        self.drill = drill
        self.template = template
        self._matrix = None

    def validate(self):
        if self.template.nb_copy * self.template.width > self.barrel.perimeter:
            return False, \
                   "Il y a une erreur au niveau de la largeur,\n nombre de motif trop élevé ou epaisseur trop grande"
        if self.template.height > self.barrel.height:
            return False, \
                   "Il y a une erreur au niveau de la hauteur,\n les motifs sont plus hhauts que le fut"
        return True, None

    @property
    def matrix(self):
        if self._matrix:
            return self._matrix
        else:
            return self.generate_matrix()

    def generate_matrix(self):

        # Calculate drill/matrix accuracy
        pixel_size = self.drill.diameter / 2

        def round_up(num):
            return num + (num % pixel_size)

        def pixelize(num):
            return int(round_up(num) / pixel_size)

        # Define matrix size
        pixel_height = nb_rows = int(self.barrel.perimeter // pixel_size + 1)
        pixel_width = nb_columns = int(self.barrel.height // pixel_size + 1)

        # Initialize matrix with base values
        default_pixel_value = 255
        matrix = list()
        for row in range(nb_rows):
            matrix.append(list())
            for _ in range(nb_columns):
                matrix[row].append(default_pixel_value)

        # Calculate motif values
        motif_delta = (self.barrel.perimeter / self.template.nb_copy)

        motif_outset_width = motif_delta - motif_margin_y
        motif_outset_height = self.barrel.height - (2 * motif_margin_y)

        # Calculate motif pixelized values
        motif_pixel_margin_x = pixelize(motif_margin_x)
        motif_pixel_margin_y = pixelize(motif_margin_y)
        motif_pixel_delta = pixelize(motif_delta)

        motif_outset_pixel_width = motif_pixel_delta - motif_pixel_margin_x
        motif_outset_pixel_height = pixel_height - (2 * motif_pixel_margin_y)

        motif_padding_pixel_x = pixelize((motif_outset_width - self.template.width) / 2)
        motif_padding_pixel_y = pixelize((motif_outset_height - self.template.height) / 2)

        for index in range(self.template.nb_copy):

            outset_x_start = index * motif_pixel_delta
            outset_x_end = outset_x_start + motif_outset_pixel_width

            outset_y_start = motif_pixel_margin_y
            outset_y_end = outset_y_start + motif_outset_pixel_height

            inset_x_start = outset_x_start + motif_padding_pixel_x
            inset_x_end = outset_x_end - motif_padding_pixel_x

            inset_y_start = outset_y_start + motif_padding_pixel_y
            inset_y_end = outset_y_end - motif_padding_pixel_y

            # Drawing outset (0 = drilling)
            for index_x in range(outset_x_start, outset_x_end):
                for index_y in range(outset_y_start, outset_y_end):
                    matrix[index_x][index_y] = 0

            # Removing inset area (255 = no drilling)
            for index_x in range(inset_x_start, inset_x_end):
                for index_y in range(inset_y_start, inset_y_end):
                    matrix[index_x][index_y] = 255

        self._matrix = matrix
        return matrix

    def save(self):
        pass
