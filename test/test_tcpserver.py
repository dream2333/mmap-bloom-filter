import socket
import sys
from tools import caculate_time


@caculate_time
def test_tcp():
    HOST, PORT = "localhost", 9999
    for i in range(100):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((HOST, PORT))
            sock.sendall("123456789".encode("utf-8"))
            received = bool(sock.recv(1))


def test_tcp_client():
    HOST, PORT = "localhost", 9999
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        sock.connect((HOST, PORT))
        sock.sendall("123456789".encode("utf-8"))
        received = bool(sock.recv(1))
        print(received)
