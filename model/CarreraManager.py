from entidad.Carrera import Carrera

class CarreraManager:

    def __init__(self, conn):
        self.conn = conn
    
    def registrarCarrera(self, carrera):
        pass
    
    def listarCarreras(self):
        query = "SELECT * FROM carreras"
        cur = self.conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        carreras = []
        for row in rows:
            carreras.append(Carrera(row[0], row[1]))
        cur.close()
        return carreras