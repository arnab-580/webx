# Base Image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Flask runs on port 5000
EXPOSE 5000

# Run Flask application
CMD ["python", "app.py"]
