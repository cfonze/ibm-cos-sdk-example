import ibm_boto3
from progressbar import ProgressBar, Percentage, Bar, ETA, RotatingMarker, FileTransferSpeed
import humanize
import os
import os.path
from os import path

COS1_ENDPOINT_URL = 'https://s3.us.cloud-object-storage.appdomain.cloud'
COS1_AWS_ACCESS_KEY_ID = '***'
COS1_AWS_ACCESS_ACCESS_KEY = '***'
COS1_BUCKET_NAME = 'pnnl-data'

COS2_ENDPOINT_URL = 'https://s3.us.cloud-object-storage.appdomain.cloud'
COS2_AWS_ACCESS_KEY_ID = '***'
COS2_AWS_ACCESS_ACCESS_KEY = '***'
COS2_BUCKET_NAME = 'pnnl-data-copy-test'


def cos2_multi_part_upload(item_name, file_data):
    try:
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
        with open('./file.data', "rb") as file_data:
            cos2.Object(COS2_BUCKET_NAME, item_name).upload_fileobj(
                Fileobj=file_data,
                Config=transfer_config
            )

    except Exception as e:
        print("Error: {0}".format(e))


def total_size_of_source_bucket():
    print("Retrieving source bucket size.")
    try:
        cos1_files = cos1.Bucket(COS1_BUCKET_NAME).objects.all()
        cos1_total = 0
        for f in cos1_files:
            cos1_total += f.size

        return cos1_total
    except Exception as e:
        print("Error: {0}".format(e))


cos1 = ibm_boto3.resource('s3',
                          aws_access_key_id=COS1_AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=COS1_AWS_ACCESS_ACCESS_KEY,
                          endpoint_url=COS1_ENDPOINT_URL)

cos2 = ibm_boto3.resource('s3',
                          aws_access_key_id=COS2_AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=COS2_AWS_ACCESS_ACCESS_KEY,
                          endpoint_url=COS2_ENDPOINT_URL)

try:
    files = cos1.Bucket(COS1_BUCKET_NAME).objects.all()

    total_size = total_size_of_source_bucket()
    print("Source bucket size: {0}".format(humanize.naturalsize(total_size)))

    progress, progress_maxval = 0, total_size
    pbar = ProgressBar(widgets=['Transferring: ', Percentage(), ' ', Bar(marker=RotatingMarker()), ' ', ETA(), ' ',
                                FileTransferSpeed()],
                       maxval=progress_maxval).start()

    current_size = 0
    for file in files:
        if path.exists('./file.data'):
            os.remove('./file.data')

        with open('file.data', 'wb') as data:
            cos1.Bucket(COS1_BUCKET_NAME).download_fileobj(file.key, data)
            cos2_multi_part_upload(file.key, data)

        current_size += file.size
        pbar.update(current_size)

    pbar.finish()
    print("Transfer completed successfully!")

except Exception as e:
    print("Error: {0}".format(e))
