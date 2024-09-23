import json, uuid

class Endpoints():
    def __init__(self, dbDynamoClient, tableName ):
        self.dbDynamoClient = dbDynamoClient
        self.tableName = tableName
        self.http_methods = {}
        
    def run(self, event):
        if event['httpMethod'] == "OPTIONS": return self.http_response()

        return self.http_methods.get(event['httpMethod'], self.not_found) (event)

    def not_found(self, event):
        return self.http_response( body=event, statusCode=400 )

    def resource_not_found(self, event):
        return self.http_response( body={"messsage" : "Resource not found" }, statusCode=400 )

    def http_response(self, body={}, statusCode=200):
        return {
            'headers': {
                "Access-Control-Allow-Headers": "*",
                "Access-Control-Allow-Methods": "OPTIONS,GET,POST,PATCH,PUT,DELETE",
                "Access-Control-Allow-Origin": "*",
                "content-type": "application/json"
            },
            'multiValueHeaders':{},
            'isBase64Encoded': False,
            'statusCode': statusCode,
            'body': json.dumps(body)
        }

