# Base image is python 3.1
FROM python:3.11.5

# Set the working directory 
WORKDIR /app

# Copy the requirements file 
COPY requirements.txt .

# Install  dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the other codes
COPY main.py .
COPY utils.py .
COPY run.sh .

COPY public public
COPY templates templates

# Set and expose ports
ENV APP_PORT=3000
EXPOSE ${APP_PORT}

# Add healthcheck
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
   CMD curl http://localhost:${APP_PORT}/health

# Make the run.sh script executable
CMD ["./run.sh"]
