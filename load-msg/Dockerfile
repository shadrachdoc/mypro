# Set the base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the necessary files to the working directory
COPY requirements.txt .
COPY run1.py .

# Install the required packages
RUN pip install -r requirements.txt

# Set environment variables
ENV AZURE_STORAGE_CONNECTION_STRING=DefaultEndpointsProtocol=https;AccountName=6545643;AccountKey=MhaERvUyva5+WSVt2k4J6jMkal0w5LXdshAbbIqCcynreZVOhpcdzNAhkts9/PbWmD33I13uv+uQ+AStMCA/XA==;EndpointSuffix=core.windows.net
ENV AZURE_STORAGE_QUEUE_NAME=incoming

# Run the Python script to load message and run container service
CMD python run1.py

