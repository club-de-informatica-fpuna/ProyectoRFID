from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *
from entidad.Socio import Socio
from util.ConversorImg import ConversorImg
import os, uuid
class FormSocios:

    def __init__(self, view, title='', update=False, socio=None, alumno=None, carrera=None):
        self.view        = view
        self.title       = title
        self.detailRoute = None
        self.update      = update
        self.socio       = socio
        self.alumno      = alumno
        self.carrera     = carrera

    def build(self):
        self.window = QWidget()
        self.window.setWindowTitle(self.title)
        self.createGridLayout()
        self.center()

    def start(self):
        self.build()
        self.window.show()

    def createGridLayout(self):
        self.pathIcons      = "./view/resources/icons/"
        self.pathResources  = "./view/resources/"
        if not self.update:
            self.layoutPost()
        else:
            self.layoutPut(self.alumno, self.carrera)
        
        

    def layoutPost(self):
        self.layout = QHBoxLayout(self.window)

        verticalLayoutImage      = QVBoxLayout()
        horizontalLayoutButtons  = QHBoxLayout()
        horizontalLayoutSearch   = QHBoxLayout()
        verticalLayoutContent    = QVBoxLayout() 

        self.cameraButton = QPushButton()
        self.cameraButton.setObjectName("botonPrimario")
        self.cameraButton.setIcon(QIcon(self.pathIcons+"camera.png"))
        self.cameraButton.setIconSize(QSize(20,20))
        self.cameraButton.clicked.connect(self.openCamera)

        self.imgButton = QPushButton()
        self.imgButton.setObjectName("upload")
        self.imgButton.setIcon(QIcon(self.pathIcons+"upload.png"))
        self.imgButton.setIconSize(QSize(50,30))
        with open(self.pathResources + "styles.css") as f:
            self.imgButton.setStyleSheet(f.read())
        with open(self.pathResources + "styles.css") as f:
            self.cameraButton.setStyleSheet(f.read())

        lbImgTile = QLabel("Imagen")
        lbImgTile.setStyleSheet("text-align:center;")
        self.lbImg = QLabel()
        self.imageUtil(self.pathResources + "student-img-default.png")

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
        self.inputDate.setDisplayFormat('dd/MM/yyyy')
        
        self.inputFN.setEnabled(False)
        self.inputLN.setEnabled(False)
        self.inputCarrer.setEnabled(False)
        self.inputCI.setFocus(True)

        btnRegistrar = QPushButton("Registrar")
        btnRegistrar.setIcon(QIcon(self.pathIcons+"floppy.png"))
        btnRegistrar.setIconSize(QSize(16,16))
        btnRegistrar.setObjectName("botonPrimario")
        btnRegistrar.clicked.connect(self.postSocio)

        btnCancelar = QPushButton("Cancelar")
        btnCancelar.setIcon(QIcon(self.pathIcons+"cancel.png"))
        btnCancelar.setIconSize(QSize(20,20))
        btnCancelar.setObjectName("cancel")
        btnCancelar.clicked.connect(self.cancel)

        btnSearch = QPushButton("Buscar")
        btnSearch.setObjectName("searchStudent")
        btnSearch.setIcon(QIcon(self.pathIcons+"search.png"))
        btnSearch.setIconSize(QSize(20,20))
        btnSearch.clicked.connect(self.buscarAlumno)

        with open(self.pathResources + "styles.css") as f:
            btnCancelar.setStyleSheet(f.read())
        with open(self.pathResources + "styles.css") as f:
            btnRegistrar.setStyleSheet(f.read())
        with open(self.pathResources + "styles.css") as f:
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
        with open(self.pathResources + "styles.css") as f:
            self.window.setStyleSheet(f.read())

    def layoutPut(self, student, career):
        self.layout = QHBoxLayout(self.window)

        verticalLayoutImage      = QVBoxLayout()
        horizontalLayoutButtons  = QHBoxLayout()
        horizontalLayoutSearch   = QHBoxLayout()
        verticalLayoutContent    = QVBoxLayout() 

        self.cameraButton = QPushButton()
        self.cameraButton.setObjectName("botonPrimario")
        self.cameraButton.setIcon(QIcon(self.pathIcons+"camera.png"))
        self.cameraButton.setIconSize(QSize(20,20))
        self.cameraButton.clicked.connect(self.openCamera)

        self.imgButton = QPushButton()
        self.imgButton.setObjectName("upload")
        self.imgButton.setIcon(QIcon(self.pathIcons+"upload.png"))
        self.imgButton.setIconSize(QSize(50,30))
        with open(self.pathResources + "styles.css") as f:
            self.imgButton.setStyleSheet(f.read())
        with open(self.pathResources + "styles.css") as f:
            self.cameraButton.setStyleSheet(f.read())

        lbImgTile = QLabel("Imagen")
        lbImgTile.setStyleSheet("text-align:center;")
        self.lbImg = QLabel()
        if self.socio.foto is not None:
            self.imageUpdateUtil(self.socio.foto)

        self.imgButton.clicked.connect(self.selectImg)

        ci          = QLabel("C.I.")
        firstName   = QLabel("Nombres")
        lastName    = QLabel("Apellidos")
        careerlb    = QLabel("Carrera")
        uid         = QLabel("UID Tarjeta")
        fechaInsert = QLabel("Fecha Ingreso")
        

        self.inputCI     = QLineEdit()
        self.inputFN     = QLineEdit()
        self.inputLN     = QLineEdit()
        self.inputCareer = QLineEdit()
        self.inputUID    = QLineEdit()
        self.inputDate   = QDateEdit()
        self.selectState = QComboBox()
        self.selectState.addItem("Activo", True)
        self.selectState.addItem("Inactivo", False)                
        self.selectState.setCurrentIndex(0 if self.socio.estado else 1)
        
        self.inputCI.setEnabled(False)
        self.inputFN.setEnabled(False)
        self.inputLN.setEnabled(False)
        self.inputCareer.setEnabled(False)
        self.inputDate.setEnabled(False)

        btnUpdate = QPushButton("Actualizar")
        btnUpdate.setIcon(QIcon(self.pathIcons+"update.png"))
        btnUpdate.setIconSize(QSize(16,16))
        btnUpdate.setObjectName("botonPrimario")
        btnUpdate.clicked.connect(self.putSocio)

        btnCancelar = QPushButton("Cancelar")
        btnCancelar.setIcon(QIcon(self.pathIcons+"cancel.png"))
        btnCancelar.setIconSize(QSize(20,20))
        btnCancelar.setObjectName("cancel")
        btnCancelar.clicked.connect(self.cancel)

        self.inputCI.setText(self.socio.ci)
        self.inputFN.setText(student.nombre)
        self.inputLN.setText(student.apellido)
        self.inputCareer.setText(career.denominacion)
        self.inputUID.setText(self.socio.uid)
        self.inputDate.setDate(self.socio.fechaIngreso)
        
        with open(self.pathResources + "styles.css") as f:
            btnCancelar.setStyleSheet(f.read())
        with open(self.pathResources + "styles.css") as f:
            btnUpdate.setStyleSheet(f.read())

        verticalLayoutImage.addWidget(lbImgTile)
        verticalLayoutImage.addWidget(self.lbImg)
        verticalLayoutImage.addWidget(self.imgButton)
        verticalLayoutImage.addWidget(self.cameraButton)

        horizontalLayoutButtons.addWidget(btnUpdate)
        horizontalLayoutButtons.addWidget(btnCancelar)

        horizontalLayoutSearch.addWidget(self.inputCI)

        verticalLayoutContent.addWidget(ci)
        verticalLayoutContent.addLayout(horizontalLayoutSearch)
        verticalLayoutContent.addWidget(firstName)
        verticalLayoutContent.addWidget(self.inputFN)
        verticalLayoutContent.addWidget(lastName)
        verticalLayoutContent.addWidget(self.inputLN)
        verticalLayoutContent.addWidget(careerlb)
        verticalLayoutContent.addWidget(self.inputCareer)
        verticalLayoutContent.addWidget(uid)
        verticalLayoutContent.addWidget(self.inputUID)
        verticalLayoutContent.addWidget(fechaInsert)
        verticalLayoutContent.addWidget(self.inputDate)
        verticalLayoutContent.addWidget(self.selectState)
        verticalLayoutContent.addLayout(horizontalLayoutButtons)

        self.layout.addLayout(verticalLayoutImage)
        self.layout.addLayout(verticalLayoutContent)

        self.window.setObjectName("ventanaGeneral")
        with open(self.pathResources + "styles.css") as f:
            self.window.setStyleSheet(f.read())

    def selectImg(self):
        pathImg = QFileDialog.getOpenFileName(filter = "Imagenes (*.png *.jpg *.svg *.jpeg)")
        
        self.detailRoute = self.pathResources + "student-img-default.png" if not pathImg[0] else pathImg[0]
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
        ci = self.inputCI.text()
        existencia = self.view.generalController.socioController.verificarExistencia(ci)
        if existencia:
            self.view.mostrarPopup("Aviso", "Detalle", "El socio ya ha sido registrado")
            return
        else:
            uid             = self.inputUID.text()
            photo           = self.pathResources + "student-img-default.png" if self.detailRoute is None else self.detailRoute
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
        qr = self.window.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.window.move(qr.topLeft())
    
    def openCamera(self):
        self.filename = str(uuid.uuid4()) + ".png"
        self.view.mostrarWebcam(self.filename, self.setPhoto)
    
    def setPhoto(self):
        self.detailRoute = self.filename
        self.imageUtil(self.filename)

    def putSocio(self):
        socioUpdate = Socio()
        if self.detailRoute is not None:
            if os.path.exists(self.detailRoute):
                socioUpdate.ci     = self.inputCI.text()
                socioUpdate.foto   = ConversorImg(self.detailRoute).encodeImg()
                socioUpdate.uid    = self.inputUID.text()
                indexSelect        = self.selectState.currentIndex()
                socioUpdate.estado = self.selectState.itemData(indexSelect)
        else:
            socioUpdate.ci     = self.inputCI.text()
            socioUpdate.foto   = self.socio.foto
            socioUpdate.uid    = self.inputUID.text()
            indexSelect        = self.selectState.currentIndex()
            socioUpdate.estado = self.selectState.itemData(indexSelect)
        rest = self.view.generalController.socioController.actualizarSocioCi(socioUpdate)
        
        if rest:
            self.window.destroy()
            self.view.mostrarModuloSocio()
        else:
            self.view.mostrarPopup("Error", "Detalle", "Hubo un error al querer actualizar el socio")
            return

    def imageUpdateUtil(self, img64):
        qImg = QImage.fromData(ConversorImg().decodeImg(img64))
        pixmap = QPixmap.fromImage(qImg)
        pixmapResized = pixmap.scaled(400,300,Qt.KeepAspectRatio)
        self.lbImg.setPixmap(pixmapResized)