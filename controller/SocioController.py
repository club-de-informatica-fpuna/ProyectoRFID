class SocioController:
    
    def __init__(self, socioManager):
        self.socioManager = socioManager

    def listarSocios(self):
        return self.socioManager.listarSocios()

    def obtenerSocioCi(self, key):
        return self.socioManager.obtenerSocioCi(key)

    def registrarSocio(self, socio):
        return self.socioManager.registrarSocio(socio)

    def eliminarSocioCi(self, ciKey):
        return self.socioManager.eliminarSocioCi(ciKey)

    def obtenerCarrera(self, key):
        return self.socioManager.obtenerCarrera(key)

    def actualizarSocioCi(self, socio):
        return self.socioManager.actualizarSocioCi(socio)