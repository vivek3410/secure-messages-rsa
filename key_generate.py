
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

# Generate RSA private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# 🔹 Save Private Key as PEM
with open("Vignesh_priv.pem", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,  # or PKCS8
        encryption_algorithm=serialization.NoEncryption()       # no password
    ))

# 🔹 Save Public Key as PEM (with name Vignesh.pem)
public_key = private_key.public_key()
with open("Vignesh.pem", "wb") as f:
    f.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))

print("✅ Keys generated: Vignesh.pem (public) and Vignesh_priv.pem (private)")

# 🔹 Download both files
