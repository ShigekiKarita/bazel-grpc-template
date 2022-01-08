"""Test for gRPC example."""

import os
import subprocess
import tempfile
import unittest

_BINARY_DIR = os.path.realpath(
    os.path.join(os.path.dirname(os.path.abspath(__file__))))


class ServerClientTest(unittest.TestCase):

    def test_cc(self):
        with tempfile.TemporaryFile(mode='r') as client_stdout:
            server_process = subprocess.Popen(
                [os.path.join(_BINARY_DIR, 'cc_server')])
            client_process = subprocess.Popen(
                [os.path.join(_BINARY_DIR, 'cc_client')], stdout=client_stdout)
            client_process.wait()
            server_process.terminate()
            client_stdout.seek(0)
            self.assertIn("Hello world", client_stdout.read())


if __name__ == '__main__':
    unittest.main()
