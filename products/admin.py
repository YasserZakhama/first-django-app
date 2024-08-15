from django.contrib import admin
from .models import Product,Time
# Register your models here.
admin.site.register(Product)
admin.site.register(Time)
admin.site.site_header = 'Site Yasser administration'
admin.site.site_title = 'Site Yasser'