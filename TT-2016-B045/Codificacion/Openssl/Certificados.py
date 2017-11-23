#!/usr/bin/env python3


import sys, time, os, argparse

parser = argparse.ArgumentParser(description='''Genera claves publica, privada
y CSR para su firma por parte de una autoridad de certificacion.''')
parser.add_argument('127.0.0.1',
                    help='Dominio para el que generamos las claves y el CSR')
args = parser.parse_args()
dominio = args.dominio  # Esto es UNICODE

# Ver https://cryptography.readthedocs.org/en/latest/x509/tutorial/
# Ver https://cryptography.io/en/latest/x509/reference/#cryptography.x509.CertificateSigningRequestBuilder

from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.x509.oid import NameOID

private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

builder = x509.CertificateSigningRequestBuilder()

builder = builder.subject_name(x509.Name([
        x509.NameAttribute(NameOID.COMMON_NAME, dominio),
    ]))
builder = builder.add_extension(
        x509.BasicConstraints(ca=False, path_length=None), critical=True,
    )
csr = builder.sign(
        private_key, hashes.SHA256(), default_backend()
    )

dominio = "%s-%d" %(dominio, time.time())

with open(dominio+'.key', 'wb') as f :
     os.fchmod(f.fileno(), 0o400)
     f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
             format=serialization.PrivateFormat.TraditionalOpenSSL,
             encryption_algorithm=serialization.NoEncryption(),
        ))

with open(dominio+'.csr', 'wb') as f :
    f.write(csr.public_bytes(serialization.Encoding.PEM))