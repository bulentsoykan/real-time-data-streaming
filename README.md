# Real-Time Data Streaming with Python

This project demonstrates real-time data streaming between a server and a client using Python's `socket` library.  
The server generates sensor data at regular intervals, while the client receives and dynamically visualizes the data using `matplotlib.animation`.  

---

## Installation

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the Server
```bash
python src/server.py
```

### Run the Client
```bash
python src/client.py
```

---

## Running with Docker

### Build the Docker Image
```bash
docker build -t real-time-data-streaming .
```

### Run the Server
```bash
docker run --rm -p 65432:65432 real-time-data-streaming python src/server.py
```

### Run the Client
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
