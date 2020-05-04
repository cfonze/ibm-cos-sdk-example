import ibm_boto3

ENDPOINT_URL = 'https://s3.us.cloud-object-storage.appdomain.cloud'


def get_buckets():
    print("Retrieving list of buckets")
    try:
        buckets = s3.buckets.all()
        for bucket in buckets:
            print("Bucket Name: {0}".format(bucket.name))
    except Exception as e:
        print("Error: {0}".format(e))


s3 = ibm_boto3.resource("s3", endpoint_url=ENDPOINT_URL)
get_buckets()
