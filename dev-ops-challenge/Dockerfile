FROM python:latest
#Defining the latest image release to use for container.

WORKDIR /Users/hnuga/Desktop/dev-ops-challenge
#Sets working directory.

RUN pip3 install requests
RUN pip3 install pyyaml
#Installs necessary libraries to run files.

COPY input.yaml ./
COPY input.py ./
COPY url.py ./
#Copies all necessary files to working directory for container to use.

CMD ["python3","input.py"]
#Keeping docker container alive.
