import boto3

s3 = boto3.client('s3')

#%%

response = s3.list_buckets()

list_buckets(client.buckets.all())

len(bucket.list)


#%%

for bucket in buckets:
    print(bucket["Name"])
