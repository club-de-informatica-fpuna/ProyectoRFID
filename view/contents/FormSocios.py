from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *
from entidad.Socio import Socio
import os, uuid
class FormSocios:

    def __init__(self, view):
        self.view = view
        self.title = 'Nuevo Socio | CEP'
        self.detailRoute = None

    def build(self):
        self.window = QWidget()
        self.window.setWindowTitle(self.title)
        self.createGridLayout()
        self.center()

    def start(self):
        self.build()
        self.window.show()

    def createGridLayout(self):
        self.layout = QHBoxLayout(self.window)

        verticalLayoutImage      = QVBoxLayout()
        horizontalLayoutButtons  = QHBoxLayout()
        horizontalLayoutSearch   = QHBoxLayout()
        verticalLayoutContent    = QVBoxLayout() 

        pathImgIconUpload   = os.getcwd()+"/view/resources/icons/"
        self.pathImgDefault = os.getcwd()+"/view/resources/student-img-default.png"

        self.cameraButton = QPushButton("Camara")
        self.cameraButton.setObjectName("botonPrimario")
        self.cameraButton.clicked.connect(self.openCamera)

        self.imgButton = QPushButton()
        self.imgButton.setObjectName("upload")
        self.imgButton.setIcon(QIcon(pathImgIconUpload+"upload.png"))
        self.imgButton.setIconSize(QSize(50,30))
        with open('./view/resources/styles.css') as f:
            self.imgButton.setStyleSheet(f.read())
        with open('./view/resources/styles.css') as f:
            self.cameraButton.setStyleSheet(f.read())

        lbImgTile = QLabel("Imagen")
        lbImgTile.setStyleSheet("text-align:center;")
        self.lbImg = QLabel()
        self.imageUtil(self.pathImgDefault)

        self.imgButton.clicked.connect(self.selectImg)

        ci          = QLabel("C.I.")
        firstName   = QLabel("Nombres")
        lastName    = QLabel("Apellidos")
        career      = QLabel("Carrera")
        uid         = QLabel("UID Tarjeta")
        fechaInsert = QLabel("Fecha Ingreso")
        

        self.inputCI     = QLineEdit()
        self.inputFN     = QLineEdit()
        self.inputLN     = QLineEdit()
        self.inputCarrer = QLineEdit()
        self.inputUID    = QLineEdit()
        self.inputDate   = QDateEdit(QDate.currentDate())
        #cal = QCalendarWidget()
        self.inputDate.setDisplayFormat('dd/MM/yyyy')
        
        self.inputFN.setEnabled(False)
        self.inputLN.setEnabled(False)
        self.inputCarrer.setEnabled(False)
        self.inputCI.setFocus()

        btnRegistrar = QPushButton("Registrar")
        btnRegistrar.setObjectName("botonPrimario")
        btnRegistrar.clicked.connect(self.postSocio)

        btnCancelar = QPushButton("Cancelar")
        btnCancelar.setIcon(QIcon(pathImgIconUpload+"cancel.png"))
        btnCancelar.setIconSize(QSize(20,20))
        btnCancelar.setObjectName("cancel")
        btnCancelar.clicked.connect(self.cancel)

        btnSearch = QPushButton("Buscar")
        btnSearch.setObjectName("searchStudent")
        btnSearch.setIcon(QIcon(pathImgIconUpload+"search.png"))
        btnSearch.setIconSize(QSize(20,20))
        btnSearch.clicked.connect(self.buscarAlumno)

        with open('./view/resources/styles.css') as f:
            btnCancelar.setStyleSheet(f.read())
        with open('./view/resources/styles.css') as f:
            btnRegistrar.setStyleSheet(f.read())
        with open('./view/resources/styles.css') as f:
            btnSearch.setStyleSheet(f.read())

        verticalLayoutImage.addWidget(lbImgTile)
        verticalLayoutImage.addWidget(self.lbImg)
        verticalLayoutImage.addWidget(self.imgButton)
        verticalLayoutImage.addWidget(self.cameraButton)

        horizontalLayoutButtons.addWidget(btnRegistrar)
        horizontalLayoutButtons.addWidget(btnCancelar)

        horizontalLayoutSearch.addWidget(self.inputCI)
        horizontalLayoutSearch.addWidget(btnSearch)

        verticalLayoutContent.addWidget(ci)
        verticalLayoutContent.addLayout(horizontalLayoutSearch)
        verticalLayoutContent.addWidget(firstName)
        verticalLayoutContent.addWidget(self.inputFN)
        verticalLayoutContent.addWidget(lastName)
        verticalLayoutContent.addWidget(self.inputLN)
        verticalLayoutContent.addWidget(career)
        verticalLayoutContent.addWidget(self.inputCarrer)
        verticalLayoutContent.addWidget(uid)
        verticalLayoutContent.addWidget(self.inputUID)
        verticalLayoutContent.addWidget(fechaInsert)
        verticalLayoutContent.addWidget(self.inputDate)                
        verticalLayoutContent.addLayout(horizontalLayoutButtons)

        self.layout.addLayout(verticalLayoutImage)
        self.layout.addLayout(verticalLayoutContent)

        self.window.setObjectName("ventanaGeneral")
        with open('./view/resources/styles.css') as f:
            self.window.setStyleSheet(f.read())

    def selectImg(self):
        pathImg = QFileDialog.getOpenFileName(filter = "Imagenes (*.png *.jpg *.svg *.jpeg)")
        
        self.detailRoute = self.pathImgDefault if not pathImg[0] else pathImg[0]
        self.imageUtil(self.detailRoute)
        
    
    def buscarAlumno(self):
        ci = self.inputCI.text()
        alumno = self.view.generalController.alumnoController.buscarAlumno(ci)

        if alumno is None:
            return
        else:
            self.inputFN.setText(alumno.nombre)
            self.inputLN.setText(alumno.apellido)
            carrera = self.view.generalController.socioController.obtenerCarrera(ci)
            if carrera is not None:
                self.inputCarrer.setText(carrera.denominacion)

    def postSocio(self):
        ci              = self.inputCI.text()
        uid             = self.inputUID.text()
        photo           = self.pathImgDefault if self.detailRoute is None else self.detailRoute
        dateOfAdmission = self.inputDate.date().toPyDate()
        socio = Socio(uid=uid, ci=ci, foto=photo, fechaIngreso=dateOfAdmission, estado=True)
        response = self.view.generalController.socioController.registrarSocio(socio)
        if response :
            self.window.destroy()
            self.view.mostrarModuloSocio()
        

    def cancel(self):
        self.window.hide()

    def imageUtil(self, pathImg):
        pixMap = QPixmap(pathImg)
        pixmapResized = pixMap.scaled(400, 300, Qt.KeepAspectRatio)
        self.lbImg.setPixmap(pixmapResized)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.window.geometry()      
        self.window.move((screen.width() - size.width()) /2, (screen.height() - size.height()) / 2)
        self.window.setFixedSize(self.window.size())
    
    def openCamera(self):
        self.filename = str(uuid.uuid4()) + ".png"
        self.view.mostrarWebcam(self.filename, self.setPhoto)
    
    def setPhoto(self):
        self.imageUtil(self.filename)