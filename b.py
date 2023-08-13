import boto3

def list_resources(resource_type, client):
    resources = []

    if resource_type == 'ec2':
        response = client.describe_instances()
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                resources.append(instance)
    elif resource_type == 's3':
        response = client.list_buckets()
        for bucket in response['Buckets']:
            resources.append(bucket)
    elif resource_type == 'rds':
        response = client.describe_db_instances()
        for db_instance in response['DBInstances']:
            resources.append(db_instance)
    elif resource_type == 'lambda':
        response = client.list_functions()
        for function in response['Functions']:
            resources.append(function)
    elif resource_type == 'dynamodb':
        response = client.list_tables()
        for table_name in response['TableNames']:
            resources.append(table_name)


    # ... your existing resource listing code ...

    return resources

# ... your existing functions ...

def get_last_activity_timestamp(resource_type, resource_id, cloudtrail_client):
    response = cloudtrail_client.lookup_events(
        LookupAttributes=[
            {
                'AttributeKey': 'ResourceName',
                'AttributeValue': resource_id
            },
            {
                'AttributeKey': 'ResourceType',
                'AttributeValue': resource_type
            }
        ],
        MaxResults=1,
    )

    if 'Events' in response and len(response['Events']) > 0:
        event = response['Events'][0]
        return event['EventTime']

    return None
  



def main():
    region = 'eu-north-1'
    # Initialize Boto3 clients for different services
    ec2_client = boto3.client('ec2', region_name=region)
    s3_client = boto3.client('s3', region_name=region)
    rds_client = boto3.client('rds', region_name=region)
    lambda_client = boto3.client('lambda', region_name=region)
    dynamodb_client = boto3.client('dynamodb', region_name=region)
    cloudtrail_client = boto3.client('cloudtrail', region_name=region)

    # List AWS resources
    ec2_resources = list_resources('ec2', ec2_client)
    s3_resources = list_resources('s3', s3_client)
    rds_resources = list_resources('rds', rds_client)
    lambda_resources = list_resources('lambda', lambda_client)
    dynamodb_resources = list_resources('dynamodb', dynamodb_client)

    # Print the details of resources with last activity timestamp
    print("EC2 Instances:")
    for resource in ec2_resources:
        last_activity_time = get_last_activity_timestamp('EC2', resource['InstanceId'], cloudtrail_client)
        print("Resource:", resource)
        print("Last Activity Timestamp:", last_activity_time)
        print("\n")

    print("S3 Buckets:")
    for resource in s3_resources:
        last_activity_time = get_last_activity_timestamp('S3', resource['Name'], cloudtrail_client)
        print("Resource:", resource)
        print("Last Activity Timestamp:", last_activity_time)
        print("\n")

    print("RDS Instances:")
    for resource in rds_resources:
        last_activity_time = get_last_activity_timestamp('RDS', resource['DBInstanceIdentifier'], cloudtrail_client)
        print("Resource:", resource)
        print("Last Activity Timestamp:", last_activity_time)
        print("\n")

    print("Lambda Functions:")
    for resource in lambda_resources:
        last_activity_time = get_last_activity_timestamp('Lambda', resource['FunctionName'], cloudtrail_client)
        print("Resource:", resource)
        print("Last Activity Timestamp:", last_activity_time)
        print("\n")

    print("DynamoDB Tables:")
    for resource in dynamodb_resources:
        last_activity_time = get_last_activity_timestamp('DynamoDB', resource, cloudtrail_client)
        print("Resource:", resource)
        print("Last Activity Timestamp:", last_activity_time)
        print("\n")

if __name__ == "__main__":
    main()

