# Use an official Python runtime as a base image
FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy application files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Define the entry point
CMD ["python", "back.py"]
