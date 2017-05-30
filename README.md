Boto3_Script
========

This is the practice of using boto3 for python. I use boto3 to build common utils to manipulate AWS, which can be applied for future project.

## prerequisite

**I assume you have installed python and pip**

Install the latest Boto 3 release via pip:
```
pip install boto3
```
You may also install a specific version:
```
pip install boto3==1.0.0
````
If you have the AWS CLI installed, then you can use it to configure your credentials file:
```
aws configure
```
finish the prompt

## ec2

### This is the util relate to ec2 instances.

* **init_session()**: helper function for obtaining ec2 resource

* **ls_ids()**: list all the instance ids

* **get_instance_by_ids(ids)**: return objects of given instance ids. ids is the list of instances

* **get_instance_by_filters(filters)**: return objects corresponding to given filter. For instance, filters=[{'Name': 'instance-type', 'Values': ['t2.micro']}]

* **append_filters(filters,name,values)**: helper function to append more filters

* **create_instance(img_id,key_name)**: create instance and return ids, img_id: image id used by instance key_name: name of key-pair file

* **terminate_instance(ids)**: terminate given instances. ids is the list of instances


## s3

### This is the util relate to s3 instances.

* **init_session()**: helper function for obtaining s3 resource

* **list_contents(bucket_name)**: list all contents in a bucket

* **list_buckets()**: list all buckets

* **list_buckets_and_contents()**: list all buckets and their contents

* **create_buckets(bucket_names)**: create buckets by given name. bucket_names is a list of bucket name

* **put_file(bucket_name,object_name)**: put a file in a bucket. bucket_name: name of bucket to put file; object_name: file name

* **delete_all_contents(buckets)**: delete all contents in buckets, provide a array

* **delete_buckets(buckets)**: must delete all contents in bucket before delete the bucket. buckets is a list of bucket names


