from django.contrib import admin
from .models import Country, Director, Genre, Movie

admin.site.register([Country, Director, Genre, Movie])