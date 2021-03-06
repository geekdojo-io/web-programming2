import json
from botocore.vendored import requests

print('Loading function')

def lambda_handler(event, context):
    
    URL = '[YOUR_SLACK_INCOMING_WEBHOOK_URL]'
    message = 'Hello from AWS Lambda'
    data = '{{"text":"{}"}}'.format(message)
    response = requests.post(URL, data=data, headers={'Content-Type': 'application/json'})
    
    print('Response: ' + str(response.text))
    print('Response code: ' + str(response.status_code))
    
    return {
        'statusCode': response.status_code,
        'body': response.text
    }
