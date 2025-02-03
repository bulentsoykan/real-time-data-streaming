import unittest
from unittest.mock import patch, MagicMock
import matplotlib.pyplot as plt
from client import update  # Replace with actual update function in client.py


class TestClient(unittest.TestCase):

    @patch('client.socket.socket')
    def test_client_data_receiving(self, mock_socket):
        mock_socket.return_value.recv.return_value = b"1633082100.0,25.5\n"
        mock_socket.return_value.decode.return_value = "1633082100.0,25.5"
        
        # Simulate the data received from the server
        data_times = []
        data_values = []
        
        def mock_update(frame):
            data = mock_socket.return_value.recv(1024).decode('utf-8').strip()
            if data:
                timestamp, sensor_value = map(float, data.split(','))
                data_times.append(timestamp)
                data_values.append(sensor_value)
                
                # Check if the data has been processed correctly
                self.assertEqual(data_times, [1633082100.0])
                self.assertEqual(data_values, [25.5])

        mock_update(0)

    @patch('client.socket.socket')
    def test_client_socket_connection(self, mock_socket):
        mock_socket.return_value.connect = MagicMock()
        
        # Assume client connects to the server
        client_thread = threading.Thread(target=client_function)  # Replace with actual client function
        client_thread.daemon = True
        client_thread.start()

        # Check if socket connection is established
        mock_socket.return_value.connect.assert_called_with(('127.0.0.1', 65432))


if __name__ == '__main__':
    unittest.main()
