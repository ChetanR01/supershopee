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

# def add_product(request):
#     products = ProductDetails.objects.all()
#     categories = Category.objects.all()
#     subcategories = SubCategory.objects.all()
#     return render(request, "01-add-product.html", {"categories":categories,"subcategories":subcategories})

def add_product(request):
    if request.method == "POST":
        # form = ProductForm(request.POST or None, request.FILES or None)
        
        name = request.POST['name']
        product_details = request.POST['product_details']
        category_id = request.POST.get('category')
        subcategory_id = request.POST.get('subcategory')
        category= Category.objects.get(id=int(category_id))
        subcategory= SubCategory.objects.get(id=int(subcategory_id))
        price = request.POST['price']
        mrp = request.POST['mrp']
        main_img = request.POST['main_img']
        img1 = request.POST['img1']
        img2 = request.POST['img2']
        img3 = request.POST['img3']
        product = ProductDetails.objects.create(name=name,product_details=product_details,category=category,subcategory=subcategory,price=price,mrp=mrp,main_img=main_img,img1=img1,img2=img2,img3=img3)
        product.save()
        print("Product Saved !!!!!!!!!!!!!!!!!")

        # return redirect("/dashboard/products")
        # print("ERRORS @@@@@#!@@@@@@@@@@@@@")
        # print(form.errors )
        # if form.is_valid():
        #     category_id = request.POST.get('category')
        #     subcategory_id = request.POST.get('subcategory')
        #     category= Category.objects.get(id=int(category_id))
        #     subcategory= SubCategory.objects.get(id=int(subcategory_id))
        #     form.category = category
        #     form.subcategory = subcategory
        #     form.save()
        #     return redirect("/dashboard/products")
        # else:
        #     print("ERROR !!!!!!!!!!!!!!!!!!")
        #     name = request.POST['name']
        #     product_details = request.POST['product_details']
        #     category_id = request.POST.get('category')
        #     subcategory_id = request.POST.get('subcategory')
        #     price = request.POST['price']
        #     mrp = request.POST['mrp']
        #     img = request.POST['main_img']
        #     # "name","category","subcategory","price","mrp","product_details","main_img","img1","img2","img3"
        #     print("Name = ",name)
        #     print("category = ",category_id)
        #     print("subcategory = ",subcategory_id)
        #     print("Price = ",price)
        #     print("MRP = ",mrp)
        #     print("Details = ",product_details)
        #     print("main_img = ",img)

    form = ProductForm()
    categories=Category.objects.all()
    subcategories=SubCategory.objects.all()
    return render(request, "01-add-product.html", {"form":form,"categories":categories,"subcategories":subcategories})


def add_new_product(request):
    if request.method =="POST":
        name = request.POST['name']
        product_details = request.POST['product_details']
        category_id = request.POST.get('category')
        subcategory_id = request.POST.get('subcategory')
        price = request.POST['price']
        mrp = request.POST['mrp']
        img = request.POST['photo']
        print("Name=",name)
        print("product=",product_details)
        print("Category=",category_id)
        print("price=",price)
        print("MRP=",mrp)
        print("Photo=",img)
        category= Category.objects.get(id=int(category_id))
        subcategory= SubCategory.objects.get(id=int(subcategory_id))
        product = ProductDetails(name=name,product_details=product_details,category=category,subcategory=subcategory,price=price,mrp=mrp,main_img=img)
        product.save()
        print("Save !!!!!!!!!!!!!!")
    return redirect("/dashboard/products")

def edit_product(request,id):
    product = ProductDetails.objects.get(id=id)
    categories= Category.objects.all()
    return render(request, "01-edit-product.html", {"product":product,"categories":categories})

def update_product(request,id):
    product = ProductDetails.objects.get(id=id)
    if request.method =="POST":
        name = request.POST['name']
        product_details = request.POST['product_details']
        category_id = request.POST.get('category')
        price = request.POST['price']
        mrp = request.POST['mrp']
        product.name = name
        product.product_details = product_details
        category= Category.objects.get(id=category_id)
        product.category = category
        product.price = price
        product.mrp = mrp
        product.save()
    return redirect("/dashboard/products")