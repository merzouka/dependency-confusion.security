#!/bin/bash

which supervisord &> /dev/null
if [ $? -ne 0 ]; then
    echo "Supervisor is not installed, are you in a virtualenv?";
    exit 1
fi

# load configuration
supervisord -c gen-config/supervisord.conf

# stop running instance
supervisorctl -c gen-config/supervisord.conf stop devpi-server

# start devpi server
supervisorctl -c gen-config/supervisord.conf start devpi-server
