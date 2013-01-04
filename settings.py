# coding: utf-8

# DJANGO IMPORTS
from django.conf import settings

# Admin Site Title
ADMIN_HEADLINE = getattr(settings, "ARKI_ADMIN_HEADLINE", 'Arkiadmin')
ADMIN_TITLE = getattr(settings, "ARKI_ADMIN_TITLE", 'Arkiadmin')

# Link to your Main Admin Site (no slashes at start and end)
ADMIN_URL = getattr(settings, "ARKI_ADMIN_URL", '/admin/')

# AUTOCOMPLETE LIMIT
AUTOCOMPLETE_LIMIT = getattr(settings, "ARKI_AUTOCOMPLETE_LIMIT", 10)
