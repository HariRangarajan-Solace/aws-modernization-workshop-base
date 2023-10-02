---
title: "S3 bucket setup"
chapter: true
weight: 1 
---

## Introduction
In this section we will be an access-key/access-key-secret for the next step.

### Creating access key/access-key-secret
To be able to persist items to the newly created bucket, we will be using the Solace-S3 native connector. \
This native connector requires an access-key and its secret which we will be setting up now.

- Open the [IAM page](https://us-east-1.console.aws.amazon.com/iamv2) of the console
- Click on the **Users** link on the Access Management menu on the left
- Click on the user : **solaceS3Connector**
- Goto the **Security Credentials** tab in the central pane
- Scroll down to the **Access keys** section and click on **Create access key**
- Create an access key pair which consists of an access key and the secret access key
- Copy the pair and store it securely for the next step

