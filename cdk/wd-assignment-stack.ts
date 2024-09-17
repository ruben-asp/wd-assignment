import { Stack, StackProps, RemovalPolicy, IgnoreMode } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { AttributeType, Table, BillingMode } from 'aws-cdk-lib/aws-dynamodb';
import { Cors, LambdaIntegration, RestApi} from 'aws-cdk-lib/aws-apigateway';
import * as lambda from "aws-cdk-lib/aws-lambda";

const project_name = `WD-Assignment`;

export class WDAssignmentStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    // 1. Create our DynamoDB table
    const dbTable = new Table(this, `${project_name}-DbTable`, {
      partitionKey: { name: 'pk', type: AttributeType.STRING },
      removalPolicy: RemovalPolicy.DESTROY,
      billingMode: BillingMode.PAY_PER_REQUEST,
      tableName:`${project_name}-DbTable`
    });

    // 2. Create our API Gateway
    const api = new RestApi(this, `${project_name}-RestAPI`, {
      restApiName: `${project_name}-RestAPI`,
      defaultCorsPreflightOptions: {
        allowOrigins: Cors.ALL_ORIGINS,
        allowMethods: Cors.ALL_METHODS,
      },
      //apiKeySourceType: ApiKeySourceType.HEADER,
    });

    // 5. Create our Lambda functions to handle requests
    const postsLambda = new lambda.Function(
      this,
      `${project_name}-Lambda`,
      {
        runtime: lambda.Runtime.PYTHON_3_12,
        code: lambda.Code.fromAsset(`src`, {
          //exclude: ignoreSettings.ignoreFiles,
          ignoreMode: IgnoreMode.GIT,
        }),
        handler: `lambda_function.lambda_handler`,
        environment: {
          TABLE_NAME: dbTable.tableName,
        },
        functionName: `${project_name}-Lambda`,
      }
    );
    
    // 6. Grant our Lambda functions access to our DynamoDB table
    dbTable.grantReadWriteData(postsLambda);
    //dbTable.grantReadWriteData(postLambda);

    // 7. Define our API Gateway endpoints
    const posts = api.root //.addResource('{id}');
    const post = posts.addResource('{id}');

    // 8. Connect our Lambda functions to our API Gateway endpoints
    const postsIntegration = new LambdaIntegration(postsLambda);
    //const postIntegration = new LambdaIntegration(postLambda);

    //const namespace = posts.addResource('{proxy+}', { defaultIntegration:postsIntegration })
    //const proxyResource = new posts.ProxyResource(this, `{proxy+}`, {
    //  anyMethod: true,
    //})
    //proxyResource.addMethod("ANY", postsIntegration)
    
    // 9. Define our API Gateway methods
    
    // To list or create new items
    posts.addMethod('GET', postsIntegration, {
      apiKeyRequired: false,
    });
    posts.addMethod('POST', postsIntegration, {
      apiKeyRequired: false,
    });

    // To manipulate existing items
    post.addMethod('DELETE', postsIntegration, {
      apiKeyRequired: false,
    });
    post.addMethod('GET', postsIntegration, {
      apiKeyRequired: false,
    });
    post.addMethod('PATCH', postsIntegration, {
      apiKeyRequired: false,
    });
    
  }
}
