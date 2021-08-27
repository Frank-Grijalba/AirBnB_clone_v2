#!/usr/bin/python3
# Fabfile to delete out-of-date archives.
from fabric.api import *
import os

def do_clean(number=0):
    if number < 0:
        return None
    number = 2 if (number == 0 or number == 1) else (number + 1)
    with lcd("./versions"):
        local('ls -t | tail -n +{:d} | xargs rm -rf --'.
              format(number))
    with cd("/data/web_static/releases"):
        run('ls -t | tail -n +{:d} | xargs rm -rf --'.
            format(number))
