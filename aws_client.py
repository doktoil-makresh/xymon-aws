def create_client(service):
    import boto3
#Get credentials from file
    import configparser
    credentials = configparser.ConfigParser()
    credentials.read('creds.ini')
    ACCESS_KEY = credentials[service]['aws_access_key_id']
    SECRET_KEY = credentials[service]['aws_secret_access_key']
#Create client
    client = boto3.client(service,aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY)
    return(client)
