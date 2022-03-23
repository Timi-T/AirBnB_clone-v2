#!/usr/bin/python3
"""
remove old archives from deployment
"""


from fabric.api import run, local, env


env.user = 'ubuntu'
env.hosts = ['34.148.87.245', '3.231.218.82']


def do_clean(number=0):
    """function to delete archives"""

    number = int(number)
    if number == 0:
        number += 1
    number +=1
    num_str = str(number + 1)
    arc_path = '/data/web_static/releases'
    local('ls versions -t | tail -n +{} | xargs rm --'.format(num_str))
    run('ls {} -t | tail -n +{} | xargs rm --'.format(arc_path, num_str))
