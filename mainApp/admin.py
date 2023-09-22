from django.contrib import admin
from .models import Category, Flower, Orders, Cart, Payment
# Register your models here.

admin.site.register(Flower)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Payment)
admin.site.register(Orders)