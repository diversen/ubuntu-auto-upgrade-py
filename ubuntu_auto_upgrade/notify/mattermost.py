from config import CONFIG_MATTERMOST
import requests
import logging
import json


logger: logging.Logger = logging.getLogger(__name__)


def send_mattermost_message(subject, message):
    mattermost_webhook_url = CONFIG_MATTERMOST["mattermost_webhook"]

    payload = {"text": f"{message}"}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(
            mattermost_webhook_url,
            headers=headers,
            data=json.dumps(payload),
        )
        response.raise_for_status()

    except Exception as e:
        logging.error(f"Failed to send email: {e}")
        logging.exception(e)
