

import boto3


class Ec2:

    def __init__(self, ec2Client):
        self.__ec2Client = ec2Client
        #self.__response = self.__get_Instances()

    #request instances information
    def __get_Instances(self,filters):
        response = []
        if filters is None:
            response = self.__ec2Client.describe_instances()
        else:
            response = self.__ec2Client.describe_instances(Filters=filters)
        return response

    #if no filters provided, list all instances
    def list_instance_ids(self,filters=None):
        instance_ids = []
        response = self.__get_Instances(filters)
        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                instance_ids.append(instance['InstanceId'])
        return instance_ids

    #list whole information about instances
    def list_instances(self):
        instances = []
        for reservation in self.__response["Reservations"]:
            for instance in reservation["Instances"]:
                instances.append(instance);
        return instances




if __name__=='__main__':

    ec2Client = boto3.client('ec2')
    ec2 = Ec2(ec2Client)
    #print(ec2.list_instance_ids())
    #print(ec2.list_instances())
    print(ec2.list_all_instance_ids())
    
