
from PIL import Image
import numpy as np

from objects.drill import Drill
from objects.barrel import Barrel
from objects.template import Template


class IHM:

    @staticmethod
    def error(message):
        print('[ERROR] ' + message)


ihm = IHM()


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


def do_work(barrel, drill, template):

    assert isinstance(barrel, Barrel)
    assert isinstance(drill, Drill)
    assert isinstance(template, Template)

    # Check requested work feasibility
    validity = check_motif_validity(template, barrel)

    if not validity:
        ihm.error("requested motif is invalid")

    # Calculate drill/matrix accuracy
    pixel_size = drill.diameter / 2

    # Define matrix size
    nb_rows = int(barrel.perimeter // pixel_size + 1)
    nb_columns = int(barrel.height // pixel_size + 1)

    # Initialize matrix with base values
    default_pixel_value = 255
    matrix = list()
    for row in range(nb_rows):
        matrix.append(list())
        for _ in range(nb_columns):
            matrix[row].append(default_pixel_value)

    # Calculate width between two motif's x position
    motif_delta = barrel.perimeter / template.nb_copy

    # Motif  list setup
    motifs_int = list()

    for index in range(template.nb_copy):

        # Calculate motif x position starting from 0
        pos_x = index * motif_delta + 13

        # Calculate motif y position to center each motif vertically
        pos_y = (barrel.height / 2) - (template.height / 2)

        # Generate motif and motif validator
        motif = Motif(pos_x=pos_x, pos_y=pos_y, template=template)
        motif.set_bool_exp(
            lambda x, y:
            motif.pos_x <= x <= motif.pos_x + motif.template.width and
            motif.pos_y <= y <= motif.pos_y + motif.template.height
        )
        # Add motif to motifs list
        motifs_int.append(motif)

    motifs_ext = list()
    template_ext = Template(motif_delta-5., barrel.height-5., template.nb_copy)

    for index in range(template_ext.nb_copy):

        # Calculate motif x position starting from 0
        pos_x = index * motif_delta + 5

        # Calculate motif y position to center each motif vertically
        pos_y = (barrel.height / 2) - (template_ext.height / 2)

        # Generate motif and motif validator
        motif = Motif(pos_x=pos_x, pos_y=pos_y, template=template_ext)
        motif.set_bool_exp(
            lambda x, y:
            motif.pos_x <= x <= motif.pos_x + motif.template.width and
            motif.pos_y <= y <= motif.pos_y + motif.template.height
        )

        # Add motif to motifs list
        motifs_ext.append(motif)
    # Iterate on each pixel
    for pos_x in range(len(matrix)):
        for pos_y in range(len(matrix[pos_x])):

            # For each pixel, iterate on each motif
            for motif in motifs_ext:

                # If pixel is in a motif, update pixel depth value
                if motif.check_point_in_motif(pos_x * pixel_size, pos_y * pixel_size):
                    matrix[pos_x][pos_y] = 0

            # For each pixel, iterate on each motif
            for motif in motifs_int:

                # If pixel is in a motif, update pixel depth value
                if motif.check_point_in_motif(pos_x * pixel_size, pos_y * pixel_size):
                    matrix[pos_x][pos_y] = 255
    return matrix


def check_motif_validity(template, barrel):
    assert isinstance(template, Template)
    assert isinstance(barrel, Barrel)
    return True


def __main__():
    #barrel = Barrel(diameter=72., height=112.)
    #drill = Drill(diameter=.5)
    #template = Template(height=100., width=35., nb_copy=4)

    barrel = Barrel(diameter=60., height=112.)
    drill = Drill(diameter=.5)
    template = Template(height=100., width=40., nb_copy=3)

    matrix = do_work(barrel=barrel, drill=drill, template=template)
    array2 = np.array(matrix, dtype=np.uint8)
    new_image = Image.fromarray(array2)
    new_image = new_image.transpose(Image.ROTATE_90)    # Rotate 90° due to matrix orientation (top-bottom is x)
    new_image.show()


# __main__()
