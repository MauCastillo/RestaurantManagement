from django.contrib import admin
from .models import Client, Bill

admin.site.register(Client)
admin.site.register(Bill)