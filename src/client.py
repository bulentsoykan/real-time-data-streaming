import socket
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Client setup
HOST = '127.0.0.1'
PORT = 65432

data_times = []
data_values = []
BUFFER_SIZE = 1024

# Set up the plot
fig, ax = plt.subplots()
line, = ax.plot([], [], label='Sensor Data')
ax.set_xlabel('Time')
ax.set_ylabel('Sensor Value')
ax.set_title('Real-Time Sensor Data')
ax.legend()

def update(frame):
    global data_times, data_values
    try:
        data = client_socket.recv(BUFFER_SIZE).decode('utf-8').strip()
        if data:
            timestamp, sensor_value = map(float, data.split(','))
            data_times.append(timestamp)
            data_values.append(sensor_value)

            # Keep only the last 100 data points
            data_times, data_values = data_times[-100:], data_values[-100:]

            # Efficiently update the plot
            line.set_data(data_times, data_values)
            ax.relim()
            ax.autoscale_view()
    except socket.timeout:
        print("No data received, retrying...")
    except Exception as e:
        print(f"Error: {e}")

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        client_socket.settimeout(2)  # Avoid blocking indefinitely

        ani = FuncAnimation(fig, update, interval=1000)
        plt.show()
except ConnectionRefusedError:
    print("Failed to connect to the server. Is it running?")
