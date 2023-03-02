import logging#
import sys
sys.path.append('/usr/local/lib/python3.9/site-packages')


import azure.functions as func

from azure.storage.queue import QueueServiceClient

# Set the connection string and queue name
connection_string = 'DefaultEndpointsProtocol=https;AccountName=pycode354;AccountKey=Y4WFGMP/2WGt4htqNUx8/t/WonJCXawafrA4POSMIr/sq3kjs8kasTMz/8mfrdsHbQIqoBA38BZD+AStyyJBaQ==;EndpointSuffix=core.windows.net'
queue_name = 'incoming'

# Create a QueueServiceClient object
queue_service_client = QueueServiceClient.from_connection_string(connection_string)

# Get a reference to the queue
queue_client = queue_service_client.get_queue_client(queue_name)

# Send a message to the queue
queue_client.send_message('Hello, Azure Queue!')

print('Message sent to Azure Queue.')

