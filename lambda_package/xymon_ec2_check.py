def lets_go():
  import aws_client
  import ec2_list
  import ec2_health
  import ec2_xymon_output
  from xymon_client import Xymon

#Create the EC2 client
  ec2_client = aws_client.create_client('ec2')
#Define the file containing the list of EC2 instances to monitor
  instances_list = list()
  instances_list.append('i-09ef7eeb1dfae05f5')
#Get the EC2 instances statuses
  instances_status = ec2_list.get_by_list(ec2_client,instances_list)
#Enhance the output
  instances_health = ec2_health.ec2s_health(instances_status['InstanceStatuses'])
#Generate Xymon message
  xymon_msg = ec2_xymon_output.generate_output(instances_health)

##Let's initialize the Xymon values
  _test = "EC2_status"

#Let's generate the statuses colors
  _status = instances_health['global_status']['color']

#Let's send this output to Xymon server(s)
  server = Xymon('www.makelofine.org',1984)
  server.report('aws',_test,_status,xymon_msg)
