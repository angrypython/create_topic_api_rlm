import requests
import urllib3
import argparse
#import datetime
def get_params_run():
    mainparser = argparse.ArgumentParser(description="For create topics")
    subparsers = mainparser.add_subparsers(title='subcommands', description='valid subcommands', help='description')

    head = subparsers.add_parser("head", description="Heads")
    head.add_argument("-url", dest="url", default='https://rlm.sigma.ru')
    head.add_argument("-authorization", dest="Authorization", default='token')
    head.add_argument("-accept", dest="accept", default='application/json')
    head.add_argument("-content_type", dest="Content-Type", default='application/json')

    param = subparsers.add_parser("param", description="Param")
    param.add_argument("-action", dest="action", default='aktag_create_topic')
    param.add_argument("-ak_topic", dest="ak_topic", default='test2api')
    param.add_argument("-ak_replication_factor", dest="ak_replication_factor", default='1')
    param.add_argument("-ak_partitions", dest="ak_partitions", default='1')
    param.add_argument("-ak_security", dest="ak_security", default='SSL')
    param.add_argument("-ak_port", dest="ak_port", default='9093')
    param.add_argument("-ak_topic_config", dest="ak_topic_config", default='[]')
    param.add_argument("-user_email", dest="user_email", default='user@example.com')
    param.add_argument("-env_type", dest="env_type", default='TEST')

    item = subparsers.add_parser("item", description="Items")
    item.add_argument("-invsvm_ci_svm", dest="invsvm_ci_svm", default='CI04340141')
    item.add_argument("-invsvm_ip", dest="invsvm_ip", default='10.56.165.201')

    heads = vars(head.parse_args())
    params = vars(param.parse_args())
    items = vars(item.parse_args())

    return [heads, params, items]

def post_to_api(all):
    heads = all[0]
    if heads['Authorization'] == 'token':
        heads['Authorization'] = input('enter your token: ')
    body = {}
    body['params'] = all[1]
    body['items'] = all[2]
    urllib3.disable_warnings()
    #print(heads.pop('url'))
    #print(heads)
    #print(body)
    r = requests.post(url=heads.pop('url'), headers=heads, data=body)
    #if str(r.status_code) == '200':
    #    print('sucsses')
    #else:
    #    print('fail')

if __name__ == '__main__':
    #print(get_params_run())
    post_to_api(get_params_run())