# built-in django modules
from django.contrib import admin

# custom django modules
from .models import Section
from .models import New
from .models import Resource

# Register your models here.


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass


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
