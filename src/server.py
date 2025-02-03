import socket
import time
import random

# Server setup
HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Server is listening on {HOST}:{PORT}")

    conn, addr = server_socket.accept()
    with conn:
        print(f"Connected by {addr}")
        try:
            while True:
                sensor_data = random.uniform(20.0, 30.0)
                timestamp = time.time()
                message = f"{timestamp},{sensor_data}\n"

                conn.sendall(message.encode('utf-8'))
                time.sleep(1)
        except (BrokenPipeError, ConnectionResetError):
            print("Client disconnected.")
        except Exception as e:
            print(f"Server error: {e}")
