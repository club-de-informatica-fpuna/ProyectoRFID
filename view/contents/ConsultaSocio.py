from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *
from entidad.Alumno import Alumno
from util.ConversorImg import ConversorImg
import os

class ConsultaSocio:

    def __init__(self, socio, alumno, carrera):
        self.socio = socio
        self.alumno = alumno
        self.carrera = carrera
        self.title = "Ver socio | CEP"
    
    def build(self):
        self.window = QWidget()
        self.window.setWindowTitle(self.title)
        self.createGridLayout()
        self.center()

    def start(self):
        self.build()

    def createGridLayout(self):

        self.layout = QHBoxLayout(self.window)
        self.pathResources ="./view/resources/"

        verticalLayoutData = QVBoxLayout()
        gridLayoutData = QGridLayout()

        self.lbImg = QLabel()
        if self.socio.foto is not None:
            self.imageUtil(self.socio.foto)

        labelNombreApellido = QLabel("Nombre y apellido")
        labelCedula = QLabel("Cedula de identidad")
        labelEmail = QLabel("Email")        
        labelTelefono = QLabel("Teléfono")
        labelCarrera = QLabel("Carrera")
        labelFechaSocio = QLabel("Fecha asociación")
        labelUid = QLabel("UID Tarjeta")
        labelEstado = QLabel("Estado")

        self.inputNombreApellido = QLineEdit()
        self.inputNombreApellido.setObjectName("inputFormDisable")
        self.inputNombreApellido.setEnabled(False)
        self.inputNombreApellido.setText(self.alumno.nombre + ", " + self.alumno.apellido)
        
        self.inputCedula = QLineEdit()
        self.inputCedula.setObjectName("inputFormDisable")
        self.inputCedula.setEnabled(False)
        self.inputCedula.setText(str(self.alumno.ci))

        self.inputEmail = QLineEdit()
        self.inputEmail.setObjectName("inputFormDisable")
        self.inputEmail.setEnabled(False)
        self.inputEmail.setText(self.alumno.email)

        self.inputTelefono = QLineEdit()
        self.inputTelefono.setObjectName("inputFormDisable")
        self.inputTelefono.setEnabled(False)
        self.inputTelefono.setText(self.alumno.telefono)

        self.inputCarrera = QLineEdit()
        self.inputCarrera.setObjectName("inputFormDisable")
        self.inputCarrera.setEnabled(False)   
        self.inputCarrera.setText(self.carrera.denominacion)

        self.inputFecha = QLineEdit()
        self.inputFecha.setObjectName("inputFormDisable")
        self.inputFecha.setEnabled(False)
        self.inputFecha.setText(str(self.socio.fechaIngreso))

        self.inputUID = QLineEdit()
        self.inputUID.setObjectName("inputFormDisable")
        self.inputUID.setEnabled(False)
        self.inputUID.setText(self.socio.uid)

        btnCerrar = QPushButton("Ok")
        btnCerrar.setObjectName("botonSecundario")
        btnCerrar.clicked.connect(self.manejarCancelar)

        with open(self.pathResources + "styles.css") as f:
            btnCerrar.setStyleSheet(f.read())

        shortcutExit = QShortcut(QKeySequence(Qt.Key_Escape), self.window)
        shortcutExit.setContext(Qt.WindowShortcut)
        shortcutExit.activated.connect(self.window.hide)

        gridLayoutData.addWidget(labelNombreApellido,0,0)
        gridLayoutData.addWidget(labelFechaSocio,0,1)
        gridLayoutData.addWidget(self.inputNombreApellido,1,0)
        gridLayoutData.addWidget(self.inputFecha,1,1)
        gridLayoutData.addWidget(labelCedula,2,0)
        gridLayoutData.addWidget(labelUid,2,1)
        gridLayoutData.addWidget(self.inputCedula,3,0)
        gridLayoutData.addWidget(self.inputUID,3,1)
        gridLayoutData.addWidget(labelTelefono,4,0)
        gridLayoutData.addWidget(labelEmail,4,1)
        gridLayoutData.addWidget(self.inputTelefono,5,0)
        gridLayoutData.addWidget(self.inputEmail,5,1)
        gridLayoutData.addWidget(labelCarrera,6,0,1,2)
        gridLayoutData.addWidget(self.inputCarrera,7,0,1,2)
        gridLayoutData.addWidget(btnCerrar,8,0,1,1)
        gridLayoutData.setAlignment(Qt.AlignTop)

        if self.socio.foto is not None:
            self.layout.addWidget(self.lbImg)
        self.layout.addLayout(gridLayoutData)

        self.layout.setAlignment(Qt.AlignTop)
        self.layout.setContentsMargins(20, 20, 20, 20)

        self.window.setObjectName("ventanaPopup")
        with open(self.pathResources + "styles.css") as f:
            self.window.setStyleSheet(f.read())

        self.window.show()

        heightGRID = gridLayoutData.geometry().height()
        pixmap = self.pixmapResized.scaledToHeight(heightGRID)
        self.lbImg.setPixmap(pixmap)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.window.geometry()      
        self.window.move((screen.width() - size.width()) /2, (screen.height() - size.height()) / 2)
    
    def manejarCancelar(self):
        self.window.hide()

    def imageUtil(self, base64):
        qimg = QImage.fromData(ConversorImg().decodeImg(base64))
        self.pixmap = QPixmap.fromImage(qimg)
        self.pixmapResized = self.pixmap.scaledToHeight(220)
        self.lbImg.setPixmap(self.pixmapResized)
