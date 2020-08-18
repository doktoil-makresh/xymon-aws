import os
import sys
import socket
from time import ctime
from collections import defaultdict
from xml.etree import ElementTree
from urllib.request import urlopen
from urllib.parse import urlencode

__version__ = '2.0.0'

class Xymon(object):
    """Communicate with a Xymon server

    server: Hostname or IP address of a Xymon server. Defaults to $XYMSRV
            if set, or 'localhost' if not.
    port:   The port number the server listens on. Defaults to 1984.
    """
    def __init__(self, server=None, port=1984):
        if server is None:
            server = os.environ.get('XYMSRV', 'localhost')
        self.server = server
        self.port = port

    def report(self, host, test, color, message, interval='30m'):
        """Report status to a Xymon server

        host:     The hostname to associate the report with.
        test:     The name of the test or service.
        color:    The color to set. Can be 'green', 'yellow', 'red', or 'clear'
        message:  Details about the current state.
        interval: An optional interval between tests. The status will change
                  to purple if no further reports are sent in this time.
        """
        args = {
            'host': host,
            'test': test,
            'color': color,
            'message': message,
            'interval': interval,
            'date': ctime(),
        }
        report = '''status+{interval} {host}.{test} {color} {date}
{message}'''.format(**args)
        self.send_message(report)

    def data(self, host, test, raw_data):
        """Report data to a Xymon server

        host:     The hostname to associate the report with.
        test:     The name of the test or service.
        data:     The RRD data.
        """
        args = {
            'host': host,
            'test': test,
            'data': raw_data,
        }
        report = '''data {host}.{test}\n{data}'''.format(**args)
        self.send_message(report)

    def send_message(self, message):
        """Report arbitrary information to the server

        See the xymon(1) man page for message syntax.
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            server_ip = socket.gethostbyname(self.server)
            message = message + '\n'
            s.connect((server_ip, self.port))
            s.sendall(message.encode())
        except:
            # Re-raising the exceptions as this should not pass silently.
            raise
        finally:
            s.close()
