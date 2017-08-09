import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast

aleatorio = Random.new().read
Llaves = RSA.generate(2048, aleatorio) #Se generaran el par de llaves

LlavePublica = Llaves.publickey() # Se guarda la llave puclica

#El mensaje debe ser convertido a enteros, no en string


text= 'Hola Mundo 56777'
text_bytes = text.encode('unicode')
Cifrado = LlavePublica.encrypt(text_bytes, 32) #Funcion para cifrar el mensaje con llave pública


print ('Mensaje Cifrado: ',Cifrado)
f = open ('cifrado.txt', 'w')
f.write(str(Cifrado))
f.close()

#descifrado

f = open('cifrado.txt', 'r')
mensaje = f.read()


descifrado = Llaves.decrypt(ast.literal_eval(str(Cifrado)))

print ('Mensaje Descifrado: ', descifrado)

f = open ('cifrado.txt', 'w')
f.write(str(mensaje))
f.write(str(descifrado))
f.close()