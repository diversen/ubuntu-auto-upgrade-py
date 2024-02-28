# Ubuntu Auto Upgrade

These scripts are a rewrite of the following PHP scripts: 

[ubuntu-auto-upgrade](https://github.com/diversen/ubuntu-auto-upgrade)

The python scripts will upgrade ubuntu. The scripts will probably also work with other Debian variants of linux. 

The scripts upgrades the server. It also restarts the server (if needed) - but this is configurable.

It may send notifications via email or slack or using a custom function.

It should be easy to create a custom notification function.

The script has been tested on Ubuntu 20.04 LTS and 22.04 LTS

## Install

    git clone https://github.com/diversen/ubuntu-auto-upgrade-py.git
    cd ubuntu-auto-upgrade-py
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

## Config

Create config file:

    cp config_dist.py config.py

You may edit `restart` that determines if the server should restart when needed. Otherwise it
will not restart the server.

You may also alter `send_message` function. This function is called when the server is upgraded or
if the server is restarted (or if it needs to be restarted).

You may remove this function if you do not want to send any messages.

## Cron

Set the script up as a cron script. Let it run every 10 minutes of once a week.
You will need to let the script run as root. Edit crontab as `sudo`, e.g.: 

    sudo crontab -e

Add the crontab line and remember to change to your own source path. 

This will e.g. run the script every 10 minutes:

    */10 * * * * cd /home/dennis/ubuntu-auto-upgrade-py && ./venv/bin/python cron.py

## Logs

Logs are written to `logs/main.log`. This log file will be created if it does not exist.  

# License

MIT © [Dennis Iversen](https://github.com/diversen)