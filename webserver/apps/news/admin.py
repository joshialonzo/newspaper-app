# built-in django modules
from django.contrib import admin

# custom django modules
from .models import New
from .models import Resource

# Register your models here.


class ResourceAdmin(admin.StackedInline):
    model = Resource


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    inlines = [ResourceAdmin]

    class Meta:
        model = New


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    pass
