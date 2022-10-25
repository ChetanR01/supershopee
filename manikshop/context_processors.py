from unicodedata import category
from .models import Category, SubCategory

def pass_cat_nd_sub_cat(request):
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()

    return {"categories":categories, "subcategories":subcategories}