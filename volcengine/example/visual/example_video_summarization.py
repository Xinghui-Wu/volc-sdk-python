# coding:utf-8
from __future__ import print_function

import time

from volcengine.visual.VisualService import VisualService

if __name__ == '__main__':
    visual_service = VisualService()

    # call below method if you dont set ak and sk in $HOME/.volc/config
    visual_service.set_ak('ak')
    visual_service.set_sk('sk')
    data = None
    with open("filepath", "rb") as f:
        data = f.read()

    form = {
        "result_duration": 5,
        "result_width": 1280
    }
    files = {
        "video": data
    }

    resp = visual_service.video_summarization_submit_task(form, files)
    print(resp)

    params = dict()

    params = {
        "task_id": "get from submit_task resp"
    }

    resp = visual_service.video_summarization_query_task(params)
    print(resp)
