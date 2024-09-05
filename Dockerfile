# Use a Python base image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any required packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose a port (for Gunicorn)
EXPOSE 8000

# Run the application with Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
