from django.contrib import admin
from django.contrib.auth.models import User
from .models import Category,SubCategory,ProductDetails, Deal
# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(ProductDetails)
admin.site.register(Deal)