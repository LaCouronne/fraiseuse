import math as math

import numpy as np

import dao
import logging
from PIL import Image


class Fraiseuse:
    def __init__(self, positionMax, positionMin):
        self.position = 0
        self.positionMax = positionMax
        self.positionMin = positionMin


class Chariot:
    def __init__(self, xmax):
        self.position = 0
        self.xMax = xmax

    def deplacement(self, distance, direction):
        if (direction == 0):
            self.position = self.position + distance
        else:
            self.position = self.position + distance


class Fut:
    def __init__(self):
        self.position = 0

    # methode de rotation d'angle fut, dependant de la précision

    def rotation(self, angle):
        self.position = self.position + angle


class Carter:
    def __init__(self):
        self.securite = 0

    def erreur_carter(self):
        self.securite = 1


class Machine:
    def __init__(self, fraiseuse, chariot, fut, carter):
        self.fraiseuse = fraiseuse
        self.chariot = chariot
        self.fut = fut
        self.carter = carter


class Empreinte:
    def __init__(self, diam_fut, hauteur_fut, diam_fraiseuse, x_fenetre, y_fenetre, nb_pose):
        self.diam_fut = float(diam_fut)
        self.diam_fraiseuse = float(diam_fraiseuse)
        self.x_fenetre = float(x_fenetre)
        self.y_fenetre = float(y_fenetre)
        self.nb_pose = int(nb_pose)
        self.hauteur_fut = float(hauteur_fut)
        self.precision = float(diam_fraiseuse / 2)

    def surface(self):
        marge_x = float(1)
        marge_y = float(2)

        longueur = math.pi * self.diam_fut
        logging.info("longueur fut:" + str(longueur))
        logging.info("hauteur" + str(self.hauteur_fut))

        logging.info("Condition a valider: ")
        logging.info(" ( largeur Y fenetre  + 2 marge Y)  < hauteur fut  ")
        logging.info(self.y_fenetre + 2 * marge_y)
        logging.info(self.hauteur_fut)
        conditionY = (self.y_fenetre + 2 * marge_y) < self.hauteur_fut
        logging.info(conditionY)
        logging.info("----------------------------------")
        logging.info(" nb fenetre * ( largeur X fenetre  X 2 marge X)  < longueur fut  ")
        conditionX = (self.nb_pose * (self.x_fenetre + 2 * marge_x) < longueur)
        logging.info(self.nb_pose * (self.x_fenetre + 2 * marge_x))
        logging.info(longueur)
        logging.info("condition x: " + str(conditionX))
        return (longueur, conditionX, conditionY)


# def ecriture_etape_1(precision,d1):

# def ecriture_etape_1():
# def ecriture_etape_1():


def ecriture_instructions(empreinte):
    print(dao.get_specific_parameter_admin())
    precision = empreinte.precision
    nb_colone = int(empreinte.hauteur_fut // precision + 1)
    nb_ligne = int(empreinte.diam_fut * math.pi // precision + 1)

    print("nombre de ligne" + str(nb_ligne))
    print("nb de colonne  " + str(nb_colone))
    lst = [[255] * nb_colone] * nb_ligne
    # print (lst)
    b = 0
    for i in range(0, len(lst)):
        for j in range(0, len(lst[i])):
            b = b + 1

    print(b)
    index = 0
    for j in range(0, int(empreinte.nb_pose)):
        print("Majeur : index" + str(index))
        # premiere partie: haut de l'empreinte
        lst, index = ecriture_horizontale(lst, empreinte, index)
        print("fin motif " + str(j) + " : index" + str(index))
        lst,index = ecriture_verticale(lst,empreinte,index)
        lst,index=ecriture_horizontale(lst,empreinte,index)
        lst,index=ecriture_vide_empreinte(lst,empreinte,index)
    # print(list)

    return lst


# def ecriture_verticale(matrice,empreinte,index):

def ecriture_vide_empreinte(matrice, empreinte, index):
    # 5 mm
    precision = empreinte.precision
    lignes = 5 // precision
    print(lignes)
    print("matrice:")
    for i in range(index, int(index + lignes)):
        matrice[index] = [255 for x in matrice[index]]
        # print(matrice[index])
    return matrice, i


def ecriture_horizontale(matrice, empreinte, index):
    precision = empreinte.precision

    nb_ligne = int((((empreinte.diam_fut * math.pi // empreinte.nb_pose) - empreinte.x_fenetre - 5) / 2) // precision)

    print(precision)
    print("nb lignes " + str(nb_ligne))
    for i in range(index, index + nb_ligne):
        #matrice[i]=[255 if index(x) * precision < empreinte.hauteur_fut or index(x)*precision > empreinte.hauteur_fut-2 else 0 for x in matrice[index]]
        for j in range(0,len(matrice[i])):
            if( j*precision > empreinte.hauteur_fut-2 or j*precision <2):

                matrice[i][j]=255
            else:
                matrice[i][j]=0
        index = index + 1
    return matrice, index


'''
   for j in range(0, len(matrice[i])):
            if (j * precision) < 2:
                matrice[index][j] = 255
            elif (j * precision > empreinte.hauteur_fut * precision - 2):
                matrice[index][j] = 255

            else:
                matrice[index][j] = 150
'''

def ecriture_verticale(matrice,empreinte, index):
    precision = empreinte.precision
    epaisseur =(empreinte.hauteur_fut-empreinte.y_fenetre-4)/2
    #b = y+4
    #c = hauteur fut -4
    #blanc de 0 à 2
    #noir de C-F a
    #blanc milieu
    #noir droit
    #blanc droit de F-2 à F
    nb_ligne = int(empreinte.x_fenetre+5 // precision)
    print(precision)
    print("nb lignes " + str(nb_ligne))
    for i in range(index, index + nb_ligne):
        for j in range(0, len(matrice[i])):
            if (j*precision <2 ):
                matrice[index][j] = 255



            elif(j*precision+2 > empreinte.hauteur_fut):
                matrice[index][j]=255

            elif ((2<j*precision and j*precision < 2 + epaisseur )or (6 +empreinte.y_fenetre+epaisseur )):
            #if (int(j) * precision) < 2:
                pass
             #   matrice[index][j] = 255
            #elif (j * precision > empreinte.hauteur_fut - 2):
             #   matrice[index][j] = 255
            else:
                matrice[index][j] = 0
        index = index + 1
    return matrice, index


def affichage_matrice(matrice, empreinte):
    nb_colone = int(empreinte.hauteur_fut // empreinte.precision + 1)
    nb_ligne = int(empreinte.diam_fut * math.pi // empreinte.precision + 1)
    im = Image.new("RGB", (nb_ligne, nb_colone))
    pix = im.load()
    print(nb_colone)
    print(nb_ligne)
    for i in range(nb_ligne):
        for j in range(nb_colone):
            # matrice[i][j] = matrice[i][j] * 255
            # pix[i, j] = (255, 0, 0)
            logging.info("Ligne n° " + str(j))
    array = np.array(matrice, dtype=np.uint8)

    array2 = np.array(matrice, dtype=np.uint8)
    new_image = Image.fromarray(array2)
    new_image.save('new.png')
    # im.save("test.png", "PNG")


# logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

# diam_fut, hauteur_fut, diam_fraiseuse, x_fenetre, y_fenetre, nb_pose
a = Empreinte(64, 111, 0.5, 45, 100, 3)
carter = Carter()
chariot = Chariot(10)
fraiseuse = Fraiseuse(1, 0)

fut = Fut()
machine = Machine(fraiseuse, chariot, fut, carter)

# a.surface()
#matrice = ecriture_instructions(a)
#affichage_matrice(matrice, a)
