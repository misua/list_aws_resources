# list_aws_resources
List whatever resources is still being used in your aws account.


b.py - cli output [you can still dump the output in a file]

c.py - csv output.

pls see screenshot.


Instructions:
  you need to edit the resources you need listed,so if you are executing this script as a user, make sure it has permissions to query those services like s3 or rds, i usually just add ALL permissions to that specific user during the duration of the script execution.

this will NOT automatically just list all you want. review and edit script and copy paste (replacing the resource)

examples: 

 elif resource_type == 'lambda':  //lambda
        response = client.list_functions()
        for function in response['Functions']:
            resources.append(function)
    elif resource_type == 'dynamodb':  //dynamodb
        response = client.list_tables()
        for table_name in response['TableNames']:
            resources.append(table_name)
