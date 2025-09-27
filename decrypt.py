from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization
import base64
import os

# === Try multiple paddings ===
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
    raise ValueError("❌ Decryption failed with all paddings")

# === Load ciphertext depending on extension ===
def load_ciphertext(path):
    if path.endswith(".enc"):  # raw binary file
        with open(path, "rb") as f:
            return f.read()
    else:  # assume Base64-encoded text file
        with open(path, "r") as f:
            b64_cipher = f.read().strip()
        return base64.b64decode(b64_cipher)

def load_and_decrypt(private_key, in_path):
    ciphertext = load_ciphertext(in_path)
    decrypted = try_decrypt(private_key=private_key, ciphertext=ciphertext)
    return decrypted

# === File Lists ===
PERSONS = [
    "./Sharedencryptedfiles/Encrypted-by-Aydeger-for-Vignesh.txt",
    "./Sharedencryptedfiles/Encryptedby-Izzy-for-Vigneshy.txt",
    "./Sharedencryptedfiles/Encryptedby-Marcus_Feliciano-for-vigneshy.txt.enc",
    "./Sharedencryptedfiles/EncryptedBy-Yash-for-Vignesh.txt"
    # "./Sharedencryptedfiles/EncryptedBy-Yash-for-Vignesh.txt",
]

PUBLIC_KEY_FILES = ["./My_keys/Vignesh.pem"] * len(PERSONS)
PRIVATE_KEY_FILES = ["./My_keys/Vignesh_priv.pem"] * len(PERSONS)

# === Load Keys ===
def load_public_key(path):
    with open(path, "rb") as f:
        return serialization.load_pem_public_key(f.read())

def load_private_key(path, password=None):
    with open(path, "rb") as f:
        return serialization.load_pem_private_key(f.read(), password=password)

# === Process Files ===
for person, pub_file, priv_file in zip(PERSONS, PUBLIC_KEY_FILES, PRIVATE_KEY_FILES):
    print(f"\n=== 🔹 Processing {person} ===")
    pub = load_public_key(pub_file)
    priv = load_private_key(priv_file)

    try:
        decrypted = load_and_decrypt(priv, person)
        print(f"🔓 Decrypted Text from {os.path.basename(person)}: {decrypted.decode()}")
    except Exception as e:
        print(f"❌ Failed to decrypt {person}: {e}")
