# Program to encrypt a word by shifting characters by a key of +2  Basic Cipher Encryption
# Example: "abc" becomes "cde"
plain_text = input("Enter a word to encrypt (lowercase only): ")
cipher_text = ""

for char in plain_text:
    if char.isalpha():
        # Get ASCII value, add 2, and convert back to character
        new_char = chr(ord(char) + 2)
        cipher_text += new_char
    else:
        cipher_text += char  # Keep spaces or symbols as they are

print(f"Encrypted Text: {cipher_text}")
