---
title: "Event mesh integration" 
chapter: true
weight: 3 
---

## What is the Solace Event mesh

As we said before, the Solace event mesh is a flexible and unified architecture that connects applications, microservices, and distributed components.
As a part of this workshop, we will be linking the broker that you created in the previous step with the central _on-premise_ broker that has already been provisioned and made available to the participants.
This link will be bi-directional static link that allows events and messages to be passed between the two brokers.

Follow the steps below to create this static link :

1. Open the PubSub+ Broker Manager by clicking on the top-right button
![Broker Console - Open manager](/images/moduleOne/brokerconsole_openManager.png)

2. In the right-side menu, click on the "Bridge" button
![PubSub Manager - Bridge creation](/images/moduleOne/pubsubManager_bridges.png)

3. Click on the "Click to Connect" button on the top-right and enter the static bridges creation wizard
![Static Bridges - click to connect](/images/moduleOne/bridges_clickToConnect.png)

4. In the section titled _Remote Message VPN Management Credentials_, enter the SEMP hostname and credentials of the **Remote** broker which we defined in the section : **Credentials and required connection details - Section 1 - Step 1**.
![Click to connect - Remote Message VPN Management Credentials](/images/moduleOne/bridges_clickToConnect_Screen_1.png)
Click on the button _Select Remote Message VPN_

5. Select the retrieved remote vpn name as shown below and click on the button _Remote Connection Setup_
![Click to connect - Select Remote message VPN](/images/moduleOne/bridges_clickToConnect_Screen_2.png)

6. Make sure to fill in the details in this section very carefully as they are used to establish the connection.
   1. Remote Message VPN connection
      - Host list : Fill in the hostname of the **Remote** broker, this is detailed in the section : **Credentials and required connection details - Section 1 - Step 2**
   _Note: This field is pre-populated, but the actual port to be used is different. So make sure to use the proper hostname_ 
   2. Bridge Client for Remote Message VPN
       - Client Username : Select the value `solace-cloud-client` from the dropdown
       - Password : Fill in the password of the **Remote** broker, this is detailed in the section : **Credentials and required connection details - Section 1 - Step 2**
       - Confirm Password : Fill in the same value as above
   3. Bridge Client for Local Message VPN
      - Client Username : Select the value `solace-cloud-client` from the dropdown
      - Password : Fill in the password of the **Initiator** broker, this is detailed in the section : **Credentials and required connection details - Section 2 - Step 1**
      - Confirm Password : Fill in the same value as above
   4. Enable the button _TLS Enabled_
   ![Click to connect - Remote connection setup](/images/moduleOne/bridges_clickToConnect_Screen_3.png)
   Click on the button _Create Bridge and Test Connection_

7. If everything is fine, then a success page will be displayed as below.
![Click to connect - Bridge creation](/images/moduleOne/bridges_clickToConnect_Screen_4.png)

8. Click on the button _Set up Subscriptions_ where you can specify the topic subscription that you want to attract from the **Remote** broker
  - Specify the topic subscription `TW/TWSE/>`
  - Leave the topic direction as is
  - Select the `Direct` quality of service

![Click to connect - Setup subscriptions](/images/moduleOne/bridges_clickToConnect_Screen_5.png)
9. Click _Apply_


10. Create subscription on the  **Remote** broker \ 
    We will be using a simple postman collection that has been provided as a part of this demo.
    As a part of the prerequisites, you will have installed Postman tool which we will be using for making SEMP API calls to the remote broker. 
    1. Download the following files and save them to a folder of your preference :
       - [Postman Environment file](/postman_collection/Solace-AWS-Demo-Env.postman_environment.json "download")
       - [Postman Collection file](/postman_collection/Solace-AWS-Demo-Collection.postman_collection.json "download")
       
    2. Import the above two files into Postman app.
    3. Open the environment and adjust the variable **REMOTE_VPN_QUEUE_NAME** to what will be specific to you. The format of the queue name is:
  **YOUR_LOCAL_BROKER_NAME**_solace-aws-int-onprem_Queue. 
    4. Replace the name of your broker in the placeholder and set it in the **current** and **initial** value of the variable.
    ![Postman environment](/images/moduleOne/postman_env_screen_1.png)
    5. Open the Postman collection and run it to execute the request. Make sure to have the proper environment selected in the top-right corner.
    ![Postman Collection_screen 1](/images/moduleOne/postman_collection_screen_1.png)
    6. Run the collection and view the status of the request in the right column
    ![Postman Collection_screen 2](/images/moduleOne/postman_collection_screen_2.png)
    ![Postman Collection_screen 3](/images/moduleOne/postman_collection_screen_3.png)


With these steps you will have configured a full functional bidirectional VPN bridge between your new broker and a central **Remote** broker.
This VPN bridge will allow the governed flow of events between the two brokers subject to the topic subscriptions that you have set up. \
Lets move on the to the next step of the workshop.


