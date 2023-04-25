import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='music',
    KeySchema=[
        {
            'AttributeName': 'artist',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'song',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'artist',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'song',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
table.wait_until_exists()

# Get the table resource.
table = dynamodb.Table('music')

# Create item 1.
item1 = {
    'artist': 'Drake',
    'song': 'Laugh Now Cry Later',
    'genre': 'Hip Hop'
}

# Create item 2.
item2 = {
    'artist': 'Ariana Grande',
    'song': 'Positions',
    'genre': 'Pop'
}

# Create item 3.
item3 = {
    'artist': 'Taylor Swift',
    'song': 'Willow',
    'genre': 'Pop'
}

# Create item 4.
item4 = {
    'artist': 'Beyonce',
    'song': 'Formation',
    'genre': 'R&B'
}

# Create item 5.
item5 = {
    'artist': 'Eminem',
    'song': 'Lose Yourself',
    'genre': 'Hip Hop'
}

# Create item 6.
item6 = {
    'artist': 'Snoop Dogg',
    'song': 'Gin and Juice',
    'genre': 'Hip Hop'
}

# Create item 7.
item7 = {
    'artist': 'Baby Face',
    'song': 'When Can I See You',
    'genre': 'R&B'
}

# Create item 8.
item8 = {
    'artist': 'Aaliyah',
    'song': 'Try Again',
    'genre': 'R&B'
}

# Create item 9.
item9 = {
    'artist': 'En Vogue',
    'song': 'Don\'t Let Go (Love)',
    'genre': 'R&B'
}

# Create item 10.
item10 = {
    'artist': 'Maxwell',
    'song': 'Ascension (Don\'t Ever Wonder)',
    'genre': 'R&B'
}

# Add the items to the table.
table.put_item(Item=item1)
table.put_item(Item=item2)
table.put_item(Item=item3)
table.put_item(Item=item4)
table.put_item(Item=item5)
table.put_item(Item=item6)
table.put_item(Item=item7)
table.put_item(Item=item8)
table.put_item(Item=item9)
table.put_item(Item=item10)