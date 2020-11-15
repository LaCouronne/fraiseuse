from objects.barrel import Barrel
from objects.drill import Drill
from objects.template import Template
import numpy as np

def read_matrix(matrix):
    drill_depth = 0
    index = 0
    iter_asc = True
    for row in matrix:

        for _ in row:
            pixel_depth = row[index]
            set_depth(min(drill_depth, pixel_depth))
            move_x(1 if iter_asc else -1)
            set_depth(pixel_depth)
            index += 1 if iter_asc else -1

        move_y(1)

        iter_asc = not iter_asc

def set_depth():
    pass


def rotation():
    pass

def move_x(distance,wise):
    pass

def move_y(distance,wise):
    pass

def move_x_init():
    pass

def move_y_init():
    pass


barrel = Barrel(diameter=60., height=112.)
drill = Drill(diameter=.5)
template = Template(height=100., width=40., nb_copy=3)

#matrix = .do_work(barrel=barrel, drill=drill, template=template)
array2 = np.array(matrix, dtype=np.uint8)

read_matrix(array2)

