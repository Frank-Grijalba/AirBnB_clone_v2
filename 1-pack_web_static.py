#!/usr/bin/python3
# Fabric script that generates a .tgz archive
from fabric.api import *

import datetime


def do_pack():
    now = datetime.datetime.now()
    file = ('versions/web_static_{}{}{}{}{}{}.tgz'.format(
        now.year, now.month, now.day, now.hour, now.minute, now.second))
    local("mkdir versions")
    path = "web_static"
    review = local("tar -czvf {} {}".format(file, path))

    if review.failed:
        return None
    else:
        return file
