# Use Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy app code and model files
COPY app/ ./app/
COPY models/ ./models/

# Install dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app/app.py"]
