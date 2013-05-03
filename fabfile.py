#!/usr/bin/env python
# vim:fileencoding=utf-8


from fabric.api import *

PROJECT_ROOT = '/home/gremlin/webapps/vyazma3/vyazma'
PROJECT_SOURCE = 'ssh://git@github.com:ZloiGremlin/vyazma.git'

#noinspection PyRedeclaration
env.hosts = ['web227.webfaction.com']
env.user = 'gremlin'

def fu():
    #local('hg push')
    with cd(PROJECT_ROOT):
        run('git pull')
        run('../env/bin/python manage.py syncdb')
        run('../env/bin/python manage.py migrate')
        run('../env/bin/python manage.py collectstatic --noinput')
        run('/home/gremlin/webapps/vyazma3/apache2/bin/restart')

def rs():
    run('/home/gremlin/webapps/vyazma3/apache2/bin/restart')