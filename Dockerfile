# Use the Debian "light" version as the base image
FROM debian:bullseye-slim

# Update package lists and install necessary packages
RUN apt-get update && apt-get install -y \
    build-essential \
    # gcc-arm-none-eabi \
    python3

# Cleanup to reduce the image size
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Set a working directory (optional)
WORKDIR /app

# You can add additional commands to customize your environment or install more packages if needed

# Define the entry point or default command (optional)
# CMD ["/bin/bash"]
 
