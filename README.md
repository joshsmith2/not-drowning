# not-drowning
Visualise and play waves and music samples in browser. We hope.

This is a Django project, and needs a secret key. Current setup is to set this up with an environment variable; you can set this as follows:
  - cp env.txt.template env.txt
  - Edit env.txt
  - Run source env.txt

SERVER SETUP
This webserver is currently set up to use uWSGI and nginx
If uWSGI's not running on login, the following will do it: 
```
/usr/local/bin/uwsgi --emperor /etc/uwsgi/apps-enabled --uid www-data --gid www-data --daemonize /var/log/uwsgi/uwsgi-emperor.log
```
