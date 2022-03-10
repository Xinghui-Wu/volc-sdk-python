# coding:utf-8
import json

from volcengine.live.LiveService import LiveService

if __name__ == '__main__':
    live_service = LiveService()
    ak = ""
    sk = ""
    live_service.set_ak(ak)
    live_service.set_sk(sk)
    body = {
        "MessageType": "record",
        "Vhost": "vhost",
        "CallbackDetailList": [
            {
                "Duration": 10,
                "Splice": 1,
                "RecordObject": "",
                "Format": "",
            },
        ],
    }
    resp = live_service.update_callback(body)
    print(resp)
