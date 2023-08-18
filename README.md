# list_aws_resources
### List whatever resources is still being used in your aws account.


b.py - cli output [you can still dump the output in a file]

c.py - csv output.

pls see screenshot.
<br />

**Instructions:** <br />
  1.] you need to edit the resources you need listed,so if you are executing this script as a user. <br />
  2.] make sure it has permissions to query those services like s3 or rds,lambda etc <br />
  
  tip - i usually just add ALL permissions to that specific user during the duration of the script execution.<br /> <br />

_This will NOT automatically just list all you want. review and edit script and copy paste <sup>(replacing the resource)<sup>_

examples: 
```python
 elif resource_type == 'lambda':  #lambda
        response = client.list_functions()
        for function in response['Functions']:
            resources.append(function)
    elif resource_type == 'dynamodb':  #dynamodb
        response = client.list_tables()
        for table_name in response['TableNames']:
            resources.append(table_name)
```

and in the main() part you will need to add these for every svcs

```python

lambda_resources = list_resources('lambda', lambda_client)
dynamodb_resources = list_resources('dynamodb', dynamodb_client)
```
