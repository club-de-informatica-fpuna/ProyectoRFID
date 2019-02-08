import io
import os
import base64
from PIL import Image

class ConversorImg:

    def __init__(self, pathToImg=''):
        self.pathToImg = pathToImg


    def encodeImg(self):
        img = Image.open(self.pathToImg)
        inMemFile = io.BytesIO()
        img.save(inMemFile, format = img.format)
        # reset file pointer to start
        inMemFile.seek(0)
        imgBytes = inMemFile.read()
        base64Encode = base64.b64encode(imgBytes)
        return base64Encode

    def decodeImg(self, base64Str):
        base64Decode = base64.b64decode(base64Str)
        imgBytes = io.BytesIO(base64Decode)
        img = Image.open(imgBytes)
        #img.show()
        return img

