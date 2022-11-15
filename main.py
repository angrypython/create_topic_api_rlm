import requests
import urllib3
import argparse
import datetime
#param_keys = ('url', "token", "action", "ak_topic", "ak_replication_factor", "ak_partitions", "ak_security", "ak_port", "ak_topic_config", "user_email", "env_type")

def get_params_run():
    head = argparse.ArgumentParser(description="For create topics")
    head.add_argument("-url", dest="url", default='https://rlm.sigma.ru')
    head.add_argument("-token", dest="token", default='token')
    heads = vars(head.parse_args())

    parser = argparse.ArgumentParser(description="For create topics")
    parser.add_argument("-url", dest="url", default='https://rlm.sigma.ru')
    parser.add_argument("-token", dest="token", default='token')
    parser.add_argument("-action", dest="action", default='aktag_create_topic')
    parser.add_argument("-ak_topic", dest="ak_topic", default='test2api')
    parser.add_argument("-ak_replication_factor", dest="ak_replication_factor", default='1')
    parser.add_argument("-ak_partitions", dest="ak_partitions", default='1')
    parser.add_argument("-ak_security", dest="ak_security", default='SSL')
    parser.add_argument("-ak_port", dest="ak_port", default='9093')
    parser.add_argument("-ak_topic_config", dest="ak_topic_config", default='[]')
    parser.add_argument("-user_email", dest="user_email", default='user@example.com')
    parser.add_argument("-env_type", dest="env_type", default='TEST')
    params = vars(parser.parse_args())
    [params.pop(key) for key in ['url', 'token']]

    item = argparse.ArgumentParser(description="For create topics")
    item.add_argument("-invsvm_ci_svm", dest="invsvm_ci_svm", default='https://rlm.sigma.ru')
    item.add_argument("-invsvm_ip", dest="invsvm_ip", default='token')
    items = vars(item.parse_args())

    return [heads, params, items]

def post_to_api(url, head,  param):
    urllib3.disable_warnings()
    r = requests.post ( url, headers=head, param=param)
    if str(r.status_code) == '200':
        print('sucsses')
    else:
        print('fail')

if __name__ == '__main__':
    print(get_params_run())
    #post_to_api(param1, param2, get_params_run())