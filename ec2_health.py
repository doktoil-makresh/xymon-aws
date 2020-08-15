def ec2_health(instances_health):
    all_instances = instances_health['InstanceStatuses']
    for instance in all_instances:
        InstanceId = instance['InstanceId']
        InstanceState = instance['InstanceState']['Name'] # 'Name': 'pending'|'running'|'shutting-down'|'terminated'|'stopping'|'stopped'
        InstanceStatus = instance['InstanceStatus']['Status'] # 'Status': 'ok'|'impaired'|'insufficient-data'|'not-applicable'|'initializing'
        if InstanceStatus == 'impaired':
            Impaired_instance_reason = instance['InstanceStatus']['Details']['Status'] # 'Status': 'passed'|'failed'|'insufficient-data'|'initializing'
        SystemStatus = instance['SystemStatus']['Status'] # Status': 'ok'|'impaired'|'insufficient-data'|'not-applicable'|'initializing'
        if SystemStatus == 'impaired':
            Impaired_system_reason = instance['InstanceStatus']['Details']['Status'] # 'Status': 'passed'|'failed'|'insufficient-data'|'initializing'

