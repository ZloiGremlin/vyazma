import os
import sys
sys.path += ['/home/gremlin/webapps/vyazma3/vyazma']
from django.core.handlers.wsgi import WSGIHandler

os.environ['DJANGO_SETTINGS_MODULE'] = 'vyazma.settings'
# activate_this = os.path.expanduser("~/webapps/vyazma3/env/bin/activate_this.py")
# execfile(activate_this, dict(__file__=activate_this))
application = WSGIHandler()