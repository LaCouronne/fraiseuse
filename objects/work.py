from objects.drill import Drill
from objects.barrel import Barrel
from objects.template import Template
from objects.motif import Motif


from objects.loadable import Loadable


motif_spacing_x = 5.
motif_spacing_y = 5.


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

        # Define matrix size
        nb_rows = int(self.barrel.perimeter // pixel_size + 1)
        nb_columns = int(self.barrel.height // pixel_size + 1)

        # Initialize matrix with base values
        default_pixel_value = 255
        matrix = list()
        for row in range(nb_rows):
            matrix.append(list())
            for _ in range(nb_columns):
                matrix[row].append(default_pixel_value)

        # Calculate width between two motif's x position
        motif_delta = self.barrel.perimeter / self.template.nb_copy

        motif_outside_width = motif_delta - motif_spacing_x
        motif_outside_height = self.barrel.height - (motif_spacing_y * 2)

        #
        inset_width = (motif_outside_width - self.template.width) / 2
        inset_height = (self.barrel.height - motif_outside_height) / 2

        # Motif  list setup
        motifs_int = list()

        for index in range(self.template.nb_copy):
            # Calculate motif x position starting from 0
            pos_x = index * motif_delta

            # Calculate motif y position to center each motif vertically
            pos_y = (self.barrel.height - self.template.height) / 2

            # Generate motif and motif validator
            motif = Motif(pos_x=pos_x, pos_y=pos_y, template=self.template)

            def point_validator(x, y):
                return (
                    motif.pos_x <= x <= motif.pos_x + motif.template.width and
                    motif.pos_y <= y <= motif.pos_y + motif.template.height
                ) and not (
                    motif.pos_x + inset_width <= x <= motif.pos_x + motif.template.width - inset_width and
                    motif.pos_y + inset_height <= y <= motif.pos_y + motif.template.height - inset_height
                )

            motif.set_bool_exp(point_validator)
            # Add motif to motifs list
            motifs_int.append(motif)

        # Iterate on each pixel
        for pos_x in range(len(matrix)):
            for pos_y in range(len(matrix[pos_x])):

                # For each pixel, iterate on each motif
                for motif in motifs_int:

                    # If pixel is in a motif, update pixel depth value
                    if motif.check_point_in_motif(pos_x * pixel_size, pos_y * pixel_size):
                        matrix[pos_x][pos_y] = 0

        self._matrix = matrix
        return matrix

    def save(self):
        pass
