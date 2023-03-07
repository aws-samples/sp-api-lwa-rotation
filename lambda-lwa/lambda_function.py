from __future__ import print_function
import json

import requests
import boto3

ssm = boto3.client('ssm', 'us-east-2')


def get_parameters():
    response = ssm.get_parameters(
        Names=['/my-erp/lwa/cliensecret', "/my-erp/lwa/clientidentifier", "/my-erp/refreshToken"], WithDecryption=True
    )

    payload = {'grant_type': 'refresh_token',
               'client_secret': response['Parameters'][0]["Value"],
               'client_id': response['Parameters'][1]["Value"],
               'refresh_token': response['Parameters'][2]["Value"]}
    lwa = requests.post("https://api.amazon.com/auth/o2/token", data=payload)

    return lwa.text


def lambda_handler(event, context):
    value = get_parameters()
    print("lwa value =  " + value)
    return value  # Echo back the first key value
