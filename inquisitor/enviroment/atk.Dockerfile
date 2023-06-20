FROM debian:stable-slim

# LABEL: herramienta para agregar metadatos a la imagen dato=valor
LABEL maintainer="inquisitor" 

RUN set -ex && apt-get update && apt-get install -y python3 python3-dev libpcap-dev libnet-dev pip arping net-tools bash openssh-server curl python-libpcap

COPY requirements.txt /tmp/requirements.txt

RUN echo "root:root" | chpasswd && echo "PermitRootLogin yes" >> /etc/ssh/sshd_config && echo "Port 4242" >> /etc/ssh/sshd_config

COPY exec.sh /exec.sh

RUN chmod +x /exec.sh
EXPOSE 4242

WORKDIR /root

ENTRYPOINT [ "/exec.sh" ]

