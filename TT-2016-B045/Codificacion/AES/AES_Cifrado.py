import base64
import os
import hashlib, Crypto.Cipher.AES, Crypto.Util.Counter
import hmac
import tkFileDialog

##Vaciamos las variables al inicio de la corrida
ctext = ''
plaintext = ''
content = ''
filename =''
key = ''

##Se genera una clave aleatoria de 16 bytes = 128 bits
key = os.urandom(16)



##Escribiendo la Clave Secreta en Archivo.txt
escribeK = open("ClaveSecreta.txt","wb")
escribeK.write(key)
escribeK.close()

##Leer Contenido de la Clave Secreta
contentK = open("ClaveSecreta.txt", "rb").read()


###Dialogo para elegir el archivo a cifrar
filename = tkFileDialog.asksaveasfilename()

##Mandamos la ruta del archivo que se va a descifrar, a un archivo .txt para que pueda ser utiilizado por la aplicacion
rutaAr = open("RutaArchivo.txt","wb")
rutaAr.write(filename)
rutaAr.close()


##Almacenamos el contenido del arcvhivo que se eligio desde el dialogo
content = str(open(filename, "rb").read())


##Creamos el vector de inicializacion para el modo de operacion CTR


iv = hmac.new(contentK, content, hashlib.sha256).hexdigest()[:32]

##Mandamos el vector IV a un archivo .txt para que tambien pueda ser utilizado por el descifrado
escribeIV = open("vector.txt","wb")
escribeIV.write(iv)
escribeIV.close()


##Funcion de cifrado
def cifrado(contentK, content):
  ctr = Crypto.Util.Counter.new(128, initial_value=long(iv, 16))
  cipher = Crypto.Cipher.AES.new(contentK, Crypto.Cipher.AES.MODE_CTR, counter=ctr)
  return cipher.encrypt(content)


def main():
  print "********* Cifrador AES *********"
  ctext = cifrado(contentK,content)

  ##Mandamos el Cifrado a un archivo temporal, dicho archivo es el qe se subira a la nube
  temp_cifrado = open("./tempc", "wb")
  temp_cifrado.write(ctext)
  temp_cifrado.close()

  print "Mensaje Cifrado: ", ctext


##Funcion Main
if __name__ == '__main__':
    main()
