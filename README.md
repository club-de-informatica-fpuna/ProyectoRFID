# **Guía de instalación de dependencias del proyecto**

## **Lenguaje de programación**
* **python**: version ^3
> `$ sudo apt-get install python3`

## **Librerías**
* **pyqt5** : **_Librería para manejo de interfaces gráficas_**
* **psycopg2** : **_Librería para manejo de la base de datos_**
* **cv2** : **_Librería para el manejo de cámaras_**
* **PIL** : **_Librería para procesamiento de imágenes_**

## **Gestor de paquetes**
* **pip3**
> `$ sudo apt-get install python3-pip`

## **Instalación de librerias**
* > `$ pip3 install pyqt5`
* > `$ pip3 install psycopg2`
* > `$ pip3 install opencv-python`
* > `$ pip3 install pillow` 

## **Base de datos**

### **Base de datos local**
> Para instalar de la base de datos de manera local, debemos instalar el motor de base de datos postgres y el gestor pgadmin [guía windows](http://www.ajpdsoft.com/modules.php?name=News&file=print&sid=489), [guía linux](https://ideafalaz.blogspot.com/2016/04/instalar-postgresql-y-pgadmin-en-linux.html),
luego crear la base de datos **rfid** y en ella ejecutar el query que crea las tablas y relaciones [create-rfid-tables-2.sql](https://drive.google.com/open?id=1F9DX2p54mAXQUaiWis6_OJO3OCd0F0JA), una vez creada la base de datos con las tablas, ya estamos listos para ejecutar el programa, por defecto, al ejecutar la aplicación va a tratar de conectarse a una base de datos local con las siguientes credenciales `user: postgres, password: 12345, host:localhost, port:5432, bd: rfid`, si falla, se tratará de conectar a una base de datos remota, y si vuelve a fallar, se pedirán por teclado los datos para conectarse.  
Por lo cual, para configurar nuestra base de datos local, editamos la función **conexionLocal** del archivo **Manager.py** con los datos correspondientes.

### **Base de datos remota**
> Nuestra base de datos remota solo la utilizarmos en el caso de no querer configurar localmente la base de datos, la cual está alojada en un servidor de [heroku](https://www.heroku.com), el sistema se conectará a la base de datos remota en el único caso de que falle la conexión a la supuesta base de datos local

### **Iniciar la aplicación: python3 Application.py"**
