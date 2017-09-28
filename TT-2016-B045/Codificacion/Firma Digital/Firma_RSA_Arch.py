 # Firmar
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random


random_generator = Random.new().read
key = RSA.generate(2048, random_generator)
public_key = key.publickey()

#Generando Firma

archivo = open("linux.jpg","r")
contenido = archivo.read()
archivo.close()

#text = '1234567890ABC 888 uio'
text_bytes=contenido.encode('utf-8')
hash = SHA256.new(text_bytes).digest()
signature = key.sign(hash, '')
print('Firma:  ',signature)
print ()



#Verificar firma
#text = '1234567890ABC 888 uio'
text_bytes=contenido.encode('utf-8')
hash = SHA256.new(text_bytes).digest()
print('Comprobando Firma:  ',public_key.verify(hash, signature))
