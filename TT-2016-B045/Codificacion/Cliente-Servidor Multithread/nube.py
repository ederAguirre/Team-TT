import SocketServer
import threading
import time
from glob import glob

def ls(expr = '*.*'):
    return glob(expr)

                
#creo mi TCP Handler
class MiTcpHandler(SocketServer.BaseRequestHandler):
    
    #sobrescribo la funcion handle
    def handle(self):
        data= ""
        while data != "salir":
            #intento recibir informacion
            try:
                print "**************** Nuevo Cliente Conectado **************** "
                data= self.request.recv(655 36)
                #print data
                hc1 = str(data)
                print "hc1: ", hc1
                temp_cifrado = open("./archivos/hashc1", "wb")
                temp_cifrado.write(hc1)
                temp_cifrado.close()
                print(ls('./archivos/*'))
                #y = pow(x,d,n)
				#Devolvemos el mensaje al cliente
                #print "y: ", y
                #self.request.send(str(y))
                time.sleep(0.1)
			 #espero 0.1 segundos antes de leer neuvamente
            #si hubo un error lo digo y termino el handle
            except:
                print "El cliente D/C o hubo un error"
                data="salir"

#no se assusten Creo una clase llamada ThreadServer
class ThreadServer (SocketServer.ThreadingMixIn, SocketServer.ForkingTCPServer):
    pass

def main():
    #host & port
    host ="localhost"
    port = 9998
    #creo el server
    server = ThreadServer((host,port),MiTcpHandler)
    #creo un thread del server
    server_thread = threading.Thread(target=server.serve_forever)
    #empiezo el thread
    server_thread.start()
    
    print "nube corriendo.."


main()      
