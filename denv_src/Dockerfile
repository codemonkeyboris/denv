FROM debian:bullseye-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    # gcc-arm-none-eabi \
    python3 \
    python3-pip \
    unzip \
    procps 

# Install Python packages from requirements.txt
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Install Arduino CLI
RUN apt-get install -y curl && \
    curl -fsSL https://downloads.arduino.cc/arduino-cli/arduino-cli_latest_Linux_64bit.tar.gz | tar -xzC /usr/local/bin && \
    chmod +x /usr/local/bin/arduino-cli


# # Install stm32cubeclt
# # place the file in the same directory as your Dockerfile or within a directory that is included in the build context.
# COPY ./*stm32cubeclt*.zip .
# RUN unzip *stm32cubeclt*.zip
# RUN chmod +x ./*stm32cubeclt*.sh
# # RUN ./*stm32cubeclt*.sh -q -d /opt/st/stm32cubeclt
# RUN yes | ./*stm32cubeclt*.sh -q
# ENV PATH="/opt/st/stm32cubeclt/STM32CubeProgrammer/bin:${PATH}"

# Copy STM32Cube Programmer binaries to /opt
COPY stm32cubeclt /opt/st/stm32cubeclt

# Add STM32Cube Programmer to the PATH
ENV PATH="/opt/st/stm32cubeclt/STM32CubeProgrammer/bin:${PATH}"


# Cleanup to reduce the image size
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app


