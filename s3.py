
import boto3
import os

region = os.environ.get('EC2REGION')

#get a s3 resource
def init_session(r=None):
    if r is None:
        r = region
    s = boto3.Session(profile_name=r)
    return s.resource('s3')

#list all contents in a bucket
def list_contents(bucket_name):
    s3 = init_session()
    try:
        bucket = s3.Bucket(bucket_name)
        for object in bucket.objects.all():
            print (object.key)
    except Exception as error:
        print (error)

#list all buckets
def list_buckets():
    for bucket in s3.buckets.all():
        print (bucket.name)

#list all buckets and their contents
def list_buckets_and_contents():
    s3 = init_session()
    for bucket in s3.buckets.all():
        print (bucket.name)
        print ("---")
        for item in bucket.objects.all():
            print ("\t%s" % item.key)

# 1) bucket names must be globally unique and
# 2) bucket names must follow DNS naming conventions.
def create_buckets(bucket_names):
    s3 = init_session()
    for bucket_name in bucket_names:
        try:
            response = s3.create_bucket(Bucket=bucket_name)
            print (response)
        except Exception as error:
            print (error)

#put a file in a bucket
def put_file(bucket_name,object_name):
    s3 = init_session()
    try:
        response = s3.Object(bucket_name,object_name).put(Body=open(object_name,'rb'))
    except Exception as error:
        print (error)
        
            
#delete all contents in buckets, provide a array
def delete_all_contents(buckets):
    s3 = init_session()
    for bucket_name in buckets:
        bucket = s3.Bucket(bucket_name)
        for key in bucket.objects.all():
            try:
                response = key.delete()
                print (response)
            except Exception as error:
                print (error)

#must delete all contents in bucket before delete the bucket
def delete_buckets(buckets):
    s3 = init_session()
    for bucket_name in buckets:
        bucket = s3.Bucket(bucket_name)
        try:
            response = bucket.delete()
            print (response)
        except Exception as error:
            print (error)

if __name__=="__main__":
    create_buckets(['for-delete1'])
    f = open('test.txt','w')
    f.write("for test\n")
    f.close()
    put_file('for-delete1','test.txt')
    list_contents("for-delete1")
    delete_all_contents(['for-delete'])
    delete_buckets(['for-delete'])

    


    
