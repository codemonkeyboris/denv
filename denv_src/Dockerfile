# FROM debian:bullseye-slim

# # Update the package repository and install required packages
# RUN apt-get update -y && apt-get install -y \
#     build-essential \
#     libncursesw5-dev \
#     libgdbm-dev \
#     libc6-dev \
#     zlib1g-dev \
#     libsqlite3-dev \
#     tk-dev \
#     libssl-dev \
#     openssl \
#     libbz2-dev \
#     libreadline-dev \
#     libffi-dev \
#     wget

# # Download Python 3.11 source code
# RUN wget https://www.python.org/ftp/python/3.11.0/Python-3.11.0.tgz

# # Extract the source code
# RUN tar xzf Python-3.11.0.tgz

# # Build and install Python 3.11
# RUN cd Python-3.11.0 && ./configure && make && make install

# # Clean up by removing downloaded source code and temporary files
# RUN rm -rf Python-3.11.0 Python-3.11.0.tgz

# # Check if Python 3.11 is installed successfully
# RUN python3.11 --version



# # Use Ubuntu 22.04 as the base image (update the base image tag once it's available)
# FROM ubuntu:22.04


# # Update the package repository and install necessary packages
# RUN apt-get update && apt-get install -y \
#     wget \
#     && apt-get clean

# # Remove Python 3.10 packages to avoid conflicts
# RUN apt-get remove -y python3.10 python3.10-minimal

# # Install Python 3.11 and related packages
# RUN apt-get install -y \
#     python3.11 \
#     python3.11-dev \
#     python3-pip \
#     && apt-get clean

# # Set the default Python version to 3.11
# RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1

# # Create a symbolic link for pip3
# RUN ln -s /usr/bin/pip3 /usr/bin/pip

# # Update pip and install any additional Python packages you need
# RUN pip install --upgrade pip


# Use Ubuntu 22.04 as the base image (update the base image tag once it's available)
FROM ubuntu:22.04

# FROM debian:bullseye-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    wget \
    libffi-dev \
    libssl-dev \
    zlib1g-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libreadline-dev \
    libsqlite3-dev \
    libgdbm-dev \
    libdb5.3-dev \
    libbz2-dev \
    libexpat1-dev \
    liblzma-dev \
    libffi-dev

WORKDIR /tmp
RUN wget https://www.python.org/ftp/python/3.11.0/Python-3.11.0.tar.xz
RUN tar -xf Python-3.11.0.tar.xz
WORKDIR /tmp/Python-3.11.0
RUN ./configure --enable-optimizations
RUN make -j4
RUN make install

WORKDIR /
RUN rm -rf /tmp/Python-3.11.0
RUN apt-get autoremove -y
RUN apt-get clean

# special way to install pip for python 3.11 (ref https://tecadmin.net/how-to-install-python-3-11-on-ubuntu/)
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11 
COPY ./pythonlibs/requirements.txt .
RUN pip3 install -r requirements.txt





RUN apt-get update && apt-get install -y \
    build-essential \
    gcc-arm-none-eabi \
    udev

# lrzsz


# Install Arduino CLI
RUN apt-get install -y curl && \
    curl -fsSL https://downloads.arduino.cc/arduino-cli/arduino-cli_latest_Linux_64bit.tar.gz | tar -xzC /usr/local/bin && \
    chmod +x /usr/local/bin/arduino-cli


################################################
#  WCH Related
################################################
# This version is too new for WCH chips
# # Install xPack GNU RISC-V Embedded GCC
# RUN mkdir -p /tmp/riscv-gcc
# RUN curl -fsSL https://github.com/xpack-dev-tools/riscv-none-elf-gcc-xpack/releases/download/v13.2.0-2/xpack-riscv-none-elf-gcc-13.2.0-2-linux-x64.tar.gz | tar -xzC /tmp/riscv-gcc
# RUN mv /tmp/riscv-gcc/xpack-riscv-none-elf-gcc-13.2.0-2 /opt
# RUN chmod -R +x /opt/xpack-riscv-none-elf-gcc-13.2.0-2/bin
# ENV PATH="/opt/xpack-riscv-none-elf-gcc-13.2.0-2/bin:${PATH}"
# RUN rm -rf /tmp/riscv-gcc

