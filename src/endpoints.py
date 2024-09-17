import json, uuid

class Endpoints():
    def __init__(self, dbDynamoClient, tableName ):
        self.dbDynamoClient = dbDynamoClient
        self.tableName = tableName
        self.http_methods = {}
        
    def run(self, event):

        return self.http_methods.get(event['httpMethod'], self.not_found) (event)

    def not_found(self, event):
        return {
            'statusCode': 400,
            'body': json.dumps(event)
        }


