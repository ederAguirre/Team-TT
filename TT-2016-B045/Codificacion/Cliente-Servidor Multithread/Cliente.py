from random import randint
import socket
import hashlib
import hmac
from rsagen import *
import tkFileDialog
import base64
import os
import Crypto.Cipher.AES, Crypto.Util.Counter
import hmac

#va a mandar mensajes al servidor

def main():
    print "Cliente 1.0"
    
    mensaje =""
    n = int(open("key_n", "r").read())
    e = int(open("key_e", "r").read())
    d = int(open("key_d", "r").read())
    m= ""
    ctext = ''
    plaintext = ''
    content = ''
    filename =''
    host, port = "localhost" , 9999
    #creo un socket y me conecto
    sock= socket.socket()
    sock.connect((host,port))
    
    print "Ingrese un mensaje o salir para terminar"
    while mensaje != "salir":
    	#generamos un numero aleatorio que este dentro de N
        r = randint(0,n)
        ###Dialogo para elegir el archivo a cifrar
        filename = tkFileDialog.asksaveasfilename()
        ##Mandamos la ruta del archivo que se va a realizar el hash, a un archivo .txt para que pueda ser utiilizado por la aplicacion
        rutaAr = open("RutaArchivo.txt","wb")
        rutaAr.write(filename)
        rutaAr.close()
        ##Almacenamos el contenido del arcvhivo que se eligio desde el dialogo
        m = str(open(filename, "rb").read())
        #realizamos un hash del archivo 
        h = int(hashlib.sha256(m).hexdigest(), 16)
        print "h(m): ", h
        x1 = pow(r,e,n)
        x = (h * x1) % n
        print "x: ", x
        f_x = open("x", "w")
        f_x.write(str(x))
        f_x.close()
        mensaje = open("x", "r").read() 


        #intento mandar msj
        try:
            sock.send(mensaje)

        # si no se puede entonces salgo
        except:
            print "no se mando el mensaje"
            mensaje="salir"
        

        recibido = sock.recv(65536)
        print ""
        print "RECIBIDO:  ", recibido
        y = int(recibido)
        print "y: ", y
        rinv = modinv(r,n)
        print "inverso: ", rinv
        z_long = (y * rinv) % n  

        ####### Calculo de llave Z en tamano original
        print "z: ", z_long
        f_z = open("key_z", "w")
        f_z.write(str(z_long))
        f_z.close()
        check = pow(z_long,e,n)
        print "check: ", check
        print "h: ", h % n

        ############ Hash a Llave Z ya que es muy grande Se manda a escribir de nuevo al archivo
        kz = str(open("key_z", "rb").read())
        z = hashlib.sha256(kz).hexdigest()[:16]
        wz =  open("key_z", "w")
        wz.write(str(z))
        wz.close()


        ##################################################################  CIFRADO  #####################################################################
        contentK = open("key_z", "rb").read()
        iv = hmac.new(contentK, m, hashlib.sha256).hexdigest()[:32]  ## Generacion del IV 
        ##Mandamos el vector IV a un archivo .txt para que tambien pueda ser utilizado por el descifrado
        escribeIV = open("vector.txt","wb")
        escribeIV.write(iv)
        escribeIV.close()
        ##Funcion de cifrado
        ctr = Crypto.Util.Counter.new(128, initial_value=long(iv, 16))
        cipher = Crypto.Cipher.AES.new(contentK, Crypto.Cipher.AES.MODE_CTR, counter=ctr)
        ctext = cipher.encrypt(m)
        ##Mandamos el Cifrado a un archivo temporal, dicho archivo es el qe se subira a la nube
        temp_cifrado = open("./tempc", "wb")
        temp_cifrado.write(ctext)
        temp_cifrado.close()
        print ""
        print "Mensaje Cifrado...  "
        
    sock.close() #recuerden cerrar el socket

main()