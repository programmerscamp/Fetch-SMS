"""DOCSTRING."""
import android
import androidhelper
import socket


class Search:
    """DOCSTRING."""
    @staticmethod
    def view_all():
        """DOCSTRING."""
        for message in SMSmsgs:
            print("{}: {}".format(message['address'], message['body']))

    @staticmethod
    def view_by_address():
        """DOCSTRING."""
        user_requested_address = input("Enter Number: ")
        for message in SMSmsgs:
            if message['address'] == user_requested_address:
                print("{}: {}".format(message['address'], message['body']))
            else:
                print("Not found")

    @staticmethod
    def view_by_string():
        """DOCSTRING."""
        user_requested_string = input("Enter Search String: ")
        for message in SMSmsgs:
            if user_requested_string in message['body']:
                print("{}: {}".format(message['address'], message['body']))

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
