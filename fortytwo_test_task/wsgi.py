"""
WSGI config for fortytwo_test_task project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""
import os,sys

path="/d/diadkoroman.fortytwotesttask-247"
if not path in sys.path:
    sys.path.append(path)

activate_this = "/d/diadkoroman.fortytwotesttask-247/django272/bin/activate_this.py"
execfile(activate_this, dict(__file__=activate_this))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fortytwo_test_task.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
