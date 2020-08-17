#!/usr/bin/env python3
# -*- coding: utf-8

import aws_client
import ec2_list
import ec2_health
import ec2_xymon_output
import os
import datetime

#Create the EC2 client
ec2_client = aws_client.create_client('ec2')
#Define the file containing the list of EC2 instances to monitor
instances_list = 'ec2_instances.json'
#Get the EC2 instances statuses
instances_status = ec2_list.get_by_list(ec2_client,instances_list)
#Enhance the output
instances_health = ec2_health.ec2s_health(instances_status['InstanceStatuses'])
#Generate Xymon message
xymon_msg = ec2_xymon_output.generate_output(instances_health)

##Let's initialize the Xymon values
_test = "EC2_status"
now=datetime.datetime.now()
_date=now.strftime("%a %d %b %Y %H:%M:%S %Z")

#Let's generate the statuses colors
_status = instances_health['global_status']['color']

#Let's send this output to Xymon server(s)
_cmd_line="%s %s \"status %s.%s %s %s\n\n%s\"" %(os.environ['XYMON'], os.environ['XYMSRV'], os.environ['MACHINE'], _test, _status, _date, _msg_line)
os.system(_cmd_line)
