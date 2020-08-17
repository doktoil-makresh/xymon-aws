def generate_output(instances_health):
  xymon_msg = '&'+instances_health['global_status']['color']+'EC2 instances overall status is: '+instances_health['global_status']['message']
  for instance in instances_health['instances']:
    xymon_msg += '\n&'+instance['instance_color']+' Instance: '+instance['instance_id']+'\nInstances checks:'
    for detail in instance['instance_details_with_color']:
      xymon_msg += '\n&'+detail['color']+' Check '+detail['Name']+': '+detail['Status']
    xymon_msg += '\nSystem checks:'
    for detail in instance['system_details_with_color']:
      xymon_msg += '\n&'+detail['color']+' Check '+detail['Name']+': '+detail['Status']
  xymon_msg += '\n'
  return(xymon_msg)
