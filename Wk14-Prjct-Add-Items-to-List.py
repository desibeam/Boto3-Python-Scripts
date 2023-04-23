import boto3

# Create a DynamoDB resource

dynamodb = boto3.client('dynamodb', region_name = 'us-west-2')

# Access a table using the Table attribute

table = dynamodb.table('rnb_songs_i_like')

#Add 10 items into the table using the put_item method

table.put_item(
    item = {'album':{'S':'Whats the 411?'},
        'artist':{'S':'Mary J. Blige'},
        'info':{'M':{'year':{'S':'1992'},
                    'song':{'S':'Real Love'}}}}
        
    item = {'album':{'S':'Johnny Gill'},
        'artist':{'S':'Johnny Gill'},
        'info':{'M':{'year':{'S':'1990'},
                    'song':{'S':'My My My'}}}}

    item = {'album':{'S':'The Miseducation of Lauryn Hill'},
        'artist':{'S':'Lauren Hill'},
        'info':{'M':{'year':{'S':'1998'},
                    'song':{'S':'Ex-Factor'}}}}

    item = {'album':{'S':'Maxwells Urban Hang Suite'},
        'artist':{'S':'Maxwell'},
        'info':{'M':{'year':{'S':'1996'},
                    'song':{'S':'Ascension'}}}}

    item = {'album':{'S':'Secret'},
        'artist':{'S':'Toni Braxton'},
        'info':{'M':{'year':{'S':'1996'},
                    'song':{'S':'Un-Break My Heart'}}}}

    item = {'album':{'S':'Boyz II Men II'},
        'artist':{'S':'Boyz II Men'},
        'info':{'M':{'year':{'S':'1994'},
                    'song':{'S':'I’ll Make Love to You'}}}}

    item = {'album':{'S':'Born to Sing'},
        'artist':{'S':'Envogue'},
        'info':{'M':{'year':{'S':'1990'},
                    'song':{'S':'Don’t Let Go'}}}}

    item = {'album':{'S':'The Day'},
        'artist':{'S':'Babyface'},
        'info':{'M':{'year':{'S':'1996'},
                    'song':{'S':'Every Time I Close My Eyes'}}}}

    item = {'album':{'S':'One in a Million'},
         'artist':{'S':'Aaliyah'},
         'info':{'M':{'year':{'S':'1996'},
                'song':{'S':'One in a Million'}}}}
)

print("Put Items succeded")
