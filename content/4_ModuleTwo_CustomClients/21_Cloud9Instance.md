---
title: "Working with Cloud9 and EC2 instances" 
chapter: true
weight: 1 
---

## Introduction
In this step we will be using Cloud9 and its EC2 instance to deploy and run two custom applications for subscribing to and viewing our market data events.

### Cloud9 instance
AWS Cloud9 is a cloud-based integrated development environment (IDE) that lets you write, run, and debug your code with just a browser. \
We will be using a Cloud9 backed EC2 instance to deploy our applications and consume events from over the mesh. \
As a part of this workshop, you will have already got a Cloud9 subscription setup. You can find this in your Cloud9 environments screen. 



In this step we will be learning how to :
- Open ports on the EC2 instance to enable network connectivity to our applications.


1. Navigate to the Cloud9 Environments and enter the Cloud9 instance created for you as a part of this workshop named Solace-AWS-Cloud9
![Cloud9 Environments list](/images/moduleTwo/cloud9-environments-list.png)
2. Click on the **Manage EC2 Instance** button as shown
![Manage EC2 instance](/images/moduleTwo/Solace-AWS-cloud9.png)
3. Navigate to the Security Group attached to the EC2 instance as shown below
![Security group](/images/moduleTwo/ec2-instance-security-group.png)
4. Edit the inbound rules
![Edit inbound rules](/images/moduleTwo/edit-security-group.png)
5. Add in 8081 and 7888 as Custom TCP ports as below
![Add inbound ports](/images/moduleTwo/Add-inbound-ports.png)   