# Use official Python base image
FROM python:3.8-slim

# Set working directory in container
WORKDIR /app

# Copy project files from host build context to container working directory
COPY . .

# Install dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt # Added --no-cache-dir for cleaner builds

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]