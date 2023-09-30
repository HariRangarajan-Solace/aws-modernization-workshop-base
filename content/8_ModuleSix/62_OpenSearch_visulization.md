---
title: "Create visualization in Open Search"
chapter: true
weight: 2 
---

## Introduction
Since the data is being ingested into the OpenSearch serverless 'collection', The goal of this section is to create a Histogram visualization of stock price, that can be refreshed in (semi) real time.

1. Go to OpenSearch console, find and open the Dashboard URL. Since the cloud formation template has set up the IAM policy, you should be able to open the dashboard. 

![OpenSearch Console](/images/moduleSix/AmazonOpenSearchConsole.png)

If you want to learn more about OpenSearch dashboard, please go to [official documentation](https://opensearch.org/docs/2.0/dashboards/dashboard/index/). In this section, we'll quickly go through the steps to create a visulization capability called "Histogram"

2. Now, you can explore and validate the "solace-index" is ingested with data, by going into the hamburger menu of OpenSearch, choose "Dev Tools". Input and run the following code:
```json
GET solace-index/_search
{
  "query": {
     "match_all": { 
     }
  }
}
```
You should see the data that are ingested already as following:
![Dev Tool to query the index](/images/moduleSix/OpenSearchDevTools.png)

3. Before createing visualization, the Index Pattern is required. Go to the humburger menu, choose **Stack Management**, choose **Index Patterns**, then click **Create index pattern**
In the following screen, input:
Index pattern name = solace*

![Create the Index Pattern](/images/moduleSix/OpenSearchCreateIndexPattern.png)

In next screen, choose the **Time field** (Here, _time_ is a colume, representing the epoch time of the stock price record), then **Create index pattern**

![Select the Time Field](/images/moduleSix/OpenSearchCreateIndexPatternTimeField.png)

4. Go to the hamburger menu, choose **Visualize**, and then **Create visualization**. Choose **Area** type from the visualization options
![Choose Area Type Visualization](/images/moduleSix/OpenSearchNewVisualization.png)

5. Choose "solace*" as your source, then add a filter with the following parameter
* Field == "ticker"
* Operator == "is"
* Value == "AAPL" (means APPLE Stock)
This step would filter all stock data from APPLE stock.
![Define Area Chart Filter](/images/moduleSix/OpenSearchVisualizationFilter.png)


6. Now define Y-axis configuration
* Aggregation == "Average"
* Field == "price_end"
* Customer label = "Price"
![Define Y-Axis](/images/moduleSix/OpenSearchYAxis.png)

7. Click **Buckets**, then **X-axis**, Then define the X-axis configuration
* Aggregation == "Date Histogram"
* Field = "time"
* Minimum interval == "Second"
This will display the stock price in every minute

![Define X-Axis](/images/moduleSix/OpenSearchXAxis.png)

8. Now go to the "Metrics & axes" tab, to fine tune the axes definition 
* Mode == "Normal"
* Scale to data bounds == enable

![Define Axes](/images/moduleSix/OpenSearchVisualizationAxes.png)

9. Now, you'll get the area chart of the stock market. which you can set the refresh frequency
You'll see the stock price refreshed in semi real time, as data is ingested from Solace event mesh
![Define refresh frequency](/images/moduleSix/OpenSearchVisualizationRefreshConfig.png)


