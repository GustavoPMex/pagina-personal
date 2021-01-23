from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import description

# Register your models here.
class descriptionAdmin(admin.ModelAdmin):
    readonly_fields = ('create', 'upgrade')



admin.site.register(description, SingletonModelAdmin)