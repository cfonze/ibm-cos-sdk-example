import ibm_boto3

ENDPOINT_URL = 'https://s3.us.cloud-object-storage.appdomain.cloud'
BUCKET_NAME = 'pnnl-data'

ITEM_NAME = 'example file.pdf'
FILE_PATH = './example file.pdf'


def multi_part_upload(bucket_name, item_name, file_path):
    try:
        print("Starting file transfer for {0} to bucket: {1}\n".format(item_name, bucket_name))
        # set 5 MB chunks
        part_size = 1024 * 1024 * 5

        # set threadhold to 15 MB
        file_threshold = 1024 * 1024 * 15

        # set the transfer threshold and chunk size
        transfer_config = ibm_boto3.s3.transfer.TransferConfig(
            multipart_threshold=file_threshold,
            multipart_chunksize=part_size
        )

        # the upload_fileobj method will automatically execute a multi-part upload
        # in 5 MB chunks for all files over 15 MB
        with open(file_path, "rb") as file_data:
            s3.Object(bucket_name, item_name).upload_fileobj(
                Fileobj=file_data,
                Config=transfer_config
            )

        print("Transfer for {0} Complete!\n".format(item_name))
    except Exception as e:
        print("Error: {0}".format(e))


s3 = ibm_boto3.resource("s3", endpoint_url=ENDPOINT_URL)
multi_part_upload(BUCKET_NAME, ITEM_NAME, FILE_PATH)
