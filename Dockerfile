FROM mongo:latest

RUN apt update -y
RUN apt install -y python3 python3-pip python3-venv

WORKDIR /data/db/agendum-database

COPY startup.py .
COPY db_python_util db_python_util

# https://stackoverflow.com/a/42917632/11411686
COPY startup.sh /docker-entrypoint-initdb.d/
RUN chmod +x /docker-entrypoint-initdb.d/startup.sh

# According to https://stackoverflow.com/a/47594352/11411686
# this isn't actually necessary but is good practice for documentation purposes
EXPOSE 27017
