"""DOCSTRING."""
import socket


def receive():
    """DOCSTRING"""
    host = input("Enter Host: ")
    port = input("Enter Port #: ")

    mySocket = socket.socket()
    mySocket.bind((host, port))

    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print("Connection from: " + str(addr))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected  user: " + str(data))

    conn.close()
