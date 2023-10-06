---
title: "Setup and run the client frontend"
chapter: true
weight: 3
---

## Introduction
In this step we will be learning how to :
- Understanding the functionalities of the FX price client application
- Install the following on an EC2 instance:
    - Docker compose
- Modify the configuration properties as required
- Build and run the client application
- Walk through the application

### Understand the functionalities of the FX price client application
In this workshop, our primary use case involves an edge broker that provides FX pricing to client desktop and mobile devices for easy access and review.

Users are divided into different categories (categories 1-4) based on the refresh rates of the data they receive. \
This rate limiting is implemented using the concept of Direct Messaging Eliding backed by client profiles with the corresponding message delays. 

> Run the below steps in a new terminal in the Cloud9 environment. Do not stop the admin application that we deployed in the previous step

### Step 1 : Installing development tools
To build and run the client application, you will need some development tools namely :

#### Docker

To start the Docker service, run `sudo service docker start`.

#### Docker compose
Following are the set of commands need to be executed sequentially to install Docker compose :

`sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose`

`sudo chmod +x /usr/local/bin/docker-compose`

To verify the installation, run `docker-compose version`.

### Step 2 : Codebase of the frontend application
The frontend application is already checked out and present within the repository that you cloned in the earlier step.

Navigate to the directory : solace-aws-integration/solace-quoteappdemo-frontend

### Step 3 : Modifying configuration properties
Similar to the Admin application, you will have to update some of the configuration properties that are required for the application to connect and start off. \
The properties file can be found at the location in the browser : solace-aws-integration/solace-quoteappdemo-frontend/src/environments \
Change the following parameters with the values that you have collected earlier in **Credentials and required connection details - Section 2 - Step 2**
- host : Public Endpoint
- vpn : Message VPN
- clientUserName : Username
- clientPassword : Password 
- uri : The public IP of the Cloud9 EC2 instance. You should be using the same IP that you used in the previous step for the Administration application
![Edit Frontend application properties](/images/moduleTwo/edit-fe-app-properties.png)

### Step 4 : Build and run the Administration application
Build and run the application using the command  : `sudo docker-compose up --build`

Once the application shows up as started, you can hit the different urls of the client applications like below :
- Refresh rate - 1 : [http://EC2_PUBLIC_IP:7888/?elidingType=level1](http://EC2_PUBLIC_IP:7888/?elidingType=level1)
- Refresh rate - 2 : [http://EC2_PUBLIC_IP:7888/?elidingType=level2](http://EC2_PUBLIC_IP:7888/?elidingType=level2)
- Refresh rate - 3 : [http://EC2_PUBLIC_IP:7888/?elidingType=level3](http://EC2_PUBLIC_IP:7888/?elidingType=level3)
- Refresh rate - 4 : [http://EC2_PUBLIC_IP:7888/?elidingType=level4](http://EC2_PUBLIC_IP:7888/?elidingType=level4)


