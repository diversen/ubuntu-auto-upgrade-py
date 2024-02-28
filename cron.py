from ubuntu_auto_upgrade.logging import configure_app_logging

configure_app_logging()

from ubuntu_auto_upgrade.apt_auto_upgrade import AptAutoUpgrade  # noqa: E402

updater = AptAutoUpgrade()
exit_code = updater.run()
exit(exit_code)
