CONFIG = {
    # SMTP
    "host": "smtp-relay.sendinblue.com",
    "port": 465,
    "username": "some.user@test.com",
    "password": "password",
    
    # App
    "default_to": "mail@test.com",
    "default_from": "System <mail@test.com>",
    "timezone": "Europe/Copenhagen",
    "restart": True,
    "apt_check_path": "/usr/lib/update-notifier/apt-check",
    "reboot_required_path": "/var/run/reboot-required",
}
