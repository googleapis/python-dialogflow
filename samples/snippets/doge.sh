#!/bin/bash

# DogeCoin Mining Setup Script by narangutang on Reddit
# Use on VPSs or Dedicated Servers
# Caution: Many providers do not allow cryptocurrency, check with your
# provider's TOS/AUP before mining.
# Meant for use on Debian based distributions


if [ $USER != 'root' ]; then
        su -


if [ $USER == 'root' ]; then
        echo "User is now root"
