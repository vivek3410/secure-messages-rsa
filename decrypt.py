from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization
import base64

def try_decrypt(private_key, ciphertext):
    paddings = [
        padding.OAEP(
            mgf=padding.MGF1(hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        ),
        padding.OAEP(
            mgf=padding.MGF1(hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=None
        ),
        padding.PKCS1v15()
    ]

    for pad in paddings:
        try:
            return private_key.decrypt(ciphertext, pad)
        except Exception:
            continue
    raise ValueError("Decryption failed with all paddings")


def load_and_decrypt(private_key, in_path):
    with open(in_path, "r") as f:
        b64_cipher = f.read().strip()
    ciphertext = base64.b64decode(b64_cipher)
    decrypted = try_decrypt(private_key=private_key,ciphertext=ciphertext)
    return decrypted


PERSONS = [
    "./Sharedencryptedfiles/Encrypted-by-Aydeger-for-Vignesh.txt",
    "./Sharedencryptedfiles/Encryptedby-Izzy-for-Vigneshy.txt",
    # "Sharedencryptedfiles/Encryptedby-Marcus_Feliciano-for-vigneshy.txt.enc"
    # "./Sharedencryptedfiles/EncryptedBy-Yash-for-Vignesh.txt",
    
]

PUBLIC_KEY_FILES = [
    "./My_keys/Vignesh.pem",
    "./My_keys/Vignesh.pem",
    "./My_keys/Vignesh.pem",
    "./My_keys/Vignesh.pem",
]

PRIVATE_KEY_FILES = [
    "./My_keys/Vignesh_priv.pem",
    "./My_keys/Vignesh_priv.pem",
    "./My_keys/Vignesh_priv.pem",
    "./My_keys/Vignesh_priv.pem",
]

# === Load Keys ===
def load_public_key(path):
    with open(path, "rb") as f:
        return serialization.load_pem_public_key(f.read())

def load_private_key(path, password=None):
    with open(path, "rb") as f:
        return serialization.load_pem_private_key(f.read(),password=password)

for person, pub_file,priv_file in zip(PERSONS, PUBLIC_KEY_FILES,PRIVATE_KEY_FILES):
        print(f"\n=== 🔹 Processing {person} ===")
        pub = load_public_key(pub_file)
        priv = load_private_key(priv_file)

        out_file = person

        # Decrypt from saved file
        decrypted = load_and_decrypt(priv, out_file)
        print(f"🔓 Decrypted Text {person}: ", decrypted.decode())

# for f in files:
#     try:
#         priv = load_private_key(priv_file)
# 
#         decrypted = load_and_decrypt(priv, out_file)
#         # message = decrypt_message(f)
#         print(f"Decrypted message from {f}: {message}\n")
#     except Exception as e:
#         print(f"Failed to decrypt {f}: {e}\n")
