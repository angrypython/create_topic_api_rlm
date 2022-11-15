import requests
import urllib3
import logging
import datetime
param_list = []

def get_params_run():

    return param_list

def post_to_api(url, head,  param):
    urllib3.disable_warnings()
    r = requests.post ( url, headers=head, param=param)
    if str(r.status_code) == '200':
        print('sucsses')
    else:
        print('fail')

if __name__ == 'main':
    post_to_api(param1, param2, get_params_run())