#!/bin/env python3

import requests
import json

with open('my_token.txt', 'r') as f:
    token = f.read().strip()

token_header = {'Private-Token': token}

api_url = 'https://gitlab.ical.tw/api/v4/'

rets = []
id_before = None
while True:
    param = {'visibility': 'public', 'orderby': 'id', 'id_before': id_before}
    req = requests.get(
            api_url + 'projects', headers=token_header, params=param
            )
    ret = req.json()
    if len(ret) == 0:
        break
    else:
        rets.extend(ret)
        id_before = ret[-1]['id']

for proj in rets:
    #print(proj['id'], proj['path_with_namespace'], proj['visibility'])
    print(proj['path_with_namespace'])


for this_proj in rets:
    #this_proj = rets[0]
    param = {'visibility': 'internal'}
    print('Modify', this_proj['id'], this_proj['path_with_namespace'])
    ret = requests.put(api_url + 'projects/' + str(this_proj['id']), headers=token_header, data=param)
    print(ret)









