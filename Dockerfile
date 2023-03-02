# Set the base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the necessary files to the working directory
COPY requirements.txt .
COPY send_message.py .

# Install the required packages
RUN pip install -r requirements.txt
RUN apt-get update && apt-get -y install cron
# Set environment variables
ENV AZURE_STORAGE_CONNECTION_STRING=DefaultEndpointsProtocol=https;AccountName=6545643;AccountKey=MhaERvUyva5+WSVt2k4J6jMkal0w5LXdshAbbIqCcynreZVOhpcdzNAhkts9/PbWmD33I13uv+uQ+AStMCA/XA==;EndpointSuffix=core.windows.net
ENV AZURE_STORAGE_QUEUE_NAME=incoming

# Run the Python script every minute using cron
RUN echo "* * * * * root /usr/bin/python3 /app/send_message.py >> /var/log/cron.log 2>&1" >> /etc/cron.d/send_message_cron
RUN chmod 0644 /etc/cron.d/send_message_cron
RUN crontab /etc/cron.d/send_message_cron
RUN touch /var/log/cron.log

# Install Azure Functions Core Tools
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/microsoft-prod.list
RUN apt-get update && apt-get install azure-functions-core-tools -y

# Start cron
CMD cron && tail -f /var/log/cron.log

