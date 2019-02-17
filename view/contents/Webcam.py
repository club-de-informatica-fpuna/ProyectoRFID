import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2
 
class Webcam:

    def __init__(self, nombreImagen, setPhoto):
        self.nombreImagen = nombreImagen
        self.setPhoto = setPhoto
    
    def start(self):
        self.window = QWidget()
        self.window.setWindowTitle("Webcam viewer")
        self.window.setGeometry(640,480,0,0)
        self.buildWindow()
        self.webcam = cv2.VideoCapture(0)
        self.timer = QTimer(self.window)
        self.timer.timeout.connect(self.show_frame)
        self.timer.start(1)
        self.window.show()

    def show_frame(self):
        ok, img = self.webcam.read()
        if not ok:
            return
        image = QImage(img, img.shape[1], img.shape[0], img.shape[1] * img.shape[2], QImage.Format_RGB888)
        pixmap = QPixmap()
        pixmap.convertFromImage(image.rgbSwapped())
        self.lblWebcam.setPixmap(pixmap)

    def buildWindow(self):
        gridLayout = QVBoxLayout()
        takePhoto = QPushButton("Capturar")
        takePhoto.clicked.connect(self.capturar)
        self.lblWebcam = QLabel()
        self.lblWebcam.setScaledContents(True)
        gridLayout.addWidget(self.lblWebcam)
        gridLayout.addWidget(takePhoto)
        self.window.setLayout(gridLayout)
    
    def capturar(self):
        ok, img = self.webcam.read()
        cv2.imwrite(self.nombreImagen, img)
        self.webcam.release()
        self.setPhoto()
        self.window.destroy()