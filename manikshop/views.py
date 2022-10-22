import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth 
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.core.paginator import Paginator
from django.template.loader import render_to_string, get_template

# Create your views here.
def index(request):

    return render(request, "index.html", {})

def product(request):
    return render(request, "product.html", {})

def single(request):
    return render(request, "single.html", {})

def about(request):
    return render(request, "about.html", {})

def contact(request):
    return render(request, "contact.html", {})

def checkout(request):
    return render(request, "checkout.html", {})

def faqs(request):
    return render(request, "faqs.html", {})

def help(request):
    return render(request, "help.html", {})

def terms(request):
    return render(request, "terms.html", {})

def payment(request):
    return render(request, "payment.html", {})

def privacy(request):
    return render(request, "privacy.html", {})

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