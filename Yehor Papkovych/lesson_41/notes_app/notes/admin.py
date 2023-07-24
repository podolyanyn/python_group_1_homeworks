from django.contrib import admin

from .models import Categories, Note

admin.site.register(Categories)
admin.site.register(Note)