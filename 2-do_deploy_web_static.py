#!/usr/bin/python3
"""This module compresses the web static package for deployment"""
from fabric.api import *
from datetime import datetime
from os import path


env.hosts = ['100.25.19.204', '54.157.159.85']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
        """A function to deploy files to the web server"""
        try:
                if not (path.exists(archive_path)):
                        return False

                # upload archive
                put(archive_path, '/tmp/')

                # create target dir
                ts = archive_path[-18:-4]
                run('sudo mkdir -p /data/web_static/\
releases/web_static_{}/'.format(ts))

                # uncompress archive and delete .tgz
                run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
/data/web_static/releases/web_static_{}/'
                    .format(ts, ts))

                # remove archive
                run('sudo rm /tmp/web_static_{}.tgz'.format(ts))

                # move contents into host web_static
                run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
/data/web_static/releases/web_static_{}/'.format(ts, ts))

                # remove extraneous web_static dir
                run('sudo rm -rf /data/web_static/releases/\
web_static_{}/web_static'
                    .format(ts))

                # delete pre-existing sym link
                run('sudo rm -rf /data/web_static/current')

                # re-establish symbolic link
                run('sudo ln -s /data/web_static/releases/\
web_static_{}/ /data/web_static/current'.format(ts))
        except:
                return False

        # return True on success
        return True
