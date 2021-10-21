# pulls ubuntu image
FROM ubuntu:16.04

# installs python 
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /Devops project/requirements.txt

# mounts docker file to directory
WORKDIR /Devops project

# install requirements
RUN pip install -r requirements.txt

# copy our application to working directory
COPY . /Devops project

# exposes port 5000 for our app
EXPOSE 5000

ENTRYPOINT [ "python" ]

#CMD [ "my_app.py" ]
