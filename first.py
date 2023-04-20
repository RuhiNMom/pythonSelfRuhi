import boto3
print("Lets start....")
ans = input("hi whatsupp whats your name??")
print(ans)

s3 = boto3.resource('s3')
buckets = [bucket.name for bucket in s3.buckets.all()]