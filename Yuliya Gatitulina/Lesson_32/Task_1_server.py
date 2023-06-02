import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_host = socket.gethostname()
udp_port = 54998
print('starting up on {} port {}'.format(udp_host,udp_port))
sock.bind((udp_host,udp_port))

while True:
	print('waiting for a connection')
	data,addr = sock.recvfrom(1024)
	print('well done', data, addr)





