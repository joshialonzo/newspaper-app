# built-in django modules
from django.contrib import admin

# custom django modules
from .models import New

# Register your models here.


admin.site.register(New)
