from django.contrib import admin

from .models import Genre, Music


admin.site.register(Genre, Music)
