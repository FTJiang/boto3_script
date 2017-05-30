

import boto3
import os

region = os.environ.get('EC2REGION')

def init_session(r=None):
    if r is None:
        r = region
    s = boto3.Session(profile_name=r)
    return s.resource('ec2')

#list all the instance ids
def ls_ids():
    ec2 = init_session()
    for i in ec2.instances.all():
        print(i.id)
#return objects of given instance ids
def get_instance_by_ids(ids):
    ec2 = init_session()
    return ec2.Instance(id=ids)

#return objects corresponding to given filter
def get_instance_by_filters(filters):
    ec2 = init_session()
    instances = []
    for i in ec2.instances.filter(Filters=filters):
        instances.append(i)
    return instances

#helper function 
def append_filters(filters,name,values):
    filters.append({'Name':name,'Values':values})

#create instance and return ids
def create_instance(img_id,key_name):
    ec2 = init_session()
    outfile = open(key_name+'.pem','w')
    key_pair = ec2.create_key_pair(KeyName=key_name)
    KeyPairOut = str(key_pair.key_material)
    outfile.write(KeyPairOut)
    instances = ec2.create_instances(
        ImageId = img_id,
        #MinCount and MaxCount – Specify the number of instances to establish
        MinCount = 1,
        MaxCount = 1,
        KeyName = key_name,
        InstanceType = "t2.micro"
    )
    instances = []
    for instance in instances:
        instances.append(instance[0].id)
    return instances

#terminate given instances
def terminate_instance(ids):
    ec2 = init_session()
    for instance_id in ids:
        instance = ec2.Instance(instance_id)
        response = instance.terminate()
        print response
    

if __name__=='__main__':
    #ls_ids()
    #instance = get_instance('i-0d36ea736ea09f9a9')
    #ids = ['i-0d36ea736ea09f9a9','i-0e45eb67b483db99a']

    #test append_filters and get instance by filters
    filters=[{'Name': 'instance-type', 'Values': ['t2.micro']}]
    append_filters(filters,"hypervisor",['xen'])
    print(get_instance_by_ids(filters))

