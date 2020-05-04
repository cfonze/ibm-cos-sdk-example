# ibm-cos-sdk-example

Example Python scripts for using with IBM Cloud Object Storage and the 
[IBM Cloud Object Storage - Python SDK](https://github.com/IBM/ibm-cos-sdk-python).

## Quick start

You\'ll need:

* An instance of COS
* A [Service Credential](#using-a-service-credential)
* A Bucket
* Service endpoint
* [Build from source](https://github.com/ibm/ibm-cos-sdk-python/#building-from-source)

Additional documentation can be found [here.](https://cloud.ibm.com/docs/services/cloud-object-storage?topic=cloud-object-storage-python#python-examples)

### Using a Service Credential

You can source credentials directly from a [Service
Credential](https://cloud.ibm.com/docs/services/cloud-object-storage/iam/service-credentials.html)
JSON document generated in the IBM Cloud console saved to
`~/.bluemix/cos_credentials`. The SDK will automatically load these
providing you have not explicitly set other credentials during client
creation.