import boto3
import re
import requests
from requests_aws4auth import AWS4Auth



#convert csv string to json
def csvToJson(csvStr):
    #split string into array
    csvArr = csvStr.split('|')
    #create json object
    jsonObj = {}
    #add each array element to json object
    for i in range(len(csvArr)):
        jsonObj[i] = csvArr[i]
    #return json object
    return jsonObj

#test function
def test():
    test_string = '1306|AAPL|Apple Inc|63|52,20|52,25|52,20|52,25|0,05|1|345|1684234176731'
    document=csvToJson(test_string)
    print(document)


#test()

region = 'us-east-1' # e.g. us-west-1
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

host = 'https://zrf9yyk8q2vne4ae5cab.us-east-1.aoss.amazonaws.com' # the OpenSearch Service domain, e.g. https://search-mydomain.us-west-1.es.amazonaws.com
index = 'lambda-s3-index'
datatype = '_doc'
url = host + '/' + index + '/' + datatype

headers = { "Content-Type": "application/json" }

s3 = boto3.client('s3')




# Regular expressions used to parse some simple log lines
#ip_pattern = re.compile('(\d+\.\d+\.\d+\.\d+)')
#time_pattern = re.compile('\[(\d+\/\w\w\w\/\d\d\d\d:\d\d:\d\d:\d\d\s-\d\d\d\d)\]')
#message_pattern = re.compile('\"(.+)\"')




# Lambda execution starts here
def handler(event, context):
    for record in event['Records']:

        # Get the bucket name and key for the new file
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        # Get, read, and split the file into lines
        obj = s3.get_object(Bucket=bucket, Key=key)
        body = obj['Body'].read()
        lines = body.splitlines()

        # Match the regular expressions to each line and index the JSON
        for line in lines:
            line = line.decode("utf-8")
            document=csvToJson(line)
            print(document)
            r = requests.post(url, auth=awsauth, json=document, headers=headers)
            print(r.text)
