import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import CONFIG_SMTP
import logging


def send_smtp_message(subject, message):
    try:
        # Create a secure SSL context
        context = ssl.create_default_context()

        # Connect to the server using smtplib.SMTP and then upgrade to TLS
        with smtplib.SMTP(CONFIG_SMTP["host"], CONFIG_SMTP["port"]) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)  # Secure the connection
            server.ehlo()  # Can be omitted
            server.login(CONFIG_SMTP["username"], CONFIG_SMTP["password"])

            # Prepare the email
            msg = MIMEMultipart("alternative")
            msg["Subject"] = subject
            msg["From"] = CONFIG_SMTP["default_from"]
            msg["To"] = CONFIG_SMTP["default_to"]

            # Attach the message body
            part1 = MIMEText(message, "plain")
            msg.attach(part1)

            # Send the email
            server.sendmail(
                CONFIG_SMTP["username"],
                CONFIG_SMTP["default_to"],
                msg.as_string(),
            )

    except Exception as e:
        logging.error(f"Failed to send email: {e}")
        logging.exception(e)
