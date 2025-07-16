FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . /app

# Run the program
CMD ["python", "traffic_light_simulator.py"]

