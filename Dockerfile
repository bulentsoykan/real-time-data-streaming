# Use an official lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy project files
COPY requirements.txt .
COPY src/ ./src/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for the server
EXPOSE 65432

# Default command (can be overridden)
CMD ["bash"]