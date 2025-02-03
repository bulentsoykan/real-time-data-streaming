# Real-Time Data Streaming with Python

This project demonstrates real-time data streaming between a server and a client using Python's `socket` library. The server generates sensor data at regular intervals, while the client receives and dynamically visualizes the data using `matplotlib.animation`.

---

## Installation

### Install Dependencies
To install the required Python dependencies, run:
```bash
pip install -r requirements.txt
```

### Run the Server
To start the server, run:
```bash
python src/server.py
```

### Run the Client
To start the client, run:
```bash
python src/client.py
```

---

## Running with Docker

### Build the Docker Image
To build the Docker image, run:
```bash
docker build -t real-time-data-streaming .
```

### Run the Server
To run the server with Docker, execute:
```bash
docker run --rm -p 65432:65432 real-time-data-streaming python src/server.py
```

### Run the Client
To run the client with Docker, execute:
```bash
docker run --rm real-time-data-streaming python src/client.py
```

---

## Running with Docker Compose (Recommended)

### To start both server and client together:
```bash
docker-compose up
```

### To start them separately:
```bash
docker-compose up server
docker-compose up client
```

### To stop the containers:
```bash
docker-compose down
```

---

## Project Structure
```perl
real-time-data-streaming/
│── src/
│   ├── client.py        # Receives and visualizes real-time data
│   ├── server.py        # Generates and sends real-time sensor data
│── docs/
│   ├── README.md        # Project documentation
│── tests/
│   ├── test_server.py   # Unit tests for server
│   ├── test_client.py   # Unit tests for client
│── requirements.txt     # Python dependencies
│── Dockerfile           # Docker setup
│── docker-compose.yml   # Docker Compose configuration
│── .gitignore
│── LICENSE
```

---

## Troubleshooting

### Connection refused?
Ensure the server is running before starting the client.

### No graph appearing?
Check if `matplotlib` is installed:
```bash
pip install matplotlib
```

### Docker issues?
Ensure Docker is running and try rebuilding:
```bash
docker-compose build --no-cache
```

---

## License
This project is licensed under the **MIT License**.

---

## Contributions
Contributions and suggestions are welcome! Feel free to submit an issue or pull request.

---

## Tests

The project includes unit tests for both the server and client.

### Run the Tests
To run the tests, use the following command:
```bash
python -m unittest discover -s tests
```

This will run all the tests in the `tests/` directory, ensuring that the server and client behave as expected.

---

## Test Details

### Server Tests (`test_server.py`)
- **Test Socket Binding**: Ensures that the server binds the socket correctly.
- **Test Data Generation**: Verifies that the server generates and sends sensor data correctly at regular intervals.

### Client Tests (`test_client.py`)
- **Test Socket Connection**: Ensures that the client can successfully connect to the server.
- **Test Data Receiving and Visualization**: Verifies that the client correctly receives and visualizes the real-time data.

