import logging

import requests

from config import settings


logger = logging.getLogger(__name__)


def send_message(message):
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + settings.line_token}

    logger.info(message)
    payload = {'message': message}
    requests.post(url, headers=headers, params=payload,)
