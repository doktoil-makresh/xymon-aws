#Get list of EC2 instances to monitor from a file
def get_by_list(ec2_client,instances_list):
    response = ec2_client.describe_instance_status(
    InstanceIds=instances_list,
    DryRun=False,
    IncludeAllInstances=True
    )
    return(response)

#Or get list from EC2 account
def get_all():
    response = ec2_client.describe_instance_status(
    MaxResults=1000,
    DryRun=False,
    IncludeAllInstances=True
)
    return(response)
