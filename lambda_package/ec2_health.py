def ec2s_health(instances_status):
  instances_health = dict()
  instances_health['instances'] = list()
  global_red,global_yellow,global_blue = 0,0,0
  for instance_info in instances_status:
    instance_health = dict()
    instance_health['instance_id'] = instance_info['InstanceId']
    instance_color,instance_details_with_color,system_color,system_details_with_color = ec2_health(instance_info)
    instance_health['instance_color'] = instance_color
    instance_health['instance_details_with_color'] = instance_details_with_color
    instance_health['system_color'] = system_color
    instance_health['system_details_with_color'] = system_details_with_color
    instances_health['instance_id_health'] = instance_health
    global_red,global_yellow,global_blue = set_global_color(global_red,global_yellow,global_blue,instance_color,system_color)
    instances_health['instances'].append(instance_health)
  instances_health['global_status'] = global_status(global_red,global_yellow,global_blue)
  return(instances_health)

def global_status(global_red,global_yellow,global_blue):
  if global_red > 0:
    global_color = 'red'
    global_message = 'Alert !!!'
  elif global_yellow > 0:
    global_color = 'yellow'
    global_message = 'Warning'
  elif global_blue > 0:
    global_color = 'blue'
    global_message = 'Missing data'
  else:
    global_color = 'green'
    global_message = 'OK'
  global_status = dict()
  global_status['color'] = global_color
  global_status['message'] = global_message
  return(global_status)

def ec2_health(instance_info):
  instance_color = set_color(instance_info['InstanceStatus']['Status'])
  instance_details = instance_info['InstanceStatus']['Details']
  instance_details_with_color = check_details(instance_details)
  system_color = set_color(instance_info['SystemStatus']['Status'])
  system_details = instance_info['SystemStatus']['Details']
  system_details_with_color = check_details(system_details)
  return(instance_color,instance_details_with_color,system_color,system_details_with_color)
  
def set_color(status):
#Instance/System 'Status': 'ok'|'impaired'|'insufficient-data'|'not-applicable'|'initializing'
#Details 'Status': 'passed'|'failed'|'insufficient-data'|'initializing'
  if status == 'ok' or status == 'passed':
     color = 'green'
  elif status == 'initializing':
     color = 'yellow'
  elif status == 'impaired' or status == 'failed':
     color = 'red'
  elif status == 'insufficient-data':
     color = 'blue'
  return(color)

def check_details(details):
  for detail in details:
    name = detail['Name']
    status = detail['Status']
    detail['color'] = set_color(status)
  return(details)

def set_global_color(global_red,global_yellow,global_blue,instance_color,system_color):
  if instance_color == 'red' or system_color == 'red':
    global_red += 1
  elif instance_color == 'yellow' or system_color == 'yellow':
    global_yellow += 1
  elif instance_color == 'blue' or system_color == 'blue':
    global_blue += 1
  return(global_red,global_yellow,global_blue)
