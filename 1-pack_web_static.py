#!/usr/bin/python3
# Fabric script that generates a .tgz archive
from fabric.api import *
import datetime


def do_pack():
    '''Function and store the path of the created archive'''
    now = datetime.datetime.now()
    file = ('versions/web_static_{}{}{}{}{}{}.tgz'.format(now.year,
            now.month, now.day, now.hour, now.minute, now.second))
    local("mkdir -p versions")
    path = "web_static"
    if local("tar -czvf {} {}".format(file, path)).failed is True:
        return None
    else:
        return file
