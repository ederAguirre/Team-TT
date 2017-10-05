import socket
from rsagen import *

gen_rsa()
#instanciamos un objeto para trabajar con el socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

n = int(open("key_n", "r").read())
d = int(open("key_d", "r").read())
 
#Con el metodo bind le indicamos que puerto debe escuchar y de que servidor esperar conexiones
#Es mejor dejarlo en blanco para recibir conexiones externas si es nuestro caso
s.bind(("localhost", 9999))
 
#Aceptamos conexiones entrantes con el metodo listen, y ademas aplicamos como parametro
#El numero de conexiones entrantes que vamos a aceptar
s.listen(1)
 
#Instanciamos un objeto sc (socket cliente) para recibir datos, al recibir datos este 
#devolvera tambien un objeto que representa una tupla con los datos de conexion: IP y puerto
sc, addr = s.accept()
 
 
#Recibimos el mensaje, con el metodo recv recibimos datos y como parametro la cantidad de bytes para recibir
recibido = sc.recv(65536)
x = int(recibido)
#Si se reciben datos nos muestra la IP y el mensaje recibido
print "x: ", x
y = pow(x,d,n)
#Devolvemos el mensaje al cliente
sc.send(str(y))
print "y: ", y

#Cerramos la instancia del socket cliente y servidor
sc.close()
s.close()