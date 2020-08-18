# xymon-aws
This set a script aims to provide monitoring purpose of your AWS infrastructure.
Current working scripts are related to EC2 only.
##Monitoring with AWS Lambda
If you want to run this script from AWS Lambda, you will require an execution role with 2 policies.
The first is managed by AWS: AWSLambdaVPCAccessExecutionRole 
The second is a user managed policy:
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents",
                "ec2:CreateNetworkInterface",
                "ec2:DescribeNetworkInterfaces",
                "ec2:DeleteNetworkInterface"
            ],
            "Resource": "*"
        }
    ]
}
If you require your xymon client to use a fixed IP, then follow this procedure:
https://medium.com/financial-engines-techblog/aws-lambdas-with-a-static-outgoing-ip-5174a1e70245

##Xymon server configuration:
Add an entry in your hosts.cfg file, with Elastic IP and add the name of your test. Disable ping test (noping tag)
Example:
1.2.3.4    aws # EC2_status noping

#Monitor from a computer
Install boto3 python (pip install boto3)
Create an IAM policy with the following permissions:
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeInstances",
                "ec2:DescribeInstanceTypes",
                "ec2:DescribeInstanceStatus"
            ],
            "Resource": "*"
        }
    ]
}
Create an IAM programmatic user, and feed the creds.ini file with its user key and secret key.
This is not necessary while using AWS Lambda.
