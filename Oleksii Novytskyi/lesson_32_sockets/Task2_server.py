import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((UDP_IP, UDP_PORT))

print("UDP сервер запущений і прослуховує порт", UDP_PORT)


while True:
    data, addr = sock.recvfrom(1024)
    print("Отримано повідомлення:", data)
    print("Адреса клієнта:", addr)

    alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    message = 'Hello! The result is OK'
    response = ''

    for i in message.upper():
        spot = alf.find(i)
        new_letter = spot + int(data.decode())
        if i in alf:
            response += alf[new_letter]
        else:
            response += i

    sock.sendto(response.encode(), addr)