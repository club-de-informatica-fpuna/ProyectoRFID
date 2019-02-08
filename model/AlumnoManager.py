import psycopg2
from entidad.Alumno import Alumno
import sys, traceback

class AlumnoManager:
    
    def __init__(self, conn):
        self.conn = conn
    
    def listarAlumno(self):
        cur = None
        query = "SELECT * FROM alumnos"
        alumnos = []
        try:
            cur = self.conn.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            for data in rows:
                alumno = Alumno(data[0], data[1], data[2], data[3], data[4], data[5])
                alumnos.append(alumno)
            cur.close()
            return alumnos
        except(Exception) as error:
            traceback.print_exc(file=sys.stdout)
            return None
        finally:
            cur.close()

    def registrarAlumno(self, alumno):
        query  = "INSERT INTO alumnos (ci, apellidos, nombres, email, telefono, id) "
        query += "VALUES (%s, %s, %s, %s, %s, %s)"
        cur = None

        try:
            cur = self.conn.cursor()
            cur.execute(query, [str(alumno.ci), alumno.apellido, alumno.nombre, alumno.email, alumno.telefono, alumno.idCarrera])
            self.conn.commit()
            cur.close()
            return True
        except(Exception) as error:
            traceback.print_exc(file=sys.stdout)
            return False
        finally:
            cur.close()

    def eliminarAlumno(self, idSpanner):
        query = "DELETE FROM alumnos WHERE ci = %s"
        cur = None

        try:
            cur = self.conn.cursor()
            cur.execute(query, [str(idSpanner)])
            self.conn.commit()
            cur.close()
            return True
        except(Exception) as error:
            traceback.print_exc(file=sys.stdout)
            return False
        finally:
            cur.close()

    def actualizarAlumnos(self, alumno):
        query  = "UPDATE alumnos SET apellidos = %s, nombres = %s, email = %s, telefono = %s, id = %s "
        query += "WHERE ci = %s"
        cur = None

        try:
            cur = self.conn.cursor()
            cur.execute(query, [alumno.apellido, alumno.nombre, alumno.email, alumno.telefono, alumno.idCarrera, str(alumno.ci)])
            self.conn.commit()
            cur.close()
            return True
        except(Exception) as error:
            traceback.print_exc(file=sys.stdout)
            return False
        finally:
            cur.close()
