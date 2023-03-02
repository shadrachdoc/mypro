from azure.storage.queue import QueueServiceClient

# Define connection string and queue name
connection_string = "DefaultEndpointsProtocol=https;AccountName=6545643;AccountKey=MhaERvUyva5+WSVt2k4J6jMkal0w5LXdshAbbIqCcynreZVOhpcdzNAhkts9/PbWmD33I13uv+uQ+AStMCA/XA==;EndpointSuffix=core.windows.net"
queue_name = "incoming"

# Create a queue service client
queue_service_client = QueueServiceClient.from_connection_string(connection_string)

# Get a queue client
queue_client = queue_service_client.get_queue_client(queue_name)

# Get the approximate number of messages in the queue
queue_properties = queue_client.get_queue_properties()
message_count = queue_properties.approximate_message_count

if message_count > 0:
    # Get the last message in the queue
    messages = queue_client.receive_messages(max_messages=1)
    message = list(messages)[0]
    print("Message received: {}".format(message.content))
else:
    print("No messages in the queue.")
