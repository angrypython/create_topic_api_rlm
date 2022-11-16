#!/bin/python3
import requests
import urllib3
import argparse
import datetime
import json
def split_dict(in_dict):
    cor_heads=('url', 'Authorization', 'accept', 'Content-Type')
    cor_params=('action', 'ak_topic', 'ak_replication_factor', 'ak_partitions', 'ak_security', 'ak_port', 'ak_topic_config', 'user_email', 'env_type')
    cor_when=('start_at', 'service', 'datetime')
    cor_items=('invsvm_ci_svm', 'invsvm_ip')
    heads = {}
    params = {}
    when = {}
    items = {}
    for i in in_dict:
        if i in cor_heads:
            heads[i] = in_dict[i]
        elif i in cor_params:
            params[i] = in_dict[i]
        elif i in cor_when:
            when[i] = in_dict[i]
        elif i in cor_items:
            items[i] = in_dict[i]
    return [heads, params, when, items]
def get_params_run():
    mainparser = argparse.ArgumentParser(description="Arguments for create topics to kafka")

    mainparser.add_argument("-url", dest="url", default='https://rlm.sigma.sbrf.ru/api/tasks/')
    mainparser.add_argument("-authorization", dest="Authorization", default='token')
    mainparser.add_argument("-accept", dest="accept", default='application/json')
    mainparser.add_argument("-content_type", dest="Content-Type", default='application/json')

    mainparser.add_argument("-action", dest="action", default='aktag_create_topic,aktag_modify_topic')
    mainparser.add_argument("-ak_topic", dest="ak_topic", default='test4api')
    mainparser.add_argument("-ak_replication_factor", dest="ak_replication_factor", type=int, default=1)
    mainparser.add_argument("-ak_partitions", dest="ak_partitions", type=int, default=1)
    mainparser.add_argument("-ak_security", dest="ak_security", default='SSL')
    mainparser.add_argument("-ak_port", dest="ak_port", type=int, default='9093')
    mainparser.add_argument("-ak_topic_config", dest="ak_topic_config", default=[])
    mainparser.add_argument("-user_email", dest="user_email", default='user@example.com')
    mainparser.add_argument("-env_type", dest="env_type", default='TEST')

    mainparser.add_argument("-start_at", dest="start_at", default='now')
    mainparser.add_argument("-service", dest="service", default='createtopicKafka')
    mainparser.add_argument("-datetime", dest="datetime", default=datetime.datetime.utcnow().isoformat())

    mainparser.add_argument("-invsvm_ci_svm", dest="invsvm_ci_svm", default='CI04340141')
    mainparser.add_argument("-invsvm_ip", dest="invsvm_ip", default='10.56.165.201')

    return split_dict(vars(mainparser.parse_args()))

def post_to_api(all):
    heads = all[0]
    if heads['Authorization'] == 'token':
        heads['Authorization'] = input('enter your token: ')
    body = {}
    body['params'] = all[1]
    body = {**body, **all[2]}
    buff = []
    buff.append(all[3])
    body['items'] = buff
    urllib3.disable_warnings()
    json_object = json.dumps(body, indent=4)
    r = requests.post(url=heads.pop('url'), headers=heads, data=json_object, verify=False)    
    print(r.status_code)
    print(r.content)
    if r.status_code != '200':
        exit('ERROR: RLM returned an answer not 200')
    
if __name__ == '__main__':
    print(get_params_run())
    post_to_api(get_params_run())
