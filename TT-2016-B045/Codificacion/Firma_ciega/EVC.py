from random import randint
import socket
import hashlib
import hmac
from rsagen import *
import tkFileDialog


#generamos el par de claves con rsa para el servidor
#gen_rsa()
n = int(open("key_n", "r").read())
e = int(open("key_e", "r").read())
d = int(open("key_d", "r").read())

#generamos un numero aleatorio que este dentro de N
r = randint(0,n)
#print "r: ",r
#rm = r%n
#print "rm: ",rm
#abrimos el mensaje 
###Dialogo para elegir el archivo a cifrar
filename = tkFileDialog.asksaveasfilename()

##Mandamos la ruta del archivo que se va a realizar el hash, a un archivo .txt para que pueda ser utiilizado por la aplicacion
rutaAr = open("RutaArchivo.txt","wb")
rutaAr.write(filename)
rutaAr.close()


##Almacenamos el contenido del arcvhivo que se eligio desde el dialogo
m = str(open(filename, "rb").read())




#m = open("MIB.txt", 'rb').read()
print "m: ", m
#realizamos un hash del archivo 

h = int(hashlib.sha256(m).hexdigest(), 16)


#h = hashlib.sha256(m).hexdigest()
print "h(m): ", h
x1 = pow(r,e,n)
x = (h * x1) % n
print "x: ", x

f_h = open("h(m)", "w")
f_h.write(str(h))
f_h.close()

f_x = open("x", "w")
f_x.write(str(x))
f_x.close()

#Creamos un objeto socket para el servidor.
s = socket.socket()
#Nos conectamos al servidor con el metodo connect. Tiene dos parametros
s.connect(("localhost", 9999))
mensaje = open("x", "r").read()
#Con la instancia del objeto servidor (s) y el metodo send, enviamos el mensaje introducido
s.send(mensaje)

recibido = s.recv(65536)
y = int(recibido)
print "y: ", y

rinv = modinv(r,n)
print "inverso: ", rinv

z = (y * rinv) % n
print "z: ", z
f_z = open("key_z", "w")
f_z.write(str(z))
f_z.close()




check = pow(z,e,n)
print "check: ", check

print "h: ", h % n


#Cerramos la instancia del objeto servidor
s.close()

