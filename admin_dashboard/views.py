from django.shortcuts import render, redirect
from manikshop.models import ProductDetails, Category, SubCategory,Order

from .forms import ProductForm

def index(request):
    orders = Order.objects.all().order_by("-date")
    return render(request, "01-index.html", {"orders":orders})

def product(request):
    products = ProductDetails.objects.all()
    categories = Category.objects.all()
    return render(request, "01-products.html", {"products":products,"categories":categories})

def account(request):
    products = ProductDetails.objects.all()
    return render(request, "01-accounts.html", {})

def login(request):
    products = ProductDetails.objects.all()
    return render(request, "01-login.html", {})

# Add new product
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            category_id = request.POST.get('category')
            subcategory_id = request.POST.get('subcategory')
            category= Category.objects.get(id=int(category_id))
            subcategory= SubCategory.objects.get(id=int(subcategory_id))
            form.category = category
            form.subcategory = subcategory
            form.save()
            return redirect("/dashboard/products")
        else:
            print("ERROR !!! Unable to validate form ")
            return render("/dashboard/add-product")

    form = ProductForm()
    categories=Category.objects.all()
    subcategories=SubCategory.objects.all()
    return render(request, "01-add-product.html", {"form":form,"categories":categories,"subcategories":subcategories})


# Edit Product
def edit_product(request,id):
    instance=ProductDetails.objects.get(id=id)
    if request.method == "POST":
        form = ProductForm(id,request.POST or None, request.FILES or None,instance=instance )
        print("ERROR!!!\n",form.errors)
        if form.is_valid():
            category_id = request.POST.get('category')
            subcategory_id = request.POST.get('subcategory')
            category= Category.objects.get(id=int(category_id))
            subcategory= SubCategory.objects.get(id=int(subcategory_id))
            form.category = category
            form.subcategory = subcategory
            form.save()
            return redirect("/dashboard/products")
        else:
            print("ERROR !!! Unable to validate form ")
            return redirect("/dashboard/add-product")

    form = ProductForm(p_id=id)
    print("Form Data = ",form.product.name)
    categories=Category.objects.all()
    subcategories=SubCategory.objects.all()
    return render(request, "01-edit-product.html", {"form":form,"categories":categories,"subcategories":subcategories})

# Add New Category
def add_category(request):
    if request.method == "POST":
        category_name = request.POST['new_category']
        category= Category.objects.create(name=category_name)
        category.save()
        return redirect("/dashboard/products")

    return redirect("/dashboard/products")

