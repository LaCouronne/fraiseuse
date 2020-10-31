import json
import os
import tinydb

def init_parametre_admin():
    db_admin = tinydb.TinyDB('sauvegardes/admin.json')
    print(db_admin)
    if (db_admin):
        print("okay")
    else:
        print("init db")
        db_admin.insert(
            {
                'Diametre fraiseuse': "0.5",
            }

        )

    return db_admin


#barrel = Barrel(diameter=72., height=112.)
def init_param_barrel():
    db_barrel = tinydb.TinyDB('sauvegardes/barrel.json')
    if (db_barrel):
        print("okay")
    else:
        print("init db")
        db_barrel.insert(
            {
                'Nom fut': "Test",
                'diameter': 72.,
                'height': 112.,
            }

        )
    return db_barrel

# template = Template(height=100., width=35., nb_copy=4)
def init_param_template():
    db_template = tinydb.TinyDB('sauvegardes/template.json')
    if (db_template):
        print("okay")
    else:
        print("init db")
        db_template.insert(
            {
                'Nom fut': "Test, diametre ",
                'height': 100.,
                'width': 35.,
                'nb_copy': 4.,

            }

        )
    return db_template


def ini_db():
    init_param_barrel()
    init_param_template()
    init_parametre_admin()


#Get specific
def get_specific_parameter_admin(nom):
    db_admin = init_parametre_admin()
    recherche = tinydb.Query()
    return db_admin.search(recherche.nom == nom)


def get_specific_parameter_barrel(nom):
    db_barrel = init_param_barrel()
    recherche = tinydb.Query()
    return db_barrel.search(recherche.nom == nom)


def get_specific_parameter_template(nom):
    db_template = init_param_template()
    recherche = tinydb.Query()
    return db_template.search(recherche.nom == nom)


#Get all
def get_all_parameter_admin():
    db_admin = init_parametre_admin()
    return db_admin.all()


def get_all_parameter_barrel():
    db_barrel = init_param_barrel()
    return db_barrel.all()


def get_all_parameter_template():
    db_empreinte = init_param_template()
    return db_empreinte.all()


def update_db_admin(selector, param, updated_value):
    '''
    Test so
    '''
    db_admin = init_parametre_admin()
    print(db_admin)
    Admin = tinydb.Query()

    # db.update({'count': 10}, Fruit.type == 'apple')
    db_admin.update({str(param): int(updated_value)}, Admin.nom == str(selector))


dictionaire = {
    "nom": "parametre3",
    "diametre_fut": "2",
    "hauteur_fut": "2",
    "x_fenetre": "12",
    "y_fenetre": "2",
    "nb_pose": "3"
}

db = init_parametre_admin()
db.all()
ini_db()
print(get_all_parameter_admin())
print("laaaaaa")
print(db.tables())
print(db.__getattr__)
update_db_admin( "adminBasic", "tailleFraise",1)
