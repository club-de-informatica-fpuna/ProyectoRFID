import psycopg2
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

    def registrarCarrera(self, carrera):
        query  = "INSERT INTO carreras (denominacion) VALUES (%s)"
        cur = None
        
        try:
            cur = self.conn.cursor()
            cur.execute(query, [carrera.denominacion])
            self.conn.commit()
            cur.close()
            return True
        except (Exception) as error:
            print(error.__str__())
        finally:
            cur.close()
            return False

    def eliminarCarrera(self, idCarrera):
        query = "DELETE FROM carreras WHERE id = %s"
        cur = None

        try:
            cur = self.conn.cursor()
            cur.execute(query, [idCarrera])
            self.conn.commit()
            cur.close()
            return True
        except(Exception) as error:
            print(error.__str__())
        finally:
            cur.close()
            return False

    def actualizarCarrera(self, carrera):
        query  = "UPDATE carreras SET denominacion = %s "
        query += "WHERE id = %s"
        updatedRows = 0
        cur = None
        
        try:
            cur = self.conn.cursor()
            cur.execute(query, [carrera.denominacion, carrera.id])
            updatedRows = cur.rowcount
            self.conn.commit()
            cur.close()
            return updatedRows
        except(Exception, psycopg2.DatabaseError) as error:
            print(error.__str__())
        finally:
            cur.close()
            return updatedRows
        

