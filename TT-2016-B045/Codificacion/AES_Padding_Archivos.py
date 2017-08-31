from Crypto.Cipher import AES
import base64
from tkinter.filedialog import *
import os

# the block size for the cipher object; must be 16 per FIPS-197
BLOCK_SIZE = 16

# the character used for padding--with a block cipher such as AES, the value
# you encrypt must be a multiple of BLOCK_SIZE in length.  This character is
# used to ensure that your value is always a multiple of BLOCK_SIZE
PADDING = '.'
########################################################### Comienza el cifrado AES ###################################################################

print("---------------------------------------- CIFRADOR AES ------------------------------------------")
print()
print()
# one-liner to sufficiently pad the text to be encrypted
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

# Cifrado/Descifrado de String's
# Cifrado con codificacion base 64/ Padding
EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).decode().rstrip(PADDING)


secret = os.urandom(BLOCK_SIZE) #Se genera una clave aleatoria
print ('Clave Secreta: ',secret)
cipher = AES.new(secret) #Crear el objeto AES
file = ''
file = askopenfile("r")                  ###Dialogo para elegir archivo, y almacena ruta del archivo
contenido = file.read()
file.close()
contenido_bytes= contenido.encode('utf-8')



################################################################ Cifrado AES ###################################################################
encoded = EncodeAES(cipher, contenido)
print ('Mensaje Cifrado:', encoded)


############################################################### Descifrado AES ##################################################################
print("************************************ Descifrado ************************************")
decoded = DecodeAES(cipher, encoded)
print ('Texto Claro:', decoded)