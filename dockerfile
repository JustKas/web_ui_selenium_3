# Use Ubuntu 20.04 - official docker image
FROM ubuntu:20.04

## Update package manager and install debian packages
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    build-essential \
    zlib1g-dev \
    libssl-dev

# Install utils
RUN apt-get update && apt-get install -y \
    wget

# Install Chrome browser
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get -y install google-chrome-stable

# Dowload and unpack python 3.10.4
RUN wget https://www.python.org/ftp/python/3.10.4/Python-3.10.4.tgz
RUN tar xzvf Python-3.10.4.tgz && rm Python-3.10.4.tgz

# Install python 3.10.4
RUN cd /Python-3.10.4 && ./configure && make && make install
RUN rm -rf Python-3.10.4

# Install pip
RUN python3 -m pip install pip==21.3.1

# copy project files to container
WORKDIR /app
COPY . .

# Install python libraris/packages
RUN pip install -r requirements.txt

RUN python3 -m pytest
