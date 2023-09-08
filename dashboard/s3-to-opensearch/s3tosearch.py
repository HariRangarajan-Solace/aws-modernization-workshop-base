import boto3
from opensearchpy import OpenSearch, RequestsHttpConnection, AWSV4SignerAuth
from requests_aws4auth import AWS4Auth



#convert csv string to json
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
        'name': csvArr[2],
        'volume': csvArr[3],
        'price_start': csvArr[4],
        'price_end': csvArr[5],
        'change': csvArr[8],
        'time': csvArr[11]  
    } 


    #convert fileds to numbers
    document['volume'] = int(document['volume'])
    document['price_start'] = float(document['price_start'].replace(',','.'))
    document['price_end'] = float(document['price_end'].replace(',','.'))
    document['change'] = float(document['change'].replace(',','.'))
    document['time'] = int(document['time'])    
    return document

#test function
# orderId | id | displayName | symbolOrderId | pOpen | pHigh | pLow | pClose | pDiff | vCurrent | vTotal | lastUpdated
def test():
    test_string = '1306|AAPL|Apple Inc|63|52,20|52,25|52,20|52,25|0,05|1|345|1684234176731'
    document=csvToJson(test_string)
    print(document)


#test()

region = 'us-east-1' # e.g. us-west-1
service = 'aoss'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

s3 = boto3.client('s3')

host = 'zrf9yyk8q2vne4ae5cab.us-east-1.aoss.amazonaws.com' # the OpenSearch Service domain, e.g. https://search-mydomain.us-west-1.es.amazonaws.com
index = 'solace-index'
datatype = '_doc'
url = host + '/' + index + '/' + datatype

headers = { "Content-Type": "application/json" }



client = OpenSearch(
    hosts = [{'host': host, 'port': 443}],
    http_auth = awsauth,
    use_ssl = True,
    verify_certs = True,
    connection_class = RequestsHttpConnection,
    pool_maxsize = 20
)




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


        for line in lines:
            line = line.decode("utf-8")
            document=csvToJson(line)
            print(document)
            # r = requests.post(url, auth=awsauth, json=document, headers=headers)
            r = client.index(
                index = 'solace-index',
                body = document,

               # refresh = True
                )
            print(r)
