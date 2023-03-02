import logging#
import sys
sys.path.append('/usr/local/lib/python3.9/site-packages')


import azure.functions as func

from azure.storage.queue import QueueServiceClient

# Set the connection string and queue name
connection_string = 'DefaultEndpointsProtocol=https;AccountName=6545643;AccountKey=MhaERvUyva5+WSVt2k4J6jMkal0w5LXdshAbbIqCcynreZVOhpcdzNAhkts9/PbWmD33I13uv+uQ+AStMCA/XA==;EndpointSuffix=core.windows.net'
queue_name = 'incoming'

# Create a QueueServiceClient object
queue_service_client = QueueServiceClient.from_connection_string(connection_string)

# Get a reference to the queue
queue_client = queue_service_client.get_queue_client(queue_name)

# Send a message to the queue
queue_client.send_message('Hello, Azure Queue675!')

print('Message sent to Azure Queue.')

