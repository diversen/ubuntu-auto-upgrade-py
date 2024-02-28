from config import CONFIG
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import logging


def send_slack_message(subject, message):

    print("send_slack_message")
    return

    slack_token = CONFIG["slack_token"]
    client = WebClient(token=slack_token)
    text = f"{subject}\n{message}"
    text = text.strip()

    try:
        client.chat_postMessage(channel=CONFIG["slack_channel"], text=text)
    except SlackApiError as e:
        logging.error(f"Failed to send slack message: {e}")
