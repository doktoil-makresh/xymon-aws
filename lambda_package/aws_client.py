def create_client(service):
    import boto3
#Create client
    client = boto3.client(service)
    return(client)
