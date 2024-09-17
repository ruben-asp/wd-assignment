import json, uuid
from endpoints import Endpoints

class postEndpoint(Endpoints):
    def __init__(self, dbDynamoClient, tableName ):
        Endpoints.__init__(self, dbDynamoClient, tableName )
        self.http_methods = {
            "GET" : self.get_item,
            "PATCH" : self.edit_item,
            "DELETE" : self.delete_item,
        }
        
    def get_item(self, event):
        """
        This function reads one item from dynamodb table
        Returns
        -------
        
            Response Dictionary
        """
        id = event.get("pathParameters", {}).get("id", "")
        if id in ["", "{id}"]:
            return {
            'statusCode': 400,
            'body': json.dumps({ 'message': 'Missing body' })
            }

        
        response = self.dbDynamoClient.get_item( 
            TableName = self.tableName,
            Key= {"pk": {"S" :id } }
        )
        
        if "Item" in response:
            item = response["Item"]
            return { 'statusCode': 200, 'body': json.dumps({"pk":item['pk']['S'], "body": json.loads(item['body']['S'])}) }

        return { 'statusCode': 400, 'body': '{}' }

    def edit_item(self, event):
        """
        This function edits one item from dynamodb table
        Returns
        -------
        
            Response Dictionary
        """
        id = event.get("pathParameters", {}).get("id", "")
        if id in ["", "{id}"] or not event.get('body'):
            return {
            'statusCode': 400,
            'body': json.dumps({ 'message': 'Missing parameters' })
            }

        response = self.dbDynamoClient.update_item( 
            TableName = self.tableName,
            Key= {"pk": {"S" :id } },
            ExpressionAttributeNames={
                '#B': 'body'
            },            
            ExpressionAttributeValues={
                ':b': { "S" : str(event['body']) }
            },            
            UpdateExpression = 'SET #B = :b',
            ReturnValues = 'ALL_NEW'
        )
        
        if "Attributes" in response:
            item = response["Attributes"]
            return { 'statusCode': 200, 'body': json.dumps({"pk":item['pk']['S'], "body": json.loads(item['body']['S'])}) }

        return { 'statusCode': 400, 'body': '{}' }


    def delete_item(self, event):
        """
        This function deletes one item from dynamodb table
        Returns
        -------
        
            Response Dictionary
        """
        id = event.get("pathParameters", {}).get("id", "")
        if id in ["", "{id}"]:
            return {
            'statusCode': 400,
            'body': json.dumps({ 'message': 'Missing body' })
            }

        
        response = self.dbDynamoClient.delete_item( 
            TableName = self.tableName,
            Key= {"pk": {"S" :id } },
            ReturnValues = 'ALL_OLD'
        )
        
        if "Attributes" in response:
            item = response["Attributes"]
            return { 'statusCode': 200, 'body': json.dumps({"pk":item['pk']['S'], "body": json.loads(item['body']['S'])}) }

        return { 'statusCode': 400, 'body': '{}' }