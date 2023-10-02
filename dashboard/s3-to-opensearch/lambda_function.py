import boto3
import datetime
from opensearchpy import OpenSearch, RequestsHttpConnection, AWSV4SignerAuth
from requests_aws4auth import AWS4Auth


#convert csv string to json
def csvToJson(csvStr):
    #split string into array
    csvArr = csvStr.split('|')

    if len(csvArr) < 12:
        print('wrong csv string')
        return
    
    #create json object from csvArr
    document = {
        'id': csvArr[0],
        'ticker': csvArr[1],
        'displayName': csvArr[2],

        'pOpen': float(csvArr[4]),
        'pHigh': float(csvArr[5]),
        'pLow': float(csvArr[6]),
        'pClose': float(csvArr[7]),
        'pDiff': float(csvArr[8]),
        'vCurrent': int(csvArr[9]),
        'vTotal': int(csvArr[10]),
        'time': csvArr[11]  
    } 

    document['time'] = datetime.datetime.utcfromtimestamp(int(document['time'])/1000)    
    return document

#test function
# example: 2|id:ACABU|displayName:Atlantic Coastal Acquisition Corp II|symbolOrderId:2|pOpen:41,10|pHigh:41,10|pLow:31,75|pClose:31,75|pDiff:-9,35|vCurrent:9|vTotal:13|lastUpdated:1696245667261
def test():
    test_string = '264231599|AAPL|Apple Inc|13210197|52.20|57.95|47.20|56.25|4.05|4|66038700|1695876055726'
    document=csvToJson(test_string)
    print(document)


#test()

s3 = boto3.client('s3')



region = 'ap-northeast-1' # The region for the OpenSearch service.
service = 'aoss'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)


# the OpenSearch Service endpoint , e.g. https://search-mydomain.ap-northeast-1.aoss.amazonaws.com
host = 'zxs41l7or0vtsq9lzh3l.ap-northeast-1.aoss.amazonaws.com' 
index_name = 'solace-index'

client = OpenSearch(
    hosts = [{'host': host, 'port': 443}],
    http_auth = awsauth,
    use_ssl = True,
    verify_certs = True,
    connection_class = RequestsHttpConnection,
    pool_maxsize = 20
)


# Lambda function entery point
def lambda_handler(event, context):
    for record in event['Records']:

        # Get the bucket name and key for the new file
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        # Get, read, and split the file into lines
        obj = s3.get_object(Bucket=bucket, Key=key)
        body = obj['Body'].read()
        lines = body.splitlines()

        #The current data file has only one line.  Just in case, we define the loop here so that even it has multiple lines, it still works
        for line in lines:
            line = line.decode("utf-8")
            document=csvToJson(line)
            print(document)
            r = client.index(
                index = index_name,
                body = document,

               # refresh = True
                )
            print(r)
