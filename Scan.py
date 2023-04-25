import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Get the table resource.
table = dynamodb.Table('music')

# Scan the table.
response = table.scan()

# Print the items in the table.
for item in response['Items']:
    print(item)
