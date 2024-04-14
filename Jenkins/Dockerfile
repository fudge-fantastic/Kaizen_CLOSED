# Docker file
# Base image using Python 3.11
FROM python:3.11

# Update package lists (recommended for fresh installs)
RUN apt-get update

# Install system dependencies (adjust if needed)
RUN apt-get install -y build-essential libpq-dev

# Upgrade pip (optional)
RUN pip install --upgrade pip

# This line copies all the files from the current directory (.) into a directory named /code within the Docker container.
COPY . /code

# Install application dependencies from requirements.txt
RUN pip install --upgrade -r /code/src/requirements.txt

# Working directory within the container
# WORKDIR /code/src
WORKDIR /code

# Set PYTHONPATH environment variable (optional)
# ENV PYTHONPATH="${PYTHONPATH}:/code/src"

# Executes the Application
CMD ["uvicorn", "main:app", "--reload", "--host=localhost", "--port=3000"]