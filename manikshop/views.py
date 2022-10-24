import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth 
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.core.paginator import Paginator
from django.template.loader import render_to_string, get_template

from .models import ProductDetails


from django.shortcuts import render
from .models import SubCategory, Category
from django.http import HttpResponse
import json

def get_subcategory(request):
    id = request.GET.get('id', '')
    result = list(SubCategory.objects.filter(category_id=int(id)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")

# Create your views here.
def index(request):
    products = ProductDetails.objects.all()
    all_categories= Category.objects.all()
    sub_categories= SubCategory.objects.all()
    return render(request, "index.html", {"all_categories":all_categories,"sub_categories":sub_categories,"products":products})

def product(request,id):
    product = ProductDetails.objects.filter(id=id)
    all_categories= Category.objects.all()
    sub_categories= SubCategory.objects.all()
    return render(request, "product.html", {"all_categories":all_categories,"sub_categories":sub_categories,"product":product})

def single(request, id):
    product = ProductDetails.objects.filter(id=id)
    all_categories= Category.objects.all()
    sub_categories= SubCategory.objects.all()
    print("####", product)
    return render(request, "single.html", {"all_categories":all_categories,"sub_categories":sub_categories,"products":product})

def default_search(request):
    all_categories= Category.objects.all()
    sub_categories= SubCategory.objects.all()
    if request.method == "GET":
        search_for =  request.GET.get('search') 
        print("Searched for:",search_for)
    product = ProductDetails.objects.filter(name__icontains=search_for)
    return render(request, "search.html", {"all_categories":all_categories,"sub_categories":sub_categories,"product":product})

def search(request,search_type,id):
    all_categories= Category.objects.all()
    sub_categories= SubCategory.objects.all()
    if search_type =="category":
        product = ProductDetails.objects.filter(category=id)
        return render(request, "search.html", {"all_categories":all_categories,"sub_categories":sub_categories,"product":product})
    elif search_type =="subcategory":
        product = ProductDetails.objects.filter(subcategory=id)
        return render(request, "search.html", {"all_categories":all_categories,"sub_categories":sub_categories,"product":product})
    # elif request.method=="GET" and search_type =="default":
    #     product = ProductDetails.objects.filter(name__contains=request)
    #     return render(request, "search.html", {"product":product})


def about(request):
    all_categories= Category.objects.all()
    sub_categories= SubCategory.objects.all()
    return render(request, "about.html", {"all_categories":all_categories,"sub_categories":sub_categories})

def contact(request):
    products = ProductDetails.objects.all()
    all_categories= Category.objects.all()
    sub_categories= SubCategory.objects.all()
    return render(request, "contact.html", {"all_categories":all_categories,"sub_categories":sub_categories})

def checkout(request):
    products = ProductDetails.objects.all()
    all_categories= Category.objects.all()
    sub_categories= SubCategory.objects.all()
    return render(request, "checkout.html", {"all_categories":all_categories,"sub_categories":sub_categories})

def faqs(request):
    products = ProductDetails.objects.all()
    all_categories= Category.objects.all()
    sub_categories= SubCategory.objects.all()
    return render(request, "faqs.html", {"all_categories":all_categories,"sub_categories":sub_categories})

def help(request):
    products = ProductDetails.objects.all()
    all_categories= Category.objects.all()
    sub_categories= SubCategory.objects.all()
    return render(request, "help.html", {"all_categories":all_categories,"sub_categories":sub_categories})

def terms(request):
    products = ProductDetails.objects.all()
    all_categories= Category.objects.all()
    sub_categories= SubCategory.objects.all()
    return render(request, "terms.html", {"all_categories":all_categories,"sub_categories":sub_categories})

def payment(request):
    products = ProductDetails.objects.all()
    all_categories= Category.objects.all()
    sub_categories= SubCategory.objects.all()
    return render(request, "payment.html", {"all_categories":all_categories,"sub_categories":sub_categories})

def privacy(request):
    products = ProductDetails.objects.all()
    all_categories= Category.objects.all()
    sub_categories= SubCategory.objects.all()
    return render(request, "privacy.html", {"all_categories":all_categories,"sub_categories":sub_categories})

def signup(request):
    if request.method== "POST":
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['email']
        password = request.POST['password']
        confirm_pass = request.POST['confirm_pass']

        print("Name =",name)
        print("Email =",email)
        print("Pass =",password)
        print("Confirm Pass =",confirm_pass)
        
        if password == confirm_pass:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username is Already Used!")
                return redirect('/')
            else:
                user = User.objects.create_user(username=username,password= password, email=email, first_name=name)
                user.save()
                messages.info(request,"Your have successfully created account, Login Now!")

                # # to send welcome email
                # raw_data= {
                #     "name":name,
                #     "email":email,
                #     "username":username,
                #     "password":password,
                # }
                # html_template= "email_signup.html"
                # msg_for_new_user = render_to_string(html_template, context=raw_data)

                # msg= EmailMessage(
                #     "Your account is created successfully ",
                #     msg_for_new_user,
                #     'crrathod.tech@gmail.com' ,#from 
                #     [f'{email}'] ,
                # )

                # msg.content_subtype ="html"
                # msg.send()
                               
                # print(f"Email Sent to User on >. {email}")

                return redirect('/')

        else:
            messages.info(request,"Password Not matching!")
            return redirect('/')

    else:
        return render(request, "/")

def login(request):
    if request.method== "POST":
        username = request.POST['email']
        password = request.POST['password']
        user= auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            print(f"User {username} is loged in")
            messages.info(request,"You are successfully Loged In")
            return redirect("/")
        else:
            messages.info(request,"Invalid Credentials!")
            print("Invalid Login detaisl")
            return redirect("/")

    else:
        return render(request, "/")

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect("/")