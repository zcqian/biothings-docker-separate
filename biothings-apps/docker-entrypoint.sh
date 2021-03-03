#!/bin/bash

if [ ! -f /data/biothings/ssh_host_key ]; then
    ssh-keygen -f /data/biothings/ssh_host_key -N ""
fi

exec python /home/biothings/APP_NAME/src/bin/hub.py