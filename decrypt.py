from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization

# Load your private key
with open("./Vignesh_priv.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None
    )

# Function to decrypt a file
def decrypt_message(encrypted_file):
    with open(encrypted_file, "rb") as f:
        ciphertext = f.read()

    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode("utf-8")

# Example: decrypt all 5 received files
files = [
    "Encryptedby-Alice-for-Vignesh.txt",
    "Encryptedby-Bob-for-Vignesh.txt",
    "Encryptedby-Charlie-for-Vignesh.txt",
    "Encryptedby-David-for-Vignesh.txt",
    "Encryptedby-Eve-for-Vignesh.txt"
]

for f in files:
    try:
        message = decrypt_message(f)
        print(f"Decrypted message from {f}: {message}\n")
    except Exception as e:
        print(f"Failed to decrypt {f}: {e}\n")
