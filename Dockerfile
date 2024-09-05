# Use a Python base image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any required packages
RUN pip install -r requirements.txt

# Expose a port if necessary (e.g., for Flask/Django apps)
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
