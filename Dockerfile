FROM python:3.10-slim

# Copy all the files from the repository to the container
# The .dockerignore file is used to exclude files and directories
COPY . /app

# Change the working directory to /app
WORKDIR /app

# Create a virtual environment
RUN python3 -m venv /opt/venv

# Clean Python interpreter without packages: /opt/venv/bin/python
# Update pip and install the requirements
RUN /opt/venv/bin/python -m pip install pip --upgrade && \
    /opt/venv/bin/python -m pip install mysql-client &&    \
    /opt/venv/bin/python -m pip install -r requirements.txt

# Run our application
CMD /opt/venv/bin/gunicorn    \
         --bind "0.0.0.0:8000" \
         --chdir /app/webserver \
         webserver.wsgi:application