FROM ros:foxy

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -q -y --no-install-recommends apt-utils
RUN apt-get install -q -y --no-install-recommends net-tools iproute2 iputils-ping curl
RUN apt-get install -q -y --no-install-recommends git tmux vim apt-utils

RUN apt-get install -q -y --no-install-recommends python3 python-is-python3 python3-pip
RUN pip install pyserial

RUN apt-get clean

COPY ./read.py /
COPY ./00-teensy.rules /etc/udev/rules.d/