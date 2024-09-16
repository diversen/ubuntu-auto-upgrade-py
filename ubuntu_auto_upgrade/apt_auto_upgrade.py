import subprocess
import os
from datetime import datetime
import pytz
from config import CONFIG
import logging

# from config try and import send_message
try:
    from config import send_message

    logging.debug("send_message function imported from config")

except ImportError:
    logging.debug("send_message function NOT imported from config")

    def send_message(subject, message):
        pass


class AptAutoUpgrade:
    def __init__(self):
        self.config = CONFIG
        self.lock_file = "./restart.lock"
        timezone_str = self.config["timezone"]
        self.timezone = pytz.timezone(timezone_str)

    def _subprocess_run(self, params) -> subprocess.CompletedProcess:
        res = subprocess.run(
            params,
            capture_output=True,
            text=True,
            check=True,
        )

        return res

    def get_hostname(self):
        res = self._subprocess_run(["hostname"])
        return res.stdout.strip()

    def parse_apt_check(self, apt_output):
        output_ary = apt_output.split(";")  # e.g., "3;0"
        return output_ary[0] != "0" or output_ary[1] != "0"

    def has_updates(self):
        res = self._subprocess_run([self.config["apt_check_path"]])

        # a bit weird that we are using stderr here
        # but that's how the apt-check command works
        return self.parse_apt_check(res.stderr.strip())

    def upgrade(self):
        self._subprocess_run(["apt-get", "update", "-y"])
        self._subprocess_run(["apt-get", "dist-upgrade", "-y"])

    def needs_restart(self):
        return os.path.exists(self.config["reboot_required_path"])

    def should_auto_restart(self):
        return self.needs_restart() and self.config["restart"]

    def restart(self):
        self._subprocess_run(["/sbin/shutdown", "-r", "+1"])

    def get_datetime(self):
        return datetime.now(self.timezone).strftime("%Y-%m-%d %H:%M:%S")

    def run(self):
        try:
            server_name = self.get_hostname()

            if os.path.exists(self.lock_file):
                subject = f"Server ({server_name}) restarted"
                message = f"Server ({server_name}) was restarted.\n\n"
                message += "You should check if everything is working as expected.\n\n"

                os.unlink(self.lock_file)
                logging.info(f"Removed lock file (restart success): {self.lock_file}")
                send_message(subject, message)

            if self.has_updates():
                logging.info("Server should be upgraded. Will now try to upgrade")
                self.upgrade()
                logging.info("Server upgraded")
                subject = f"Server ({server_name}) upgraded with success"
                message = f"Server ({server_name}) was upgraded.\n\n"
                message += "You should check if everything is working as expected.\n\n"

                if self.needs_restart():
                    message += "The server needs to be restarted\n\n"
                    if self.should_auto_restart():
                        message += "Server will try to restart automatically\n\n"
                        with open(self.lock_file, "w") as f:
                            f.write("Restart Lock")
                        self.restart()
                        logging.info("Server restarting in one minute")
                    else:
                        message += "You will need to restart the server manually\n\n"

                send_message(subject, message)

            return 0

        except Exception as e:
            logging.error(f"Error: {e}")
            subject = f"Server ({server_name}) upgrade failed"
            message = (
                f"There was an error while trying to upgrade the server:\n\n{e}\n\n"
            )
            send_message(subject, message)
            return 1
