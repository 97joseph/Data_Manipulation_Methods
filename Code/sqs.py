#!/usr/local/bin/python3


# Import the required libraries
import boto3

# Create the SQS client or resource here, depending on your usage
sqs = boto3.client("sqs")

# Create the queue by setting its name through QueueName
# Set the Attributes for the Queue by specifying the delay in seconds
# Additionally, set the period to retain the messages in the queue as you require
response = sqs.create_queue(
    QueueName="sqs-cpd-2021",
    Attributes={"DelaySeconds": "60", "MessageRetentionPeriod": "86400"},
)

# Print the QueueUrl which would be useful later if you want to attach policies using Python
print(response["QueueUrl"])
