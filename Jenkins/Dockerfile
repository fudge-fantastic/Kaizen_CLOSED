# Base image using Python 3.11
FROM python:3.11-slim-buster

# Set the working directory in the container
WORKDIR /code

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the application code into the container
COPY . /code/

# Install application dependencies
COPY src/requirements.txt /code/
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir src/.

# Expose port 8000
EXPOSE 8000

# Command to run the application
CMD ["python", "main.py"]


# docker build -t image_name .
# docker run -p 8000:8000 image_name
# Uvicorn running on http://0.0.0.0:8000, instead, use this http://localhost:8000
# when you run the docker run command, you are launching a new container based on the specified image, and the application runs inside that container.