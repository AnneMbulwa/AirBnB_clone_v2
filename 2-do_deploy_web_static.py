#!/usr/bin/python3
"""based on 1-pack_web_static.py creating a fabric script that distributes
an archive to your web servers, using the function do_deploy"""

from fabric.api import *
from os import path
from datetime import datetime

env.host = []
env.user = 'ubuntu'
env.key_filename = ''


def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False

    try:
        compres = archive_path.split("/")[-1]
        filed = ("/data/web_static/releases/" + compres.split(".")[0])

        put(archive_path, "/tmp/")

        # Uncompress the archive to the folder/data/web_static/releases/<archive
        # filename without extension> on the web server
        run("sudo mkdir -p {}".format(filed))
        run("sudo tar -xzf /tmp/{} -C {}".format(compres, filed))

        # Delete the archive from the web server
        run("sudo rm /tmp/{}".format(compres))

        # moving contents to host web_static server
        run("sudo mv {}/web_static/* {}/*".format(filed, filed))

        # Remove any extra web_static dir
        run("sudo rm -rf {}/web_static/ ".format(filed))

        # deleting the symbolic link
        run('sudo rm -rf /data/web_static/current')

        # Create a new symbolic link /data/web_static/current on web server, 
        run("sudo ln -sf {} /data/web_static/current".format(filed))

        return True
    except:
        return False
