# Pull base image
FROM python:3.9
 
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
 
# Set work directory
RUN mkdir /kurdish
WORKDIR /kurdish
 
# Install dependencies
COPY Pipfile Pipfile.lock /kurdish/
RUN pip install pipenv && pipenv install --system
RUN apt update
RUN apt install gettext -y
 
# Copy project
COPY . /kurdish/
