import boto3
import random

sqs = boto3.resource('sqs')
queue_url = 'https://sqs.us-west-2.amazonaws.com/586687123428/customer-orders'

def lambda_handler(event, context):
    # Generate a random number
    message_body = str(random.randint(1, 100))
    
    # Send message to the SQS queue
    queue = sqs.Queue(queue_url)
    response = queue.send_message(MessageBody=message_body)
    
    print(f"Message sent: {response['MessageId']}")

