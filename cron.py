from apt_auto_upgrade import AptAutoUpgrade

updater = AptAutoUpgrade()
exit_code = updater.run()
exit(exit_code)