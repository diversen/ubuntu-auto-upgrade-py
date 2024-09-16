import logging

CONFIG = {
    # App
    "log_level": logging.DEBUG,
    "timezone": "Europe/Copenhagen",
    "restart": True,
    # Paths. These are the default paths for Ubuntu 20.04 and 22.04
    "apt_check_path": "/usr/lib/update-notifier/apt-check",
    "reboot_required_path": "/var/run/reboot-required",
}

CONFIG_SMTP = {
    # SMTP
    "host": "smtp-relay.brevo.com",
    "port": 587,
    "username": "smtp-username@test.com",
    "password": "password",
    "default_to": "to@test.com",
    "default_from": "Server <mail@10kilobyte.com>",
}

CONFIG_SLACK = {
    "slack_token": "xoxb-slack-token",
    "slack_channel": "SLACK_CHANNEL_ID",
}

# Mattermost specific
CONFIG_MATTERMOST = {
    "mattermost_webhook": "https://chat.openaws.dk/hooks/webhook-id",
}


def send_message(subject, message):
    """Define a default send_message function that sends messages
    There is a couple of built-in functions that can be used to send messages to Slack, SMTP, and Mattermost.
    If these message functions fail, the error is logged, but the exception is caught and ignored.
    This to avoid the upgrade process to fail if the notification fails.

    This function can be replaced by a custom `send_message` function
    """
    pass

    # from ubuntu_auto_upgrade.notify.slack import send_slack_message
    # send_slack_message(subject, message)

    # from ubuntu_auto_upgrade.notify.smtp import send_smtp_message
    # send_smtp_message(subject, message)

    # from ubuntu_auto_upgrade.notify.mattermost import send_mattermost_message
    # send_mattermost_message(subject, message)
