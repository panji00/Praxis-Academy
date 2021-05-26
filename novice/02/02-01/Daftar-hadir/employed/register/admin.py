from django.contrib import admin

from . models import register
# Register your models here.

class registerForAdmin(admin.ModelAdmin):
    list_display = ['fullname','mobile','position']

admin.site.register(register, registerForAdmin)