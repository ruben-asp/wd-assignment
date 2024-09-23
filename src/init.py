import json, boto3, uuid
from os import environ as env
dynamodb = boto3.client('dynamodb')

from rootEndpoint import rootEndpoint
from postEndpoint import postEndpoint

rootObject = rootEndpoint(dynamodb, env['TABLE_NAME']).run
postObject = postEndpoint(dynamodb, env['TABLE_NAME']).run
resource_not_found = rootEndpoint(dynamodb, env['TABLE_NAME']).resource_not_found

