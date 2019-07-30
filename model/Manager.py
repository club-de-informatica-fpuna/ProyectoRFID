import psycopg2
from model.CarreraManager import CarreraManager
from model.AlumnoManager import AlumnoManager
from model.SocioManager import SocioManager
from model.PrestamoManager import PrestamoManager

class Manager:

    def __init__(self, controller):
        self.conexionLocal()
        self.controller = controller
        self.intentosFallidos = 0
    
    def crearConexion(self):
        try:
            stringConexion = "host=%s port=%s user=%s password=%s dbname=%s" % (self.PSQL_HOST, self.PSQL_PORT, self.PSQL_USER, self.PSQL_PASS, self.PSQL_DB)
            self.conn = psycopg2.connect(stringConexion)
        except Exception as e:
            if self.intentosFallidos >= 2:
                print("La conexión ha fallado, ingrese los datos de la base de datos")
                self.PSQL_HOST = str(input("HOST: "))
                self.PSQL_PORT = str(input("PORT: "))
                self.PSQL_USER = str(input("USER: "))
                self.PSQL_PASS = str(input("PASSWORD: "))
                self.PSQL_DB = str(input("DATABASE: "))
                self.crearConexion()
            else:
                if self.PSQL_HOST == "localhost":
                    print("La conexión local ha fallado, conectando a servidor remoto ...")
                    self.intentosFallidos = self.intentosFallidos + 1
                    self.conexionRemota()
                    self.crearConexion()
                else:
                    print("La conexión remota ha fallado, contectado a servidor local ...")
                    self.intentosFallidos = self.intentosFallidos + 1
                    self.conexionLocal()
                    self.crearConexion()
    
    def iniciar(self):
        self.crearConexion()
        self.carreraManager = CarreraManager(self.conn)
        self.alumnoManager  = AlumnoManager(self.conn)
        self.socioManager   = SocioManager(self.conn)
        self.prestamoManager = PrestamoManager(self.conn)
    
    def conexionLocal(self):
        self.PSQL_HOST = "localhost"
        self.PSQL_PORT = "5432"
        self.PSQL_USER = "postgres"
        self.PSQL_PASS = "root"
        self.PSQL_DB = "rfid"

    def conexionRemota(self):
        self.PSQL_HOST = "ec2-107-20-183-142.compute-1.amazonaws.com"
        self.PSQL_PORT = "5432"
        self.PSQL_USER = "qdknorzbxmusgh"
        self.PSQL_PASS = "219f081a9ed3403137926ddb0f09a516326818bfb2b2a081ead5b2bedd378f4a"
        self.PSQL_DB = "dvjf688pvmb2i"
