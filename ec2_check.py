import boto3
import ec2_client
import ec2_list
import ec2_health
import ec2_status
ec2_client = ec2_client.ec2_client('ec2')

instances_list = ec2_instances.json
instances_health = ec2_list.get_by_list(ec2_client,instance_ids,instances_list)
instances_status = ec2_health.ec2_health(instances_health)
