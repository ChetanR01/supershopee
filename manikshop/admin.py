from django.contrib import admin
from django.contrib.auth.models import User
from .models import Category,SubCategory,ProductDetails, Deal, Extended_user
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(ProductDetails)
admin.site.register(Deal)

# Extended user
class Extended_userInline(admin.StackedInline):
    model =Extended_user
    can_delete = False
    verbose_name_plural = 'Extended_Users' 

class CustomizedUserAdmin(UserAdmin):
    inlines = (Extended_userInline, )

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)