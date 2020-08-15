def ec2_client():
    import boto3
    client = boto3.client('ec2')
    return(client)
