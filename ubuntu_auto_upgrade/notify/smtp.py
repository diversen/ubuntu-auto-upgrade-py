import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import CONFIG
import logging


def send_smtp_message(subject, message):

    try:
        with smtplib.SMTP_SSL(
            CONFIG["host"],
            CONFIG["port"],
            context=ssl.create_default_context(),
        ) as server:
            server.login(CONFIG["username"], CONFIG["password"])

            msg = MIMEMultipart("alternative")
            msg["Subject"] = subject
            msg["From"] = CONFIG["default_from"]
            msg["To"] = CONFIG["default_to"]

            part1 = MIMEText(message, "plain")
            msg.attach(part1)

            server.sendmail(
                CONFIG["username"],
                CONFIG["default_to"],
                msg.as_string(),
            )

    except Exception as e:
        # fail silently, but log the error
        logging.error(f"Failed to send email: {e}")
