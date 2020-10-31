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
        if self.template.nb_copy * self.template.width > self.barrel.perimeter:
            return False, "Il y a une erreur au niveau de la largeur,\n nombre de motif trop élevé ou epaisseur trop grande"
        if self.template.height > self.barrel.height:
            return False, "Il y a une erreur au niveau de la hauteur,\n les motifs sont plus hhauts que le fut"
        return True, None

