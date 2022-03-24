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
    num = str(number)
    path = '/data/web_static/releases'
    run('realpath {}/* | head -n -{} | xargs sudo rm -rf --'.format(path, num))
    local('realpath versions/* | head -n -{} | xargs rm -rf --'.format(num))
