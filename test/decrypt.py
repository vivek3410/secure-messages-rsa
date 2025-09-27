import base64
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

# 🔹 Load private key
with open("../My_keys/Vignesh_priv.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(f.read(), password=None)

# 🔹 File containing Base64 ciphertext
CIPHERTEXT_FILE = "../Encrypted_Files/EncryptedBy-Vignesh-for-daniel_acosta.txt"

# 🔹 Read ciphertext from file
with open(CIPHERTEXT_FILE, "r") as f:
    b64_ciphertext = f.read()

ciphertext = base64.b64decode(b64_ciphertext)

# 🔹 Decrypt
decrypted_text = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("🔓 Decrypted Plaintext:", decrypted_text.decode())
