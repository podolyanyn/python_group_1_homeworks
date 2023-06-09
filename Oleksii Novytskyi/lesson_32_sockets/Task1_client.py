import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = b"hello, server!"

sock.sendto(msg, (UDP_IP, UDP_PORT))

data, addr = sock.recvfrom(1024)

print("Отримано відповідь:", data)
print("Адреса сервера:", addr)