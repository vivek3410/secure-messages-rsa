import base64
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

# 🔹 Load public key
with open("../My_keys/Vignesh.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

# 🔹 Plaintext message to encrypt
plaintext = b"Hello Vignesh, this is a test message!"

# 🔹 Encrypt and save function
def encrypt_and_save(public_key, plaintext, out_path):
    ciphertext = public_key.encrypt(
        plaintext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    # Save Base64 encoded ciphertext to file
    b64_cipher = base64.b64encode(ciphertext).decode()
    with open(out_path, "w") as f:
        f.write(b64_cipher)
    print(f"✅ Encrypted & saved to {out_path}")
    return b64_cipher

# 🔹 Call function
encrypt_and_save(public_key, plaintext, "ciphertext.txt")
