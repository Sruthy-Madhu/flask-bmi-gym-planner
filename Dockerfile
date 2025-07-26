FROM python:3.10-slim

# Install system dependencies required for psycopg2
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy app files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir flask psycopg2-binary

# Expose Flask port
EXPOSE 5000

#Expose Render Port
EXPOSE 10000

# Run the app
CMD ["python", "app.py"]
