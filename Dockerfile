FROM python:3.8-slim

# Copy local files
WORKDIR /root
COPY ["main.py", "main.py"]
COPY ["entrypoint.sh", "entrypoint.sh"]
RUN chmod +x entrypoint.sh

ENTRYPOINT ./entrypoint.sh
