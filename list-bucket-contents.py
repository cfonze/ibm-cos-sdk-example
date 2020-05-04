import ibm_boto3

ENDPOINT_URL = 'https://s3.us.cloud-object-storage.appdomain.cloud'
BUCKET_NAME = 'pnnl-data'


def get_bucket_contents(bucket_name):
    print("Retrieving bucket contents from: {0}".format(bucket_name))
    try:
        files = s3.Bucket(bucket_name).objects.all()
        for file in files:
            print("Item: {0} ({1} bytes).".format(file.key, file.size))
    except Exception as e:
        print("Error: {0}".format(e))


s3 = ibm_boto3.resource("s3", endpoint_url=ENDPOINT_URL)
get_bucket_contents(BUCKET_NAME)