# This is install from xpack
# RUN mkdir -p /tmp/riscv-gcc
# RUN curl -fsSL https://github.com/xpack-dev-tools/riscv-none-embed-gcc-xpack/releases/download/v10.2.0-1.2/xpack-riscv-none-embed-gcc-10.2.0-1.2-linux-x64.tar.gz | tar -xzC /tmp/riscv-gcc
# RUN mv /tmp/riscv-gcc/xpack-riscv-none-embed-gcc-10.2.0-1.2 /opt
# RUN chmod -R +x /opt/xpack-riscv-none-embed-gcc-10.2.0-1.2/bin
# ENV PATH="/opt/xpack-riscv-none-embed-gcc-10.2.0-1.2/bin:${PATH}"
# RUN rm -rf /tmp/riscv-gcc

# Install beforeinstall from MounRiver_Studio_Community_Linux_x64_V150
# RUN mkdir -p /app/moun_river_studio_beforeinstall
# COPY beforeinstall/ /app/moun_river_studio_beforeinstall/
# RUN chmod +x /app/moun_river_studio_beforeinstall/start.sh
# RUN /app/moun_river_studio_beforeinstall/start.sh

# # Install WCH openocd files
# # COPY openocd_cfgs/* /usr/local/share/openocd/scripts/target/
# COPY openocd_cfgs/* /usr/share/openocd/scripts/target/
# RUN rm -rf /app/moun_river_studio_beforeinstall

RUN mkdir -p /tmp/wch_riscv
# COPY wch/MRS_Toolchain_Linux_x64_V1.80.tar.xz /tmp/wch_riscv
# RUN tar -xJf MRS_Toolchain_Linux_x64_V1.80.tar.xz -C /tmp/wch_riscv

# Download the file from the URL
RUN wget -P /tmp/wch_riscv http://file.mounriver.com/tools/MRS_Toolchain_Linux_x64_V1.80.tar.xz

# Extract the downloaded file
RUN tar -xJf /tmp/wch_riscv/MRS_Toolchain_Linux_x64_V1.80.tar.xz -C /tmp/wch_riscv


RUN mkdir -p /opt/gcc-riscv/
RUN mv "/tmp/wch_riscv/MRS_Toolchain_Linux_x64_V1.80/RISC-V Embedded GCC" /opt/gcc-riscv/riscv-wch-embedded-gcc-v1.80
RUN chown -R root:root /opt/gcc-riscv/riscv-wch-embedded-gcc-v1.80

RUN mkdir -p /opt/openocd/
RUN mv /tmp/wch_riscv/MRS_Toolchain_Linux_x64_V1.80/OpenOCD /opt/openocd/wch-openocd-v1.80
RUN chown -R root:root /opt/openocd/wch-openocd-v1.80

RUN mkdir -p /usr/lib/wch/
RUN cp -P /tmp/wch_riscv/MRS_Toolchain_Linux_x64_V1.80/beforeinstall/lib* /usr/lib/wch/
RUN ldconfig

# RUN mkdir -p /etc/udev/rules.d
RUN cp /tmp/wch_riscv/MRS_Toolchain_Linux_x64_V1.80/beforeinstall/50-wch.rules /etc/udev/rules.d
RUN cp /tmp/wch_riscv/MRS_Toolchain_Linux_x64_V1.80/beforeinstall/60-openocd.rules  /etc/udev/rules.d
# RUN /lib/udev/udevd --daemon
# RUN service udev status
# RUN /lib/systemd/systemd --system
# RUN service udev restart
# RUN udevadm control --reload-rules && udevadm trigger

ENV LD_LIBRARY_PATH="/usr/lib/wch:$LD_LIBRARY_PATH"
ENV PATH="/opt/gcc-riscv/riscv-wch-embedded-gcc-v1.80/bin:$PATH"
ENV PATH="/opt/openocd/wch-openocd-v1.80/bin:$PATH"


# Cleanup to reduce the image size
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
