from django.contrib import admin
from .models import link

# Register your models here.

class linkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(link, linkAdmin)
