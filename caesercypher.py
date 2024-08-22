def caesar_cipher(text, shift, mode='encrypt'):
    # Normalize the shift value to be within the range of 0-25
    shift %= 26
    
    if mode == 'decrypt':
        shift = -shift
    
    result = []
    
    for char in text:
        if char.isalpha():
            # Determine the ASCII value of the character
            base = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around using modulo
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(shifted_char)
        else:
            # Non-alphabetic characters remain unchanged
            result.append(char)
    
    return ''.join(result)

# Get user input
message = input("Enter your message: ")
shift_value = int(input("Enter the shift value: "))

# Encrypt the message
encrypted_message = caesar_cipher(message, shift_value, mode='encrypt')
print(f"Encrypted message: {encrypted_message}")

# Decrypt the message
decrypted_message = caesar_cipher(encrypted_message, shift_value, mode='decrypt')
print(f"Decrypted message: {decrypted_message}")
