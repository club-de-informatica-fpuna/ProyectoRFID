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

    def listarAlumnoPaginado(self, pagina, cantElementos):
        cur = None
        query = "SELECT * FROM alumnos limit " + str(cantElementos) + " offset " + str(((pagina-1)*cantElementos))
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
        query  = "INSERT INTO alumnos (ci, apellidos, nombres, email, telefono, id_carrera) "
        query += "VALUES (%s, %s, %s, %s, %s, %s)"
        cur = None

        try:
            cur = self.conn.cursor()
            cur.execute(query, [str(alumno.ci), alumno.apellido, alumno.nombre, alumno.email, alumno.telefono, alumno.idCarrera])
            self.conn.commit()
            cur.close()
            return True
        except (psycopg2.IntegrityError) as error:
            traceback.print_exc(file=sys.stdout)            
            self.conn.rollback()
            return "Ya existe un alumno con dicha cédula de identidad"
        except(Exception) as error:
            traceback.print_exc(file=sys.stdout)
            self.conn.rollback()
            return "Ha ocurrido un error inesperado"
        finally:
            cur.close()

    def eliminarAlumno(self, idSpanner):
        query = "DELETE FROM alumnos CASCADE WHERE ci = %s"
        cur = None
        try:
            cur = self.conn.cursor()
            if type(idSpanner) == list:
                for i in idSpanner:
                    try:
                        cur.execute(query, [str(i)])
                    except(Exception) as error:
                        self.conn.rollback()
                        traceback.print_exc(file=sys.stdout)
                        return False
            else:
                cur.execute(query, [str(idSpanner)])
            self.conn.commit()
            cur.close()
            return True
        except(Exception) as error:
            self.conn.rollback()
            traceback.print_exc(file=sys.stdout)
            return False
        finally:
            cur.close()

    def actualizarAlumnos(self, alumno):
        query  = "UPDATE alumnos SET apellidos = %s, nombres = %s, email = %s, telefono = %s, id_carrera = %s "
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
            self.conn.rollback()
            return False
        finally:
            cur.close()
    
    def getCantidadAlumnos(self):
        cur = None        
        query = "SELECT COUNT(ci) FROM alumnos"
        try:
            cur = self.conn.cursor()
            cur.execute(query)
            cant = cur.fetchone()
            cur.close()
            return cant[0]
        except(Exception) as error:
            traceback.print_exc(file=sys.stdout)
            return None
        finally:
            cur.close()        

    def buscarAlumno(self, ci):
        cur = None
        query = "SELECT ci, apellidos, nombres, email, telefono, id_carrera FROM alumnos WHERE ci = '" + str(ci) + "'"
        try:
            cur = self.conn.cursor()
            cur.execute(query)
            row = cur.fetchone()
            cur.close()
            if row is not None:
                alumno = Alumno(row[0], row[1], row[2], row[3], row[4], row[5])
                return alumno
            return None
        except(Exception) as error:
            self.conn.rollback()
            traceback.print_exc(file=sys.stdout)
            return None
        finally:
            cur.close()