# Set the base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the necessary files to the working directory
COPY requirements.txt .
COPY run_container.py .

# Install the required packages
RUN pip install -r requirements.txt

# Set environment variables
ENV AZURE_STORAGE_CONNECTION_STRING=DefaultEndpointsProtocol=https;AccountName=pyfun326ccf16;AccountKey=1Ul8S+Lk86/1ld+wgP6s3iGw110jI+xVt0WX0AjUBGe0g8oMmRbmJ4xkqsPw1hl0VkTsaqNihUTA+AStnTHsEw==;EndpointSuffix=core.windows.net
ENV AZURE_STORAGE_QUEUE_NAME=incoming

# Run the Python script to load message and run container service
CMD python run_container.py

