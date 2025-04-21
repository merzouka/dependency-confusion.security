#!/bin/bash

cd "/home/merzouka/esi/security/presentation/demo/use/merbe"
python -m venv venv
cd venv
ln -s "/home/merzouka/esi/security/presentation/demo/pip.conf" pip.conf

cd "/home/merzouka/esi/security/presentation/demo/use/internal"
python -m venv venv
cd venv
ln -s "/home/merzouka/esi/security/presentation/demo/pip.conf" pip.conf
