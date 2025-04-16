# Use official Python image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy all files from your project folder into the container
COPY . .

# Install required Python packages
RUN pip install -r requirements.txt

# Expose port 81 (this is what the app uses)
EXPOSE 81

# Run the app
CMD ["python", "app.py"]
