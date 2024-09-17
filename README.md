# WD Assignment
Take-Home Assignment: Simple Microservice with AWS Integration

Project Details
====================
This is a very simple CRUD application demo that runs in the AWS Cloud. It has a stack that includes the next AWS Services:
- DynamoDB Database
- Lambda function
- API Gateway 

It also includes:
- Python 3.12 code on Lambda logic
- Node.JS 20.17 on CDK infrastructure-as-code deployment script
- Postman collection and environment for API Testing
- A running live demo (link below)

Challenges and considerations
==============================
This demo is focused on the AWS stack creation and the basic CRUD functionalities of a REST API. So, to make it simpler, here are some points to consider:
- The structure of the database records consist of a primary key (pk) and a body that can by any JSON formatted string. (See the Testing Section below)
- The use of AWS Services such as DynamoDB, Lambda and API Gateway was kept simpler as possible. Many other features can be enabled on those services to have a more robust and secure application.
- The python code has a basic structure to handle the CRUD functionalities. This is considered a very small application that required just a custom python code. But for a REST API with more functions and more logic the use of well known python frameworks such as FastAPI, Flask or Django is strongly recommended.

System/Deployment Requirements
================================
It has a CDK deployment script, so the deployment to AWS Cloud can be from any system that meets the system requirements mentioned next.

- AWS Account
- AWS SAM CLI with credentials properly cofigured 
- CDK
- Node.JS ~20.17
- Python 3.12 (Optional, for lambda code edition only)

Deployment Instructions
=========================
- Using a terminal, move to your repo clone folder:
-   Update the project's node libraries with: 
-       npm i
-   Synthetise the CDK Project:
-       cdk synth
-   Deploy the Stack
-       cdk deploy
-   At the bottom of the CDK deployment output you will see the endpoint URL, something similar to: 
-       https://<some-unique-string>.execute-api.<your-aws-zone>.amazonaws.com/prod/
-   ...write it down.
-   To verify the correct installation just use your new url directly on your browser, you should see a empty screen with status 200 because of the empty database.

Testing
=========
This project includes a Postman collection to test each of the CRUD API functions. A running version of this system its already configured in the postman's environment file also included.

For any other API Client, here are the resources supported by this application:
- List all items:
-       GET your-base-url/
- List one item:
-       GET your-base-url/<item-pk>
- Create o new item:
-       POST your-base-url/
        body: Any JSON formatted payload
- Edit one item:
-       PATCH your-base-url/<item-pk>
        body: Any JSON formatted payload
- Delete one item:
-       DELETE your-base-url/<item-pk>

All body requirements ( POST and PATCH ) consist of a JSON formatted string. Primary Keys (pk) are automatically generated and they are used on functions that require specific item localization ( GET, PATCH and DELETE ).

A running version of this app is ready for testing at: 
https://r6gv75i2rc.execute-api.us-east-1.amazonaws.com/prod/

Uninstallation
=============================
- Using a terminal, move to your folder:
-       cdk destroy

