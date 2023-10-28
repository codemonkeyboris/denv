FROM ubuntu:22.04

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
    udev \
    minicom


################################################
#  WCH RISCV Related
################################################
# This version is too new for WCH chips
# # Install xPack GNU RISC-V Embedded GCC
# RUN mkdir -p /tmp/riscv-gcc
# RUN curl -fsSL https://github.com/xpack-dev-tools/riscv-none-elf-gcc-xpack/releases/download/v13.2.0-2/xpack-riscv-none-elf-gcc-13.2.0-2-linux-x64.tar.gz | tar -xzC /tmp/riscv-gcc
# RUN mv /tmp/riscv-gcc/xpack-riscv-none-elf-gcc-13.2.0-2 /opt
# RUN chmod -R +x /opt/xpack-riscv-none-elf-gcc-13.2.0-2/bin
# ENV PATH="/opt/xpack-riscv-none-elf-gcc-13.2.0-2/bin:${PATH}"
# RUN rm -rf /tmp/riscv-gcc

RUN mkdir -p /tmp/wch_riscv
RUN wget -P /tmp/wch_riscv http://file.mounriver.com/tools/MRS_Toolchain_Linux_x64_V1.80.tar.xz
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

RUN cp /tmp/wch_riscv/MRS_Toolchain_Linux_x64_V1.80/beforeinstall/50-wch.rules /etc/udev/rules.d
RUN cp /tmp/wch_riscv/MRS_Toolchain_Linux_x64_V1.80/beforeinstall/60-openocd.rules  /etc/udev/rules.d

RUN rm -rf /tmp/wch_riscv

ENV LD_LIBRARY_PATH="/usr/lib/wch:$LD_LIBRARY_PATH"
ENV PATH="/opt/gcc-riscv/riscv-wch-embedded-gcc-v1.80/bin:$PATH"
ENV PATH="/opt/openocd/wch-openocd-v1.80/bin:$PATH"

################################################
#  WCH CH Related
################################################
RUN apt-get install -y sdcc
COPY wch_programmer/chprog.py /usr/local/bin/
COPY wch_programmer/vnproch55x /usr/local/bin/
ENV PATH="/usr/local/bin/chprog.py:$PATH"
ENV PATH="/usr/local/bin/vnproch55x:$PATH"


# Install Arduino CLI
# RUN apt-get install -y curl && \
#     curl -fsSL https://downloads.arduino.cc/arduino-cli/arduino-cli_latest_Linux_64bit.tar.gz | tar -xzC /usr/local/bin && \
#     chmod +x /usr/local/bin/arduino-cli

RUN apt-get update && apt-get install -y \
    git \
    curl

# Install arduino-cli
RUN curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | BINDIR=/usr/local/bin sh

# Set up Arduino CLI and install the necessary tools and boards
RUN arduino-cli config init --additional-urls https://arduino.esp8266.com/stable/package_esp8266com_index.json
RUN arduino-cli core update-index
RUN arduino-cli core install arduino:avr
RUN arduino-cli core install esp8266:esp8266
RUN arduino-cli board listall
RUN arduino-cli lib install "ArduinoJson"

# Install Boards
RUN mkdir -p /root/.arduino15
RUN echo '{}' > /root/.arduino15/arduino-cli.yaml
RUN arduino-cli config add board_manager.additional_urls https://ch55xduino.pek3b.qingstor.com/package_ch55xduino_mcs51_newest_qingcloud_index.json
RUN arduino-cli config dump
RUN arduino-cli core install CH55xDuino:mcs51

RUN apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
