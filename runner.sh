#!/bin/bash

which twistd &> /dev/null
if [ $? -ne 0 ]; then
    echo "Twisted is not installed, are you in a virtualenv?";
    exit 1
fi

twistd -n web --path ./packages/
