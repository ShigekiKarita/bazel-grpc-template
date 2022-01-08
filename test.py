"""Test for gRPC example."""

from contextlib import closing
import os
import socket
import subprocess
import tempfile
import unittest

_BINARY_DIR = os.path.realpath(
    os.path.join(os.path.dirname(os.path.abspath(__file__))))


def find_free_port():
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(('', 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s.getsockname()[1]


class ServerClientTest(unittest.TestCase):

    def test_cc(self):
        port = str(find_free_port())
        client_stdout = tempfile.TemporaryFile(mode='r')
        server_process = subprocess.Popen(
            [os.path.join(_BINARY_DIR, 'cc_server'), port])

        for retry in range(3):
            client_process = subprocess.Popen(
                [os.path.join(_BINARY_DIR, 'cc_client'), port],
                stdout=client_stdout)
            code = client_process.wait()
            client_stdout.seek(0)
            result = client_stdout.read()
            if code == 14:  # server is unavailable
                print("RETRY:", retry, result)
                continue
            self.assertIn("Hello world", result)

        client_stdout.close()
        server_process.terminate()
        server_process.wait()


if __name__ == '__main__':
    unittest.main()
