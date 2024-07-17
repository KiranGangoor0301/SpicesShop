# Example of a typical wsgi.py
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spiceshop.settings')

application = get_wsgi_application()
