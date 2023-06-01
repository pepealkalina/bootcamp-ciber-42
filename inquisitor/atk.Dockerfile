FROM debian:stable-slim

# LABEL: herramienta para agregar metadatos a la imagen dato=valor
LABEL maintainer="inquisitor" 

RUN set -ex && apt update && apt install -y net-tools arping python3 python3-pip openssh-server curl 

COPY requirements.txt /tmp/requirements.txt

RUN echo "root:root" | chpasswd && echo "PermitRootLogin yes" >> /etc/ssh/sshd_config && echo "Port 4242" >> /etc/ssh/sshd_config

COPY exec.sh /exec.sh

RUN chmod +x /exec.sh
EXPOSE 4242

WORKDIR /root

ENTRYPOINT [ "/exec.sh" ]

