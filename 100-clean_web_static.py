#!/usr/bin/python3
# Fabfile to delete out-of-date archives.
from fabric.api import *
import os

def do_clean(number=0):
    if number < 0:
        return None
    number = 1 if int(number) == 0 else int(number)

    with lcd("./versions"):
        local('ls -t | tail -n +{:d} | xargs rm -rf --'.
              format(number))

    with cd("/data/web_static/releases"):
        run('ls -t | tail -n +{:d} | xargs rm -rf --'.
            format(number))
