#!/usr/bin/python3
"""script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack"""

from fabric.api import local
from datetime import datetime
from os import path


def do_pack():
    """creating 'versions' folder"""
    try:
        local("mkdir -p versions")
        time = datetime.now()
        date_str = "%Y%m%d%H%M%S"
        current_date = time.strftime(date_str)

        archived = f'web_static_{current_date}.tgz'
        local(f'tar -czvf versions/{archived} web_static')

        return os.path.join("versions", archived)
    except Exception:
        return None
