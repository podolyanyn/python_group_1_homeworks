import socket


def caesar_encrypt(text, key):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift + key) % 26 + shift)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


def caesar_decrypt(encrypted_text, key):
    return caesar_encrypt(encrypted_text, -key)


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('127.0.0.1', 5002)


key = int(input("Enter the encryption key (integer): "))
message = input("Enter a message: ")

encrypted_message = caesar_encrypt(message, key)

client_socket.sendto(str(key).encode(), server_address)

client_socket.sendto(encrypted_message.encode(), server_address)

data, _ = client_socket.recvfrom(4096)
decrypted_response = caesar_decrypt(data.decode(), key)
print(f'Received encrypted response: {data.decode()}')
print(f'Decrypted response: {decrypted_response}')

client_socket.close()
