# Docker file
# Base image using Python 3.11
FROM python:3.11-slim-buster

# Working directory within the container
WORKDIR /code

# This line copies all the files from the current directory (.) into a directory named /code within the Docker container.
COPY . .

# Update package lists (recommended for fresh installs) and installs system dependencies (adjust if needed)
RUN apt-get update && apt-get install -y build-essential libpq-dev

# Upgrade pip (optional)
RUN pip install --upgrade pip

# Install application dependencies from requirements.txt
RUN pip install --upgrade -r /code/src/requirements.txt

# Set PYTHONPATH environment variable (optional)
ENV PYTHONPATH="${PYTHONPATH}:/code/src"

# Executes the Application
RUN ["python", "main.py"]


