import os
from a2wsgi import ASGIMiddleware
import django

from channels.routing import get_default_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

django.setup()


application = get_default_application()
#application = ASGIMiddleware(get_default_application())
