# Ubuntu Auto Upgrade

These scripts are a rewrite of the following PHP scripts: 

[ubuntu-auto-upgrade](https://github.com/diversen/ubuntu-auto-upgrade)

The python scripts will upgrade ubuntu and send email notifications using SMTP. 
It will probably also work with other Debian variants of linux.

Tested on Ubuntu 20.04 LTS and 22.04 LTS

## Install

    git clone https://github.com/diversen/ubuntu-auto-upgrade-py.git
    cd ubuntu-auto-upgrade-py
    virtualenv venv
    pip install -r requirements.txt

## Config

Create config file:

    cp config_dist.py config.py

Edit SMTP settings in `config.py`. 
The `default_to` setting in SMTP is the email address of the person who will receive emails. 

You can also edit `restart` that determines if the server should restart when needed. 
You may also set a `timezone`. 

## Cron

Set the script up as a cron script. Let it run every 10 minutes of once a week.
You will need to let the script run as root. Edit crontab as `sudo`, e.g.: 

    sudo crontab -e

Add the crontab line and remember to change to your own source path. 

This will e.g. run the script every 10 minutes:

    */10 * * * * cd /home/dennis/ubuntu-auto-upgrade-py && ./venv/bin/python cron.php

## Logs

Logs are written to `logs/main.log`. This log file will be created if it does not exist.  

# License

MIT © [Dennis Iversen](https://github.com/diversen)