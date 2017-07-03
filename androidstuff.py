"""DOCSTRING."""
import sys
import socket
import android
import androidhelper


class Connection():

    def Transfer(smsdata):
        """DOCSTRING."""
        host = input("Host IP: ")
        port = input("Port: ")

        mySocket = socket.socket()
        mySocket.connect((host, port))

        message = smsdata

        mySocket.send(message.encode())
        data = mySocket.recv(1024).decode()

        print('Received from server: ' + data)

        mySocket.close()


class Search:
    """DOCSTRING."""
    @staticmethod
    def view_all():
        """DOCSTRING."""
        for message in SMSmsgs:
            smsdata = "{}: {}".format(message['address'], message['body'])
            Connection.Transfer(smsdata)

    @staticmethod
    def view_by_address():
        """DOCSTRING."""
        user_requested_address = input("Enter Number: ")
        for message in SMSmsgs:
            if message['address'] == user_requested_address:
                smsdata = "{}: {}".format(message['address'], message['body'])
                Connection.Transfer(smsdata)
        else:
            print("Not found")

    @staticmethod
    def view_by_string():
        """DOCSTRING."""
        user_requested_string = input("Enter Search String: ")
        for message in SMSmsgs:
            if user_requested_string in message['body']:
                smsdata = "{}: {}".format(message['address'], message['body'])
                Connection.Transfer(smsdata)

        else:
            print("Not found")


class Requests:
    """DOCSTRING."""

    @staticmethod
    def decision():
        """DOCSTRING."""
        print("""1. View All\n2. View Specific\n""")
        user_decision = int(input("Enter Selection: "))
        if user_decision == 1:
            Search.view_all()

        elif user_decision == 2:
            print("""1. By Number\n2. By String\n""")
            search_decision = int(input("Enter Selection: "))
            if search_decision == 1:
                Search.view_by_address()

            elif search_decision == 2:
                Search.view_by_string()


def start():
    """DOCSTRING."""
    Requests.decision()


droid = android.Android()
SMSmsgs = droid.smsGetMessages(False, 'inbox').result


start()
