# Use an official Python runtime as a base image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy requirements first and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose port 5000
EXPOSE 5000

# Define the entry point for the container
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:create_app()"]

