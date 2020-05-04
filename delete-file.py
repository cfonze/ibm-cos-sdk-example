import ibm_boto3

ENDPOINT_URL = 'https://s3.us.cloud-object-storage.appdomain.cloud'
BUCKET_NAME = 'pnnl-data'

ITEM_NAME = 'example file.pdf'


def delete_item(bucket_name, item_name):
    print("Deleting item: {0}".format(item_name))
    try:
        s3.Object(bucket_name, item_name).delete()
        print("Item: {0} deleted!".format(item_name))
    except Exception as e:
        print("Error: {0}".format(e))


s3 = ibm_boto3.resource("s3", endpoint_url=ENDPOINT_URL)
delete_item(BUCKET_NAME, ITEM_NAME)