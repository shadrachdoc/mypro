from azure.storage.queue import QueueServiceClient

# Define connection string and queue name
connection_string = "DefaultEndpointsProtocol=https;AccountName=6545643;AccountKey=MhaERvUyva5+WSVt2k4J6jMkal0w5LXdshAbbIqCcynreZVOhpcdzNAhkts9/PbWmD33I13uv+uQ+AStMCA/XA==;EndpointSuffix=core.windows.net"
queue_name = "incoming"

# Create a queue service client
queue_service_client = QueueServiceClient.from_connection_string(connection_string)

# Get a queue client
queue_client = queue_service_client.get_queue_client(queue_name)

# Peek at the next message in the queue
messages = queue_client.receive_messages()
if messages:
    message = list(messages)[0]
    print("Message received: {}".format(message.content))
else:
    print("No messages in the queue.")

