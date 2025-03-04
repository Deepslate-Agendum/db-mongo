FROM mongo:latest

WORKDIR /home/ubuntu/agendum-database

COPY startup.py .
COPY db_python_util .
RUN apt update -y
RUN apt install -y python3 python3-pip

# https://stackoverflow.com/a/42917632/11411686
# COPY startup.sh /docker-entrypoint-initdb.d/

# According to https://stackoverflow.com/a/47594352/11411686
# this isn't actually necessary but is good practice for documentation purposes
EXPOSE 27017
