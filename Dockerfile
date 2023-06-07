# Base image
FROM python:3

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

EXPOSE 5000

# Set the command to run your application
CMD ["python", "main.py"]

# Launch Dockerfile
# docker build -t app .
