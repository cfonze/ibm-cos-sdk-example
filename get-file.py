import ibm_boto3

ENDPOINT_URL = 'https://s3.us.cloud-object-storage.appdomain.cloud'
BUCKET_NAME = 'pnnl-data'

ITEM_NAME = 'example file.pdf'


def get_item(bucket_name, item_name):
    print("Retrieving item from bucket: {0}, key: {1}".format(bucket_name, item_name))
    try:
        file = s3.Object(bucket_name, item_name).get()
        print("File Contents: {0}".format(file["Body"].read()))
    except Exception as e:
        print("Error: {0}".format(e))


s3 = ibm_boto3.resource("s3", endpoint_url=ENDPOINT_URL)
get_item(BUCKET_NAME, ITEM_NAME)