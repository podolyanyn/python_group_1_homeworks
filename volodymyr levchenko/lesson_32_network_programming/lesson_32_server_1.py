import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('127.0.0.1', 5001)
server_socket.bind(server_address)

while True:
    print('Waiting for a message...')
    data, client_address = server_socket.recvfrom(4096)
    print(f'Received data from {client_address}: {data.decode()}')

    # Send a response back to the client
    response = f"Received '{data.decode()}'"
    server_socket.sendto(response.encode(), client_address)
