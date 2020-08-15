#Get list of EC2 instances to monitor from a file
def get_by_list(instance_ids,instances_list):
    import json
    json_file = instances_list
    with open(json_file, 'rb') as f:
        instances_ids = json.load(f)
        response = client.describe_instance_status(
        InstanceIds=[instance_ids],
        DryRun=False,
        IncludeAllInstances=True
)
	return(response)

#Or get list from EC2 account
def get_all():
    response = client.describe_instance_status(
    MaxResults=1000,
    DryRun=False,
    IncludeAllInstances=True
)
    return(response)
