import socket


def caesar_encrypt(message, key):
    encrypted_message = ""
    for char in message:  # each char character from the message is checked to see if it is a letter
        if char.isalpha():  # if the character is a letter, encryption is performed using the key and the encrypted
            # character is added to the encrypted_message
            if char.isupper():
                encrypted_message += chr((ord(char) - 65 + key) % 26 + 65)
            else:
                encrypted_message += chr((ord(char) - 97 + key) % 26 + 97)
        else:  # if the character is not a letter, then it is added without changes to the encrypted_message
            encrypted_message += char
    return encrypted_message  # the received encrypted message is returned from the function


HOST = '127.0.0.1'
PORT = 12345  # set the values of the HOST and PORT variables to specify the IP address and port on which the connection
# to the server will take place


def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:  # a socket is created using (IPv4) and
        # (TCP)
        server_socket.bind((HOST, PORT))  # bind the socket to the IP address and port
        server_socket.listen()  # starts listening for incoming connections
        print(f"The echo server is running on {HOST}:{PORT}")
        while True:  # in an endless loop, waiting for an incoming connection
            client_socket, client_address = server_socket.accept()
            print(f"The connection is established: {client_address}")
            key = int(client_socket.recv(1024).decode())  # receive the encryption key sent by the client, decode the
            # received string into an integer
            data = client_socket.recv(1024).decode()  # receive the encryption data sent by the client, decode the
            # received string into an integer
            encrypted_data = caesar_encrypt(data, key)  # encrypt the received data using the key
            client_socket.sendall(encrypted_data.encode())  # send encrypted data to the client, having previously
            # encoded them
            print("The data has been successfully processed and sent back to the client.")
            client_socket.close()  # close the socket


if __name__ == '__main__':
    run_server()








