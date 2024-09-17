import json, boto3, uuid
from os import environ as env
dynamodb = boto3.client('dynamodb')

# Uncomment next line for lambda local/development execution
#env['TABLE_NAME'] = "WD-Assignment-DbTable" 

from rootEndpoint import rootEndpoint
from postEndpoint import postEndpoint

rootObject = rootEndpoint(dynamodb, env['TABLE_NAME']).run
postObject = postEndpoint(dynamodb, env['TABLE_NAME']).run

def not_found(event):

    return {
        'statusCode': 400,
        'body': json.dumps( {"messsage" : "Resource not found" } )
    }
