import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('127.0.0.1', 5001)


message = input("Enter a message: ")

client_socket.sendto(message.encode(), server_address)

data, _ = client_socket.recvfrom(4096)
print(f'Received response: {data.decode()}')

client_socket.close()