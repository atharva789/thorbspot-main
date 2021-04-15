import os
import django
from channels.routing import get_default_application

os.environ.set_default("DJANGO_SETTINGS_MODULE","thorbspot.settings")
django.setup()
application = get_default_application()