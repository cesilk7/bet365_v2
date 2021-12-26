import json

import requests

from config import settings


def send_message(messages):
    requests.post(settings.slack_url, data=json.dumps({
        'text': '\n'.join(messages),
    }))
