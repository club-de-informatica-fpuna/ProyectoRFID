from entidad.Socio import Socio
from entidad.Carrera import Carrera
from entidad.Alumno import Alumno
from util.ConversorImg import ConversorImg
import sys, traceback
from datetime import datetime
from util.Logger import UtilLogger

class SocioManager:

    def __init__(self, conn):
        self.conn = conn
        self.logger = UtilLogger(self.__class__.__name__).get()

    def listarSocios(self, quantityElements, actualPage):
        query  = "SELECT id_socio, uid, ci, foto, fecha_ingreso, estado FROM socios "
        query += "limit %s offset %s"
        cur = None
        socios = []
        try:
            cur = self.conn.cursor()
            since = (actualPage-1)*quantityElements
            cur.execute(query, [quantityElements, since])
            rows = cur.fetchall()
            for column in rows:
                socio = Socio(column[0], column[1], column[2], column[3], column[4], column[5])
                socios.append(socio)
            return socios
        except(Exception) as error:
            print("{} ERROR: {}".format(datetime.now(), error))
            self.logger.error(traceback.format_exc())
            return None
        finally:
            cur.close()
    
    def obtenerSocioCi(self, key):
        query = "SELECT * FROM socios WHERE ci = %s"
        cur = None
        try:
            cur = self.conn.cursor()
            cur.execute(query, [str(key)])
            row = cur.fetchone()
            return Socio(row[0], row[1], row[2], row[3].tobytes(), row[4], row[5])
        except(Exception) as error:
            self.conn.rollback()
            print("{} ERROR: {}".format(datetime.now(), error))
            self.logger.error(traceback.format_exc())
            return None
        finally:
            cur.close()

    def registrarSocio(self, socio):
        query  = "INSERT INTO socios (uid, ci, foto, fecha_ingreso, estado) "
        query += "VALUES (%s, %s, %s, %s, %s)"
        cur = None
        socio.foto = ConversorImg(socio.foto).encodeImg()

        try:
            cur = self.conn.cursor()
            cur.execute(query, [socio.uid, str(socio.ci), socio.foto, socio.fechaIngreso, socio.estado])
            self.conn.commit()
            cur.close()
            return True
        except(Exception) as error:
            print("{} ERROR: {}".format(datetime.now(), error))
            self.logger.error(traceback.format_exc())
            return False
        finally:
            cur.close()

    def eliminarSocioCi(self, ciKey):
        query = "DELETE FROM socios WHERE ci = %s"
        cur = None
        try:
            cur = self.conn.cursor()
            if isinstance(ciKey, list):
                for i in ciKey:
                    try:
                        cur.execute(query, [i])
                    except(Exception) as error:
                        self.conn.rollback()
                        print("{} ERROR: {}".format(datetime.now(), error))
                        self.logger.error(traceback.format_exc())   
            else:
                cur.execute(query, ciKey)

            self.conn.commit()
            cur.close()
            return True
        except(Exception) as error:
            print("{} ERROR: {}".format(datetime.now(), error))
            self.logger.error(traceback.format_exc())
            return False
        finally:
            if cur != None:
                cur.close()

    def obtenerCarrera(self, key):
        query = "SELECT c.id, c.denominacion FROM alumnos a JOIN carreras c ON c.id = a.id_carrera WHERE a.ci = %s"
        cur = None
        try:
            cur = self.conn.cursor()
            cur.execute(query, [str(key)])
            row = cur.fetchone()
            return Carrera(row[0], row[1])
        except(Exception) as error:
            print("{} ERROR: {}".format(datetime.now(), error))
            self.logger.error(traceback.format_exc())
            return False
        finally:
            if cur != None:
                cur.close()

    def obtenerAlumno(self, key):
        query = "SELECT a.nombres, a.apellidos, c.id, c.denominacion FROM alumnos a JOIN carreras c ON c.id = a.id_carrera WHERE a.ci = %s"
        cur = None
        try:
            cur = self.conn.cursor()
            cur.execute(query, [str(key)])
            row = cur.fetchone()
            carrera = Carrera(row[2], row[3])
            alumno = Alumno(nombre=row[0], apellido=row[1], idCarrera=carrera)
            return alumno
        except(Exception) as error:
            print("{} ERROR: {}".format(datetime.now(), error))
            self.logger.error(traceback.format_exc())
            return False
        finally:
            if cur != None:
                cur.close()                

    def actualizarSocioCi(self, socio):
        query  = "UPDATE socios SET "
        updatedRows = 0
        cur = None
        try:
            getSocio = self.obtenerSocioCi(socio.ci)
            missingAttributes = socio.missingAttributes(getSocio)
            query += self.fieldCreator(missingAttributes)
            query += "WHERE ci = %s"
            
            missingValues = self.getMissingValues(socio, missingAttributes)

            if not missingValues :
                return updatedRows
            else:
                missingValues.append(str(socio.ci))
                cur = self.conn.cursor()
                cur.execute(query, missingValues)
                updatedRows = cur.rowcount
                self.conn.commit()
                cur.close()
                return updatedRows
        except(Exception) as error:
            print("{} ERROR: {}".format(datetime.now(), error))
            self.logger.error(traceback.format_exc())
            return updatedRows
        finally:
            if cur != None:
                cur.close()
    
    def fieldCreator(self, fieldList):
        length = len(fieldList)-1
        specialCharacter = " = %s, "
        colums = ""
        for fl in fieldList:
            colums += fl + specialCharacter if fieldList.index(fl) < length else fl + specialCharacter.replace(",", " ")
        return colums
    
    def getMissingValues(self, socio, fieldList):
        missingValues = []
        for field in fieldList:
            missingValues.append(socio.__getattribute__(field))
        return missingValues

    def numberOfPartners(self):
        query = "SELECT COUNT(ID_SOCIO) FROM SOCIOS"
        cur = None
        total = 0
        try:
            cur = self.conn.cursor()
            cur.execute(query)
            total = cur.fetchone()[0]
            cur.close()
            return total
        except(Exception) as error:
            print("{} ERROR: {}".format(datetime.now(), error))
            self.logger.error(traceback.format_exc())
            return total
        finally:
            if cur != None:
                cur.close()

