FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the local code to the container
COPY . /app

# Install Flask (assuming you have a requirements.txt file)
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which the app will run
EXPOSE 5000

# Define the command to run your Flask app
CMD ["python3", "hello.py"]