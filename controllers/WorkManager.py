import dao_example as dao


class WorkManager:

    def __init__(self):
        self.admin_conf = None
        self.work_conf = None
        self.get_default_admin_conf()
        self.work_fields=('Longueur','Largeur','Nombre de copies','Diametre fut','Hauteur fut')

    def validate_work(self):
        pass

    @classmethod
    def start_work(cls):
        pass

    @classmethod
    def stop_work(cls):
        pass

    @classmethod
    def get_work_names(cls):
        dao.works.all()

    @classmethod
    def load_work(cls, name):
        pass

    def get_default_admin_conf(self):
        conf = dao.get_default_conf()
        self.admin_conf = conf
