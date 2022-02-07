#  -*- coding: utf-8 -*-
import datetime

from volcengine.example.cdn import ak, sk
from volcengine.cdn.service import CDNService

if __name__ == '__main__':
    svc = CDNService()
    svc.set_ak(ak)
    svc.set_sk(sk)
    now = int(datetime.datetime.now().strftime("%s"))
    body = {
        'StartTime': now - 86400,
        'EndTime': now,
        'Metric': 'pv',
        'Domain': 'example.com',
        'Item': 'region'
    }
    print(body)

    resp = svc.describe_cdn_domain_top_data(body)
    print(resp)
