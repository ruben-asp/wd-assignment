import json, uuid
from endpoints import Endpoints

class rootEndpoint(Endpoints):
    def __init__(self, dbDynamoClient, tableName ):
        Endpoints.__init__(self, dbDynamoClient, tableName )
        self.http_methods = {
            "GET" : self.get_all,
            "POST" : self.insert_data,
        }
        
    def get_all(self, event):
        """
        This function reads all data from dynamodb table
        Returns
        -------
        
            Response Dictionary
        """
        response = self.dbDynamoClient.scan( TableName = self.tableName )
        
        return self.http_response (
            body = [ {"pk":item['pk']['S'], "body": json.loads(item['body']['S'])} for item in response.get('Items', []) ]
        )
        
        #return {
        #    'statusCode': 200,
        #    'body': json.dumps([ {"pk":item['pk']['S'], "body": json.loads(item['body']['S'])} for item in response.get('Items', []) ])
        #}    

    def insert_data(self, event):
        """
        This function inserts an item to the dynamodb table
        Returns
        -------
        Dictionary
            Response Dictionary
        """
        if not event.get('body'):
            return self.http_response( body = { 'message': 'Missing body' }, statusCode=400 )
            #return { 'statusCode': 400, 'body': json.dumps({ 'message': 'Missing body' }) }
        
        #with put_item function we insert data in Table
        response = self.dbDynamoClient.put_item (
            TableName = self.tableName,
            Item = { 
                    'pk': { "S" : str(uuid.uuid4()) }, 
                  'body': { "S" : str(event['body']) }
            },
            ReturnValues = 'ALL_OLD'
        )
    
        return self.http_response( statusCode= response.get("ResponseMetadata", {}).get("HTTPStatusCode", 400) )
        #return { 'statusCode': response.get("ResponseMetadata", {}).get("HTTPStatusCode", 400), 'body': '{}' }
        
