################################  Elaborado Por: Eder J. Aguirre Cruz


from Crypto.Cipher import AES
from Crypto import Random
from tkinter.filedialog import *



########################################################### Comienza el cifrado AES ###################################################################

print("############################ CIFRADOR AES ###############################")
print()
print()

print("############################ Comienza el Cifrado ###############################")
keyC= input("Introduce la llave (16 Caracteres): ")
iv = Random.new().read(AES.block_size)   ##Creación de Vector de Inicialización
obj = AES.new(keyC, AES.MODE_CBC, iv)    ##Creando Nuevo Objeto para cifrado AES
#filename = askopenfilename()             # ##Dialogo para elegir archivo, y almacena ruta del archivo
file = ''
file = askopenfile("r")
contenido = file.read()
file.close()
contenido_bytes= contenido.encode('utf-8')


################################################################ Cifrado AES ###################################################################


ciphertext=''
ciphertext = obj.encrypt(contenido_bytes)      ##Se almacena mensaje cifrado en variable ciphertext
#print (ciphertext_bytes)


############################################################### Descifrado AES ##################################################################

print("############################ Descifrado ###############################")
keyD= input("Introduce la llave (16 Caracteres): ")
obj2 = AES.new(keyD, AES.MODE_CBC, iv)
plaintext=obj2.decrypt(ciphertext)
print (plaintext)
