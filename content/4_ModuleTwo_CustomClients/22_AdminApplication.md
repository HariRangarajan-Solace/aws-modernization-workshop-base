---
title: "Setup and run Administration application"
chapter: true
weight: 2 
---

## Introduction

In this step we will  :

- Understand the functionalities of the Administration application
- Install the following on an EC2 instance:
    - Maven
- Modify the configuration properties as required
- Build and run the Administration application

### Understand the functionalities of the Administration application

In this workshop, our primary use case involves an edge broker that provides FX pricing to client desktop and mobile
devices for easy access and review.

Users are divided into different categories (categories 1-4) based on the refresh rates of the data they receive.

To enable this functionality, we have developed an Administration application. This application serves two main
purposes:

- It defines the stock symbols that will be displayed on the clients' devices
- It configures user profiles that determine the data refresh rates for each category of clients.

The data refresh rates for each category is implemented using a Solace broker feature called as Eliding. You can read
more about this feature over
here : [Message Eliding](https://docs.solace.com/Messaging/Direct-Msg/Direct-Messages.htm?Highlight=message%20eliding#Message-Eliding)

The _Administration_ application is a simple Java, Spring boot based MVC application which runs on the EC2 instance and
connects to the Solace broker (that you created in the previous module). \
It uses the [Solace Cloud v2 APIs ](https://api.solace.dev/cloud/reference/using-the-v2-rest-apis-for-pubsub-cloud) to
create client profiles supporting eliding which are used by the client application.

### Installing development tools

In the previous step, you had successfully connected to your EC2 instance using an SSH terminal.
To build and run the Administration application, you will need some development tools namely :

#### Maven

Following are the set of commands need to be executed sequentially to install Maven :

`sudo wget http://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -O /etc/yum.repos.d/epel-apache-maven.repo`

`sudo sed -i s/\$releasever/6/g /etc/yum.repos.d/epel-apache-maven.repo`

`sudo yum install -y apache-maven`

To verify the installation, run `mvn -v`

### Modifying configuration properties

At this stage you will have to update some of the configuration properties that are required for the application to
connect and start off.

Navigate to the location of the file : solace-aws-integration/solace-quoteengine-admin/src/main/resources/
![Edit Admin application properties](/images/moduleTwo/edit-admin-app-properties.png)

Enter the file using the command : `vi application.properties` \
Within the file, press `i` to enter the Insert mode \
Change the following parameters with the values that you have collected earlier in Module-1 :

- solace.semp.url : SEMP url collected in point# 2 of the **Initiator** broker
- solace.semp.username : SEMP username collected in point# 2 of the **Initiator** broker
- solace.semp.password : SEMP password collected in point# 2 of the **Initiator** broker
- solace.semo.brokername : SEMP message VPN name collected in point# 2 of the **Initiator** broker
- solace.restApiToken : API token for the Solace Cloud REST APIs
- server.ip : The public IP of the EC2 instance linked to the Cloud9 instance. You can find it by running the command curl `http://169.254.169.254/latest/meta-data/public-ipv4`
- solace.serviceId : The service id of the **Initiator** broker

### Build and run the Administration application

Navigate back to the root of the _solace-quoteengine-admin_ application using the following command : `cd solace-aws-integration/solace-quoteengine-admin/` \
Build and run the application using the command  : `mvn clean spring-boot:run`

Once the application shows up as started, you can hit the admin panel using the url :
[http://PUBLIC_IP_OF_THE_EC2_INSTANCE:8081/adminPanel](http://PUBLIC_IP_OF_THE_EC2_INSTANCE:8081/adminPanel)
and you should be able to see a screen similar to below:
![Solace QuoteApp Administration Portal](/images/moduleTwo/Solace-QuoteApp-Admin.png)

