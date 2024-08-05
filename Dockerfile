# Use the official Python image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Ensure the logs directory exists
RUN mkdir -p /app/logs

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run load_balancer.py when the container launches
CMD ["python", "load_balancer.py"]
