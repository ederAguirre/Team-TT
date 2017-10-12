import Crypto.Cipher.AES
import Crypto.Util.Counter

contentK = ""
ctext = ""
iv = ""
ctr=""
plaintext = ""
content = ""
filename = ""
key = ""

##Obtenemos la Clave secreta que se genero en el cifrado
contentK = open("key_z", "rb").read()

##Obtenemos el cifrado del archivo
textcifrado = open("./tempc", "rb").read()

##Obtenemos el contenido del vector IV
iv = open("vector.txt","rb").read()


#Funcion de decifrado
def decifrado(contentK, textcifrado):
  ctr = Crypto.Util.Counter.new(128, initial_value=long(iv, 16))
  cipher = Crypto.Cipher.AES.new(contentK, Crypto.Cipher.AES.MODE_CTR, counter=ctr)
  return cipher.decrypt(textcifrado)

def main():
  plaintext = decifrado(contentK,textcifrado)
  fname=open("RutaArchivo.txt","rb").read()
  print fname
  outf = open(fname, "wb")
  outf.write(plaintext)
  outf.close()
  print "Archivo Descifrado.... "
  #print plaintext



if __name__ == '__main__':
    main()