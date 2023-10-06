---
title: "S3 bucket"
chapter: true
weight: 1 
---

## Introduction
In this section we will be locating the S3 bucket and the credentials required for the connector to work with

### S3 Bucket
The S3 bucket has already been created as a part of the workshop setup and can be found at your Amazon S3 services screen

###  Access key/access-key-secret
To be able to persist items to the newly created bucket, we will be using the Solace-S3 native connector. \
This native connector requires an access-key and its secret which has already been set up as a part of the cloudformation template which was executed during the ramp up of the workshop.\
The access key and secret access key can be retrieved from the cloudformation template output log.

