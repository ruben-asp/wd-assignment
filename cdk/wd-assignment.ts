#!/usr/bin/env node
//import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { WDAssignmentStack } from './wd-assignment-stack';

const app = new cdk.App();
new WDAssignmentStack(app, 'WDAssignmentStack', {});
