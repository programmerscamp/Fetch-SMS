"""DOCSTRING."""
import socket


def receive():
    """DOCSTRING"""
    user_host = input("Enter Host: ")
    host = user_host
    user_port = input("Enter Port #: ")
    port = user_port

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
