import psycopg2
from model.CarreraManager import CarreraManager

class Manager:

    def __init__(self, controller):
        self.PSQL_HOST = "localhost"
        self.PSQL_PORT = "5432"
        self.PSQL_USER = "postgres"
        self.PSQL_PASS = "postgres"
        self.PSQL_DB = "rfid"
        self.controller = controller
    
    def crearConexion(self):
        stringConexion = "host=%s port=%s user=%s password=%s dbname=%s" % (self.PSQL_HOST, self.PSQL_PORT, self.PSQL_USER, self.PSQL_PASS, self.PSQL_DB)
        self.conn = psycopg2.connect(stringConexion)
    
    def iniciar(self):
        self.crearConexion()
        self.carreraManager = CarreraManager(self.conn)