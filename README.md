# Ubuntu Auto Upgrade

These python scripts upgrades your ubuntu server and they may also restart your server (if preferred).

The scripts are tested on Ubuntu 20.04 LTS and 22.04 LTS. The scripts will probably also work with other Debian variants of linux. 

The scripts may also send notifications via SMTP, slack, mattermost, or using a custom function.

## Install

    git clone https://github.com/diversen/ubuntu-auto-upgrade-py.git
    cd ubuntu-auto-upgrade-py
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

Using slack notifications:

    pip install slack_sdk

Using mattermost notifications:

    pip install requests

## Config

Create config file:

    cp config_dist.py config.py

You may edit `restart` which determines if the server should restart when needed. Default is to restart.

You may also alter the `send_message` function. This function is called when the server is upgraded or
if the server is restarted (or if it needs to be restarted).

You may remove or alter the `send_message` function if you do not want to send any messages.
Or send a message in a different way. 

## Cron

Set the script up as a cron script. E.g. let it run every 10 minute or once a week.
You will need to let the script run as root. Edit crontab as `sudo`: 

    sudo crontab -e

Add a crontab line and remember to change to your own source path. 

The following will run the script past midnight at 02.  
The script will also run when the server is rebooted:

    0 2 * * * cd /home/dennis/ubuntu-auto-upgrade-py && ./venv/bin/python cron.py
    @reboot cd /home/dennis/ubuntu-auto-upgrade-py && ./venv/bin/python cron.py

## Logs

Logs are written to `logs/main.log`. The log file will be created if it does not exist.  

# License

MIT © [Dennis Iversen](https://github.com/diversen)
