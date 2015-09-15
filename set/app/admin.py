from django.contrib import admin

from app.models import UserProfile, Product, Vendor, UserAccount

admin.site.register(UserProfile)
admin.site.register(Product)
admin.site.register(Vendor)
admin.site.register(UserAccount)