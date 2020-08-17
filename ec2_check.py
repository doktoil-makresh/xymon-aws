import aws_client
import ec2_list
import ec2_health
import ec2_xymon_output
ec2_client = aws_client.create_client('ec2')

instances_list = 'ec2_instances.json'
instances_status = ec2_list.get_by_list(ec2_client,instances_list)
instances_health = ec2_health.ec2s_health(instances_status['InstanceStatuses'])
_msg = ec2_xymon_output.generate_output(instances_health)
