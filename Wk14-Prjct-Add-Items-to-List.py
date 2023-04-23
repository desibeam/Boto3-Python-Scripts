import boto3

# Create a DynamoDB resource

dynamodb = boto3.client('dynamodb', region_name = 'us-west-2')

# Access a table using the Table attribute

table = dynamodb.table('rnb_songs_i_like')

#Add 10 items into the table using the put_item method

table.put_item(
    Item={
        'song': {
        'S': 'Water Falls',
        'year': 
        'N': '1994',
        'artist': 
        'S': 'TLC',
        'album': 
        'S': 'Crazy Sexy Cool',
        }
    }
    
)

dynamodb.put_item(TableName='rnb_songs_I_like', Item=item)

table.put_item(
    Item={'song_title': 'Waterfalls', 'artist': 'TLC'}
    
)

table.put_item(
    Item={
        'album' : "Revival"
    
    }
)

table.put_item(
    Item={
       'album' : "Forever_My_Lady"
    
    }
)

table.put_item(
    Item={
        'album' : "The_Miseducation_of_Lauryn_Hill"
    
    }
)

table.put_item(
    Item={
       'album' : "Maxwells_Urban_Hang_Suite"
    
    }
)

table.put_item(
    Item={
       'album' : "Secret"
    
    }
)

table.put_item(
    Item={
       'album' : "II"
    
    }
)

table.put_item(
    Item={
        'album' : "Born_To_Sing"
    
    }
)

table.put_item(
    Item={
        'album' : "The_Day"
    
    }
)

table.put_item(
    Item={
        'album' : "One_In_a_Million"
    
    }
)

print("Put Items succeded")
