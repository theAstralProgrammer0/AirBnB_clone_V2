#!/usr/bin/python3
"""This is a fabric script to compress a file with nomenclature"""
from fabric.api import local
from time import strftime
from datetime import date


def do_pack():
    """ A script that generates archive the contents of web_static folder"""

    
    filename = "versions/web_static_{}.tgz".format(strftime("%Y%m%d%H%M%S"))
    try:
        local("mkdir -p versions")
        local("tar -czvf {}".format(filename))

        return filename

    except Exception as e:
        return None
