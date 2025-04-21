#!/bin/bash

if [ ! -e "/home/merzouka/esi/security/presentation/demo/use/merbe/venv" ]; then
    echo "Creating virtualenv for merbe..."
    cd "/home/merzouka/esi/security/presentation/demo/use/merbe"
    python -m venv venv
    cd venv
    ln -s "/home/merzouka/esi/security/presentation/demo/pip.conf" pip.conf
fi

if [ ! -e "/home/merzouka/esi/security/presentation/demo/use/internal/venv" ]; then
    echo "Creating virtualenv for sample..."
    cd "/home/merzouka/esi/security/presentation/demo/use/internal"
    python -m venv venv
    cd venv
    ln -s "/home/merzouka/esi/security/presentation/demo/pip.conf" pip.conf
fi
