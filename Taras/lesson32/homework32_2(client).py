import socket


def caesar_decrypt(encrypted_message, key):  # decrypts an encrypted message using the Caesar cipher
    decrypted_message = ""
    for char in encrypted_message:  # each char character in the encrypted message is checked to see if it is a letter
        if char.isalpha():  # if the character is a letter, decryption is performed using the key and the decrypted
            # character is added to the decrypted_message
            if char.isupper():
                decrypted_message += chr((ord(char) - 65 - key) % 26 + 65)
            else:
                decrypted_message += chr((ord(char) - 97 - key) % 26 + 97)
        else:  # if the character is not a letter, then it is added without changes to the decrypted_message
            decrypted_message += char
    return decrypted_message  # the received decrypted message is returned from the function


HOST = '127.0.0.1'
PORT = 12345  # set the values of the HOST and PORT variables to specify the IP address and port on which the connection
# to the server will take place


def run_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:  # a socket is created using (IPv4) and
        # (TCP)
        client_socket.connect((HOST, PORT))  # connect to the server
        key = int(input("Enter the encryption key: "))  # ask the user for the encryption key
        client_socket.sendall(str(key).encode())  # send it to the server
        data = input("Enter data to send: ")  # ask the user for data to send
        client_socket.sendall(data.encode())  # send data to the server in the same way, encoding them
        encrypted_data = client_socket.recv(1024).decode()  # receive encrypted data from the server, decode them to
        # string format and save
        decrypted_data = caesar_decrypt(encrypted_data, key)  # decrypt the data and save them
        print("Encrypted data: ", encrypted_data)  # display encrypted and decrypted data on the screen
        print("Decrypted data: ", decrypted_data)


if __name__ == '__main__':
    run_client()








