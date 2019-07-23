from django.contrib import admin
# Register your models here.

# from .models import MyModel
from .models import *


class BandAdmin(admin.ModelAdmin):
    search_fields = ['members__last_name']
    list_max_show_all = 100

admin.site.register(Band, BandAdmin)
admin.site.register(Genre)
admin.site.register(Member)
