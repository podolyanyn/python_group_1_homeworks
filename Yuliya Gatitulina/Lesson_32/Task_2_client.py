import socket

def caesar_encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    key = int(input('key: '))
    text = input('text: ')
    encrypted_text = caesar_encrypt(text, key)
    s.sendall(encrypted_text.encode())
    data = s.recv(1024)

print(f"Received {data!r}")