def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

if __name__ == "__main__":
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (e.g. 3): "))

    encrypted = caesar_encrypt(message, shift)
    decrypted = caesar_decrypt(encrypted, shift)

    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
