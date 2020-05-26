# base image is an Ubuntu
FROM ubuntu:latest

# installing needed packages
RUN apt update
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential

# we will copy the app folder containing the script and requirements
COPY ./app /app

# this is like doing `cd /app` from the Docker image perspective
WORKDIR /app

# installing pythob requirements
RUN pip3 install -r requirements.txt

# executing the script
CMD ["python3", "main.py"]