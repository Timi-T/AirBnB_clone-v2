#!/usr/bin/python3
"""
fabfile to create an archive
"""

from __future__ import with_statement
from fabric.api import local, settings
from datetime import datetime


def do_pack():
    """function to compress a directory"""

    local("mkdir -p versions")
    current_time = str(datetime.now())
    current_time = (current_time.split('.'))[0]
    current_time = current_time.replace(':', '')
    current_time = current_time.replace(' ', '')
    current_time = current_time.replace('-', '')
    file_path = 'versions/web_static_' + current_time + '.tgz'
    with settings(warn_only=True):
        result = local("tar -zcvf {} web_static".format(file_path))
    if result.failed:
        return None
    else:
        return file_path
