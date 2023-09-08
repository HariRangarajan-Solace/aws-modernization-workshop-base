---
title: "Create visualization in Open Search"
chapter: true
weight: 1 
---

## Introduction
Since the data is being ingested into the OpenSearch serverless 'collection', The goal of this section is to create a Histogram visualization of stock price, that can be refreshed in (semi) real time.

1. Go to OpenSearch console, find and open the Dashboard URL. Since the cloud formation template has set up the IAM policy, you should be able to open the dashboard. 

![OpenSearch Console](/images/moduleSix/AmazonOpenSearchConsole.png)

If you want to learn more about OpenSearch dashboard, please go to [official documentation](https://opensearch.org/docs/2.0/dashboards/dashboard/index/). In this section, we'll quickly go through the steps to create a visulization capability called "Histogram"

2. Go to the hamburger menu of OpenSearch, choose "Visualize", and then "Create visualization"

3. Choose "Area" type from the visualization options
![Choose Area Type Visualization](/images/moduleSix/OpenSearchNewVisualization.png)

4. Choose "solace-index" as your source

5. Add a filter with the following parameter
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

7. Click "Buckets", then "X-axis"

8. Define the X-axis configuration
* Aggregation == "Date Histogram"
* Field = "time_readable"
* Minimum interval == "Minute"
This will display the stock price in every minute
![Define Y-Axis](/images/moduleSix/OpenSearchXAxis.png)

8. Now go to the "Metrics & axes" tab, to fine tune the axes definition 
* Mode == "Normal"
* Scale to data bounds == enable

![Define Axes](/images/moduleSix/OpenSearchVisualizationAxes.png)

9. Now, you'll get the area chart of the stock market. which you can set the refresh frequency
You'll see the stock price refreshed in semi real time, as data is ingested from Solace event mesh
![Define refresh frequency](/images/moduleSix/OpenSearchVisualizationRefreshConfig.png)


