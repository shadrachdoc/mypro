import os
import sys
import time
import azure.storage.queue 

# Retrieve the connection string and queue name from environment variables
connection_string = os.environ['DefaultEndpointsProtocol=https;AccountName=pyfun326ccf16;AccountKey=1Ul8S+Lk86/1ld+wgP6s3iGw110jI+xVt0WX0AjUBGe0g8oMmRbmJ4xkqsPw1hl0VkTsaqNihUTA+AStnTHsEw==;EndpointSuffix=core.windows.net']
queue_name = os.environ['incoming']

# Create a connection to the queue service
queue_service = QueueService(connection_string=connection_string)

# Continuously check for the most recent message in the queue
while True:
    messages = queue_service.get_messages(queue_name=queue_name, num_messages=10)
    if messages:
        # Get the most recent message
        message = max(messages, key=lambda x: x.insertion_time)

        # Print "Hello World" if this is the most recent message in the queue
        if message.id == messages[-1].id:
            print("Hello World")

    # Wait for 1 minute before checking again
    time.sleep(60)

