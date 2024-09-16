from config import CONFIG_SLACK
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import logging


def send_slack_message(subject, message):

    slack_token = CONFIG_SLACK["slack_token"]
    client = WebClient(token=slack_token)
    text = message.strip()

    try:
        client.chat_postMessage(
            channel=CONFIG_SLACK["slack_channel"],
            text=text,
        )
    except SlackApiError as e:
        logging.error(f"Failed to send slack message: {e}")
        logging.exception(e)
