#!/bin/bash

type python3 > /dev/null 2>&1

if [ $? -eq 1 ];then
    echo "Error: Require python3"
    exit 1
fi

# firefox
apt install -y firefox &> /dev/null
apt upgrade -y firefox &> /dev/null

# selenium
python3 -m pip install selenium --upgrade
python3 -m pip install Pillow --upgrade

# geckodriver
mkdir -p /tmp/screenshot_geckodriver
cd /tmp/screenshot_geckodriver

MACHINE_TYPE=`uname -m`
if [ ${MACHINE_TYPE} == 'x86_64' ]; then
    wget -q https://github.com/`curl -s https://github.com/mozilla/geckodriver/releases | grep 'geckodriver-[^-]\+-linux64.tar.gz' | head -n 1 | sed "s/.*href=\"\([^\"]\+\)\".*/\1/"` -O geckodriver.tar.gz
else
    wget -q https://github.com/`curl -s https://github.com/mozilla/geckodriver/releases | grep 'geckodriver-[^-]\+-linux32.tar.gz' | head -n 1 | sed "s/.*href=\"\([^\"]\+\)\".*/\1/"` -O geckodriver.tar.gz
fi

tar xzf geckodriver.tar.gz
mv geckodriver /usr/sbin
if [ -e /usr/bin/geckodriver ]
then
    rm /usr/bin/geckodriver
fi
ln -s /usr/sbin/geckodriver /usr/bin/geckodriver
rm -rf /tmp/screenshot_geckodriver

echo "End."