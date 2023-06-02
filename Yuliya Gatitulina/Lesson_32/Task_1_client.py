import socket

udp_host = socket.gethostname()
udp_port = 54998

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = b"hello, world"
print('UDP target IP:', udp_host)
print('UDP target Port:', udp_port)
s.sendto(msg.upper(), (udp_host, udp_port))


