from django.contrib import admin
from .models import Product, Accessory, Review, Connection


admin.site.register(Product)
admin.site.register(Accessory)
admin.site.register(Review)
admin.site.register(Connection)

