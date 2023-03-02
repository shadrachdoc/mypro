from azure.storage.queue import QueueClient

queue_connection_string = 'DefaultEndpointsProtocol=https;AccountName=6545643;AccountKey=MhaERvUyva5+WSVt2k4J6jMkal0w5LXdshAbbIqCcynreZVOhpcdzNAhkts9/PbWmD33I13uv+uQ+AStMCA/XA==;EndpointSuffix=core.windows.net'
queue_name = 'incoming'

queue_client = QueueClient.from_connection_string(queue_connection_string, queue_name)

queue_properties = queue_client.get_queue_properties()
queue_count = queue_properties.approximate_message_count

print('Queue count:', queue_count)

