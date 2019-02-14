import psycopg2
from model.CarreraManager import CarreraManager
from model.AlumnoManager import AlumnoManager
from model.SocioManager import SocioManager

class Manager:

    def __init__(self, controller):
        self.PSQL_HOST = "ec2-107-20-183-142.compute-1.amazonaws.com"
        self.PSQL_PORT = "5432"
        self.PSQL_USER = "qdknorzbxmusgh"
        self.PSQL_PASS = "219f081a9ed3403137926ddb0f09a516326818bfb2b2a081ead5b2bedd378f4a"
        self.PSQL_DB = "dvjf688pvmb2i"
        self.controller = controller
    
    def crearConexion(self):
        stringConexion = "host=%s port=%s user=%s password=%s dbname=%s" % (self.PSQL_HOST, self.PSQL_PORT, self.PSQL_USER, self.PSQL_PASS, self.PSQL_DB)
        self.conn = psycopg2.connect(stringConexion)
    
    def iniciar(self):
        self.crearConexion()
        self.carreraManager = CarreraManager(self.conn)
        self.alumnoManager  = AlumnoManager(self.conn)
        self.socioManager   = SocioManager(self.conn)