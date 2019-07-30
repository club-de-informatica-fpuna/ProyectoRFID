class PrestamoController:

    def __init__(self, prestamoManager):
        self.prestamoManager = prestamoManager

    def listarPrestamos(self):
        return self.prestamoManager.listarPrestamos()
    
    def registrarPrestamo(self, prestamo):
        return self.prestamoManager.registrarPrestamo(prestamo)

    def eliminarPrestamo(self, idSpanner):
        return self.prestamoManager.eliminarPrestamo(idSpanner)

    def actualizarPrestamo(self, prestamo):
        return self.prestamoManager.actualizarPrestamo(prestamo)

    def listarPrestamoPaginado(self, pagina, cantElementos):
        return self.prestamoManager.listarPrestamoPaginado(pagina, cantElementos)

    def getCantidadPrestamo(self):
        return self.prestamoManager.getCantidadPrestamo()
    
    def buscarPrestamo(self, fechaPrestamo):
        return self.prestamoManager.buscarPrestamo(fechaPrestamo)

    def obtenerPrestamo(self, ciKey):
        return self.prestamoManager.obtenerPrestamo(ciKey)