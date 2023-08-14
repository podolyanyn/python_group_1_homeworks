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



server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('127.0.0.1', 5002)
server_socket.bind(server_address)

while True:
    print('Waiting for a message...')
    data, client_address = server_socket.recvfrom(4096)

    key = int(data.decode())

    data, _ = server_socket.recvfrom(4096)
    encrypted_message = data.decode()

    decrypted_message = caesar_decrypt(encrypted_message, key)
    print(f'Received encrypted message: {encrypted_message}')
    print(f'Decrypted message: {decrypted_message}')

    response = caesar_encrypt(decrypted_message, key)
    server_socket.sendto(response.encode(), client_address)


