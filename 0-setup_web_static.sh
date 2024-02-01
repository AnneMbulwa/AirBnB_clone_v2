#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

sudo apt-get -y update > /dev/null/
sudo apt-get install -y nginx > /dev/null/

# creating the required folders
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# creating a fake html file and put some content in it
touch /data/web_static/releases/test/index.html
echo "Hello and Welcome!" > /data/web_static/releases/test/index.html

# checking if the symbolic exits
if [ -d "/data/web_static/current" ]
then
	sudo rm -rf /data/web_static/current
fi

# create a symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# changing the ownership
chown -hR ubuntu:ubuntu /data/

# update nginx configure
sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

server nginx restart
