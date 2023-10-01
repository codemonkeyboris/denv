FROM debian:bullseye-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc-arm-none-eabi \
    python3 \
    python3-pip  # Install pip3

# Install Arduino CLI
RUN apt-get install -y curl && \
    curl -fsSL https://downloads.arduino.cc/arduino-cli/arduino-cli_latest_Linux_64bit.tar.gz | tar -xzC /usr/local/bin && \
    chmod +x /usr/local/bin/arduino-cli

# Cleanup to reduce the image size
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python packages from requirements.txt
COPY requirements.txt .
RUN pip3 install -r requirements.txt
