# encrypt_decrypt_multi.py
import base64
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

# === CONFIG ===
PRIVATE_KEY_FILES = [
    "./private_keys/daniel_acosta_privkey.pem",
    "./private_keys/IzzyMacDonald_private_key.pem",
    "./private_keys/Marcus_feliciano_privkey.pem",
    "./private_keys/pierson_hendricks_privkey.pem",
    "./private_keys/yash_jani_privkey.pem"
]

PUBLIC_KEY_FILES = [
    "./public_keys/daniel_acosta_pubkey.pem",
    "./public_keys/IzzyMacDonald_public_key.pem",
    "./public_keys/Marcus_feliciano_pubkey.pem",
    "./public_keys/pierson_hendricks_pubkey.pem",
    "./public_keys/yash_jani_pubkey.pem"
]

PERSONS = [
    "daniel_acosta",
    "IzzyMacDonald",
    "Marcus_feliciano",
    "pierson_hendricks",
    "yash_jani"
]

PLAINTEXTS = [
    b"Message for daniel acosta",
    b"Message for IzzyMac Donald",
    b"Message for Marcus feliciano",
    b"Message for pierson hendricks",
    b"Message for yash jani"
]

# === Load Keys ===
def load_public_key(path):
    with open(path, "rb") as f:
        return serialization.load_pem_public_key(f.read())

def load_private_key(path, password=None):
    with open(path, "rb") as f:
        return serialization.load_pem_private_key(f.read(), password=password)

# === Encrypt and save as text file ===
def encrypt_and_save(public_key, plaintext, out_path):
    ciphertext = public_key.encrypt(
        plaintext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    # Save as Base64 in text file
    b64_cipher = base64.b64encode(ciphertext).decode()
    with open(out_path, "w") as f:
        f.write(b64_cipher)
    print(f"✅ Encrypted & saved for {out_path}")
    return b64_cipher

# === Load from file and decrypt ===
def load_and_decrypt(private_key, in_path):
    with open(in_path, "r") as f:
        b64_cipher = f.read()
    ciphertext = base64.b64decode(b64_cipher)
    decrypted = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted

# === Main Flow ===
if __name__ == "__main__":
    for person, pub_file, plaintext in zip(PERSONS, PUBLIC_KEY_FILES, PLAINTEXTS):
        print(f"\n=== 🔹 Processing {person} ===")
        pub = load_public_key(pub_file)
        # priv = load_private_key(priv_file)

        out_file = f"./Encrypted_Files/EncryptedBy-Vignesh-for-{person}.txt"

        # Encrypt & save
        encrypt_and_save(pub, plaintext, out_file)

        print("Plaintext: ", plaintext.decode())

