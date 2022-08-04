#  -*- coding: utf-8 -*-
import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../../")

from volcengine.example.cdn import ak, sk
from volcengine.cdn.service import CDNService

if __name__ == '__main__':
    svc = CDNService()
    svc.set_ak(ak)
    svc.set_sk(sk)

    body = {
        "PageNum": 1,
        'PageSize': 10,
        'TaskType': 'refresh_file'
    }

    resp = svc.describe_content_tasks(body)
    print(resp)
