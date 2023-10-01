# Use the Debian "light" version as the base image
FROM debian:bullseye-slim

# Update package lists and install necessary packages
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

# Set a working directory (optional)
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python packages from requirements.txt
RUN pip3 install -r requirements.txt

# You can add additional commands to customize your environment or install more packages if needed

# Define the entry point or default command (optional)
# CMD ["/bin/bash"]
