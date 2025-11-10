from config import CONFIG_MATTERMOST
import requests
import logging
import json

logger: logging.Logger = logging.getLogger(__name__)


def send_mattermost_message(message: str) -> bool:

    try:
        base_url = CONFIG_MATTERMOST.get("base_url", "").rstrip("/")
        token = CONFIG_MATTERMOST.get("token")
        channel_id = CONFIG_MATTERMOST.get("channel_id")
        payload = {"channel_id": channel_id, "message": message}

        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        url = f"{base_url}/api/v4/posts?set_online=false"
        resp = requests.post(
            url,
            headers=headers,
            data=json.dumps(payload),
            timeout=10,
        )
        resp.raise_for_status()
        return True
    except requests.RequestException as e:
        # Mirror your previous logging style but correct the message
        logger.error(f"Failed to send Mattermost message: {e}")
        logger.exception(e)
        return False
