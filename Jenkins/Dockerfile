FROM python:3.11

# This line updates the package list for the system's package manager (apt-get) 
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

# This line copies all the files from the current directory (.) into a directory named /code within the Docker container.
COPY . /code

# This line makes the script in the /code/src directory executable within the container.
RUN chmod +x /code/src

# The --no-cache-dir flag avoids using a cached directory for package installation, ensuring fresh dependencies.
RUN pip install --upgrade -r code/src/requirements.txt

# This line exposes port 8005 within the container, allowing external connections to reach your application running on that port.
EXPOSE 8005

# Our working Directory
WORKDIR /code/src

# This line sets an environment variable named PYTHONPATH. This variable tells Python where to look for modules and packages. 
# Here, it adds the /code/src directory to the search path, ensuring your application can find its dependencies.
ENV PYTHONPATH = "${PYTHONPATH}:/code/src"

# This line installs your application (main.py and its dependencies assumed to be in the current directory) in editable mode using pip install -e .
# This allows you to make changes to your code and test them without rebuilding the entire Docker image.
CMD pip install -e .