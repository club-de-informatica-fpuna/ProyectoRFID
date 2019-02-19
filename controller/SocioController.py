class SocioController:
    
    def __init__(self, socioManager):
        self.socioManager = socioManager

    def listarSocios(self, quantityElements, actualPage):
        return self.socioManager.listarSocios(quantityElements, actualPage)

    def obtenerSocioCi(self, key):
        return self.socioManager.obtenerSocioCi(key)

    def registrarSocio(self, socio):
        return self.socioManager.registrarSocio(socio)

    def eliminarSocioCi(self, ciKey):
        return self.socioManager.eliminarSocioCi(ciKey)

    def obtenerCarrera(self, key):
        return self.socioManager.obtenerCarrera(key)

    def obtenerAlumno(self, key):
        return self.socioManager.obtenerAlumno(key)        

    def actualizarSocioCi(self, socio):
        return self.socioManager.actualizarSocioCi(socio)

    def numberOfPartners(self):
        return self.socioManager.numberOfPartners()