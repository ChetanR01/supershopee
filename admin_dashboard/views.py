from django.shortcuts import render, redirect
from manikshop.models import ProductDetails, Category, SubCategory,Order

from .forms import ProductForm

def index(request):
    orders = Order.objects.all().order_by("-date")
    return render(request, "01-index.html", {"orders":orders})

def orders(request):
    orders = Order.objects.all().order_by("-date")
    return render(request, "01-orders.html", {"orders":orders,})

def create_order(request):
    orders = Order.objects.all().order_by("-date")
    return render(request, "01-create-order.html", {"orders":orders,})

def update_order(request,id):
    orders = Order.objects.filter(order_id=id)

    if request.method=="POST":
        order_status = request.POST.get('order_status')
        payment_status = request.POST.get('payment_status')

        for order in orders:
            order.order_status=order_status
            order.payment_status=payment_status
            order.save()
        return redirect("/dashboard/orders")

    grand_total=0
    for order in orders:
        rep_order=order
        grand_total+=order.total_cost
    return render(request, "01-update-order.html", {"orders":orders,"rep_order":rep_order,"grand_total":grand_total})

def product(request):
    products = ProductDetails.objects.all()
    raw_id=1
    for product in products:
        raw_id = product.id
    categories = Category.objects.all()
    return render(request, "01-products.html", {"products":products,"categories":categories,"raw_id":raw_id})

def account(request):
    products = ProductDetails.objects.all()
    return render(request, "01-accounts.html", {})

def login(request):
    products = ProductDetails.objects.all()
    return render(request, "01-login.html", {})

# Add new product
def add_product(request,id):
    if request.method == "POST":
        form = ProductForm(id,request.POST or None, request.FILES or None)
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
            return render(f"/dashboard/add-product/{id}")

    form = ProductForm(p_id=id)
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
            return redirect(f"/dashboard/edit-product/{id}")

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

