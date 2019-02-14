from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *
import os
class FormSocios:

    def __init__(self, view):
        self.view = view
        self.title = 'Nuevo Socio | CEP'

    def build(self):
        self.window = QWidget()
        self.window.setWindowTitle(self.title)
        self.createGridLayout()

    def start(self):
        self.build()
        self.window.show()

    def createGridLayout(self):
        self.layout = QHBoxLayout(self.window)

        verticalLayoutImage      = QVBoxLayout()
        horizontalLayoutButtons  = QHBoxLayout()
        horizontalLayoutSearch   = QHBoxLayout()
        verticalLayoutContent    = QVBoxLayout() 

        labelTitle = QLabel('Registrar Socio')

        pathImgIconSave = os.getcwd()+"/view/resources/icons/upload.png"

        imgButton = QPushButton()
        imgButton.setObjectName("botonPrimario")
        imgButton.setIcon(QIcon(pathImgIconSave))
        imgButton.setIconSize(QSize(50,30))
        with open('./view/resources/styles.css') as f:
            imgButton.setStyleSheet(f.read())


        imgButton.clicked.connect(self.selectImg)

        self.lbImg = QLabel()

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

        btnRegistrar = QPushButton("Registrar")
        btnRegistrar.setObjectName("botonPrimario")

        btnCancelar = QPushButton("Cancelar")
        btnCancelar.setObjectName("botonPrimario")

        btnSearch = QPushButton("Buscar")

        with open('./view/resources/styles.css') as f:
            btnCancelar.setStyleSheet(f.read())
        with open('./view/resources/styles.css') as f:
            btnRegistrar.setStyleSheet(f.read())

        verticalLayoutImage.addWidget(self.lbImg)
        verticalLayoutImage.addWidget(imgButton)

        horizontalLayoutButtons.addWidget(btnRegistrar)
        horizontalLayoutButtons.addWidget(btnCancelar)

        horizontalLayoutSearch.addWidget(self.inputCI)
        horizontalLayoutSearch.addWidget(btnSearch)


        verticalLayoutContent.addWidget(labelTitle)
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
        if not pathImg[0]:
            pathImg = os.getcwd()+"/view/resources/student-img-default.png"

        pixMap = QPixmap(pathImg[0])
        pixmapResized = pixMap.scaled(400, 300, Qt.KeepAspectRatio)
        self.lbImg.setPixmap(pixmapResized)
    


