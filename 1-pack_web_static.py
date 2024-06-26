#!/usr/bin/python3
"""This module contains a fabric script to compress a file with nomenclature"""
from fabric.api import local
from time import strftime
from datetime import date


def do_pack():
    """This function generates a .tgz for the contents of the web_static dir"""
    distinct = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(distinct))

        return "versions/web_static_{}.tgz".format(distinct)

    except Exception:
        return None
