import unittest
from unittest.mock import patch, MagicMock
import socket
import time
import random
import threading
from server import server_function  # Replace with actual function in server.py


class TestServer(unittest.TestCase):

    @patch('server.socket.socket')
    @patch('server.time.sleep', return_value=None)  # Mock sleep to prevent actual delay
    def test_server_data_generation(self, mock_sleep, mock_socket):
        # Mock socket methods
        mock_conn = MagicMock()
        mock_socket.return_value.accept.return_value = (mock_conn, ('127.0.0.1', 65432))

        with patch('random.uniform', return_value=25.5):  # Mock random sensor data
            server_thread = threading.Thread(target=server_function)  # Replace with actual function name
            server_thread.daemon = True
            server_thread.start()

            # Simulate server sending data
            mock_conn.sendall.assert_called_with(b"1633082100.0,25.5\n")

    @patch('server.socket.socket')
    def test_server_socket_binding(self, mock_socket):
        mock_socket.return_value.bind = MagicMock()
        mock_socket.return_value.listen = MagicMock()

        # Assuming `server_function` binds the socket
        server_thread = threading.Thread(target=server_function)  # Replace with actual function name
        server_thread.daemon = True
        server_thread.start()

        # Check if bind and listen are called
        mock_socket.return_value.bind.assert_called_with(('127.0.0.1', 65432))
        mock_socket.return_value.listen.assert_called_once()
        

if __name__ == '__main__':
    unittest.main()
