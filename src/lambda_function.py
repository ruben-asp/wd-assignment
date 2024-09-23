import json
from init import rootObject, postObject, resource_not_found

def lambda_handler(event, context):
    # TODO implement
    http_resources = {
            "/" : rootObject,
        "/{id}" : postObject
    }

    return http_resources.get(event['resource'], resource_not_found) (event)

