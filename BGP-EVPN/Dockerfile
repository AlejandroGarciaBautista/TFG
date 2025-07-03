FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      sshpass \
      libssl-dev \
      libffi-dev \
      build-essential \
      docker.io \
      python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir ansible requests docker

WORKDIR /ansible

# Para que el contenedor no termine, dejamos este comando en foreground
CMD ["tail", "-f", "/dev/null"]
