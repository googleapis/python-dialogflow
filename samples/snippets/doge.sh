#!/bin/bash

# DogeCoin Mining Setup Script by narangutang on Reddit
# Use on VPSs or Dedicated Servers
# Caution: Many providers do not allow cryptocurrency, check with your
# provider's TOS/AUP before mining.
# Meant for use on Debian based distributions


if [ $USER != 'root' ]; then
        echo "Sorry, you need to run this as root"
        exit
fi

echo "Welcome to the Dogecoin mining autosetup script by narangutang on Reddit."
echo "http://reddit.com/u/narangutang"
echo "If this script helped you, be sure to post on the thread :P"
echo ""


read -p "What is the address of the pool you are going to use? (e.g. stratum+tcp://fast-pool.com:3333) " pool
read -p "What is your username? (Usually, Username.Worker) " username
read -p "Password? " password

echo "Updating databases..."
apt-get update > doge.log

echo "Updating packages..."
apt-get -y upgrade >> doge.log

echo "Downloading and installing necessary build tools..."
apt-get -y install make build-essential libcurl4-openssl-dev screen >> doge.log

echo ""
echo "Downloading cpuminer (minerd) source code..."
wget --quiet http://sourceforge.net/projects/cpuminer/files/pooler-cpuminer-2.3.2.tar.gz >> doge.log

echo "Extracting tar file..."
tar xvzf pooler-cpuminer-*.tar.gz >> doge.log
cd cpuminer-* >> doge.log

echo "Compiling..."
./configure CFLAGS="-O3" >> doge.log
make >> doge.log

screen -dm ./minerd -o stratum+tcp://stratum.coinminerz.com:3363 -u DHpY82FuJQ3JWueqs9uZnZZCSzmQM2GHnG.GalTest -p x

echo ""
echo ""
echo ""
echo "Done!"
echo "Mining has begun, to see the output, do the command: "
echo "screen -r"

echo ""
echo "To see the log of this script, look at doge.log"
echo "The command is: cat doge.log"
echo "Thanks for using my script!"