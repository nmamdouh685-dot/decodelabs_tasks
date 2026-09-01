def encrypt_caesar(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_caesar(cipher_text, shift):
    decrypted_text = ""
    for char in cipher_text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def main():
    print("=== DECODELABS - PROJECT 2: CAESAR CIPHER ===")
    
    user_text = input("Enter text to encrypt: ")
    shift_key = int(input("Enter shift number (e.g. 3): "))

    encrypted = encrypt_caesar(user_text, shift_key)
    decrypted = decrypt_caesar(encrypted, shift_key)

    print("\n--- RESULTS ---")
    print(f"Original Text : {user_text}")
    print(f"Encrypted Text: {encrypted}")
    print(f"Decrypted Text: {decrypted}")

if __name__ == "__main__":
    main()