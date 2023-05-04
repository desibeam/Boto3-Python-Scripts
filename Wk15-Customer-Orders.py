import boto3

sqs = boto3.resource('sqs')

# Create a new SQS queue named 'customer-orders'
queue = sqs.create_queue(QueueName='customer-orders')

