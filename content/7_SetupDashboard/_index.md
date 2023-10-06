---
title: "6. Set up dashboard"
chapter: true
weight: 7
---

# Set up Elastic Dashboard

Typically, a customer who use adopts Solace on cloud would first utilize Solace as an infrastructure to ingest large amount of data from On-Prem applications (such as Mainframe) to cloud, and then develop use cases, such as data lake, data analytics. In this workshop, we will use OpenSearch (ELK) and Kibana as the data visualization.

The following is a simple architecture. S3 bucket and OpenSearch Serverless are already set up by CloudFormation template. What we will do in this section is:

1. Configure Lambda function, that ingest data to OpenSearch, to be indexed in real time
2. Set up visualization in OpenSearch Dashboard


![Dash board architecture](/images/moduleSix/workshop-dashboard-architecture.png)