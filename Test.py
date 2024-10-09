def encode_char(char, shift):
    # Ensure the character is a lowercase letter
    if char.isalpha() and char.islower():
        # Calculate the new position with wrap-around
        new_position = (ord(char) - ord('a') + shift) % 26
        return chr(ord('a') + new_position)
    return char

def decode_char(char, shift):
    # Ensure the character is a lowercase letter
    if char.isalpha() and char.islower():
        # Calculate the new position with wrap-around
        new_position = (ord(char) - ord('a') - shift) % 26
        return chr(ord('a') + new_position)
    return char

def encode_message(message, rotor_position):
    encoded_message = []
    for i, char in enumerate(message):
        shift = rotor_position + i
        encoded_char = encode_char(char, shift)
        # Skip if the character ends up at the same position as its original
        if encoded_char == char:
            # Increment shift until it changes
            while encoded_char == char:
                shift += 1
                encoded_char = encode_char(char, shift)
        encoded_message.append(encoded_char)
    return ''.join(encoded_message)

def decode_message(encoded_message, rotor_position):
    decoded_message = []
    for i, char in enumerate(encoded_message):
        shift = rotor_position + i
        decoded_char = decode_char(char, shift)
        # Skip if the character ends up at the same position as its original
        if decoded_char == char:
            # Increment shift until it changes
            while decoded_char == char:
                shift -= 1
                decoded_char = decode_char(char, shift)
        decoded_message.append(decoded_char)
    return ''.join(decoded_message)

# การใช้งาน
print("This is Caesar cipher")
message, initial_rotor_position = input("Enter Input : ").split(',')
encoded = encode_message(message, int(initial_rotor_position))
print("Encoded Message:", encoded)
decoded = decode_message(encoded, int(initial_rotor_position))
print("Decoded Message:", decoded)
