import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth 
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.core.paginator import Paginator
from django.template.loader import render_to_string, get_template
from django.db.models import Q


from .models import ProductDetails


from django.shortcuts import render
from .models import SubCategory, Category, Extended_user,Deal
from django.http import HttpResponse
import json

def get_subcategory(request):
    id = request.GET.get('id', '')
    result = list(SubCategory.objects.filter(category_id=int(id)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")

# Create your views here.
def index(request):
    products = ProductDetails.objects.all()
    deals = Deal.objects.all()
    all_categories= Category.objects.all()
    sub_categories= SubCategory.objects.all()
    return render(request, "index.html", {"all_categories":all_categories,"sub_categories":sub_categories,"products":products,"deals":deals})

def product(request):
    deals = Deal.objects.all()
    products = ProductDetails.objects.all()

    p = Paginator(products, 21)
    page_no= request.GET.get('page')

    try:
        page_obj = p.get_page(page_no)
    except PageNotAnInteger:
        page_obj=p.page(1)
    except EmptyPage:
        page_obj=p.page(p.num_pages)

    print(len(products))
    for product in page_obj:
        print(product)
    if len(page_obj) <= 3:
        no_col= 1
    elif len(page_obj) <= 6:
        no_col= 2
    elif len(page_obj) <= 9:
        no_col= 3
    elif len(page_obj) <= 12:
        no_col= 4
    elif len(page_obj) <= 15:
        no_col= 5
    elif len(page_obj) <= 18:
        no_col= 6
    elif len(page_obj) <= 21:
        no_col= 7
    all_categories= Category.objects.all()
    sub_categories= SubCategory.objects.all()
    return render(request, "product.html", {"all_categories":all_categories,"sub_categories":sub_categories,"products":page_obj,"no_col":no_col,"deals":deals})

def deal_product(request,id):
    deals = Deal.objects.all()
    deal_product = Deal.objects.filter(id=id)
    products = ProductDetails.objects.all()

    # print("Deal Products",deal_product)
    # print("Deal Products. products",deal_product)
    # for products in deal_product:
    #     # for products in deal.products:
    #     no_pro = len(products)
    #     print("No product",no_pro)


    p = Paginator(deal_product, 21)
    page_no= request.GET.get('page')

    try:
        page_obj = p.get_page(page_no)
    except PageNotAnInteger:
        page_obj=p.page(1)
    except EmptyPage:
        page_obj=p.page(p.num_pages)

    print(len(products))
    for product in page_obj:
        print(product)
    if len(page_obj) <= 3:
        no_col= 1
    elif len(page_obj) <= 6:
        no_col= 2
    elif len(page_obj) <= 9:
        no_col= 3
    elif len(page_obj) <= 12:
        no_col= 4
    elif len(page_obj) <= 15:
        no_col= 5
    elif len(page_obj) <= 18:
        no_col= 6
    elif len(page_obj) <= 21:
        no_col= 7
    all_categories= Category.objects.all()
    sub_categories= SubCategory.objects.all()
    return render(request, "deal-product.html", {"all_categories":all_categories,"sub_categories":sub_categories,"products":deal_product,"no_col":no_col,"deals":deals,"deal_product":deal_product})

def single(request, id):
    product = ProductDetails.objects.filter(id=id)
    for rel_pro in product:
        rel_category = rel_pro.category
    related_products = ProductDetails.objects.filter(category=rel_category)
    all_categories= Category.objects.all()
    sub_categories= SubCategory.objects.all()
    print("####", product)
    return render(request, "single.html", {"all_categories":all_categories,"sub_categories":sub_categories,"products":product,"related_products":related_products})

def default_search(request):
    deals = Deal.objects.all()
    all_categories= Category.objects.all()
    sub_categories= SubCategory.objects.all()
    if request.method == "GET":
        search_for =  request.GET.get('search') 
        print("Searched for:",search_for)
    products = ProductDetails.objects.filter(Q(name__icontains=search_for)| Q(product_details__icontains=search_for))

    print("Related results",products)
    
    p = Paginator(products, 21)
    page_no= request.GET.get('page')

    try:
        page_obj = p.get_page(page_no)
    except PageNotAnInteger:
        page_obj=p.page(1)
    except EmptyPage:
        page_obj=p.page(p.num_pages)

    print(len(products))
    for product in page_obj:
        print(product)
    if len(page_obj) <= 3:
        no_col= 1
    elif len(page_obj) <= 6:
        no_col= 2
    elif len(page_obj) <= 9:
        no_col= 3
    elif len(page_obj) <= 12:
        no_col= 4
    elif len(page_obj) <= 15:
        no_col= 5
    elif len(page_obj) <= 18:
        no_col= 6
    elif len(page_obj) <= 21:
        no_col= 7
    return render(request, "search.html", {"all_categories":all_categories,"sub_categories":sub_categories,"products":page_obj,"no_col":no_col,"deals":deals})


def search(request,search_type,id):
    deals = Deal.objects.all()
    all_categories= Category.objects.all()
    sub_categories= SubCategory.objects.all()
    if search_type =="category":
        products = ProductDetails.objects.filter(category=id)

        p = Paginator(products, 21)
        page_no= request.GET.get('page')

        try:
            page_obj = p.get_page(page_no)
        except PageNotAnInteger:
            page_obj=p.page(1)
        except EmptyPage:
            page_obj=p.page(p.num_pages)

        print(len(products))
        for product in page_obj:
            print(product)
        if len(page_obj) <= 3:
            no_col= 1
        elif len(page_obj) <= 6:
            no_col= 2
        elif len(page_obj) <= 9:
            no_col= 3
        elif len(page_obj) <= 12:
            no_col= 4
        elif len(page_obj) <= 15:
            no_col= 5
        elif len(page_obj) <= 18:
            no_col= 6
        elif len(page_obj) <= 21:
            no_col= 7
        return render(request, "search.html", {"all_categories":all_categories,"sub_categories":sub_categories,"products":page_obj,"no_col":no_col,"deals":deals})
    elif search_type =="subcategory":
        products = ProductDetails.objects.filter(subcategory=id)
        p = Paginator(products, 21)
        page_no= request.GET.get('page')

        try:
            page_obj = p.get_page(page_no)
        except PageNotAnInteger:
            page_obj=p.page(1)
        except EmptyPage:
            page_obj=p.page(p.num_pages)

        print(len(products))
        for product in page_obj:
            print(product)
        if len(page_obj) <= 3:
            no_col= 1
        elif len(page_obj) <= 6:
            no_col= 2
        elif len(page_obj) <= 9:
            no_col= 3
        elif len(page_obj) <= 12:
            no_col= 4
        elif len(page_obj) <= 15:
            no_col= 5
        elif len(page_obj) <= 18:
            no_col= 6
        elif len(page_obj) <= 21:
            no_col= 7
        return render(request, "search.html", {"all_categories":all_categories,"sub_categories":sub_categories,"products":page_obj,"no_col":no_col,"deals":deals})
        


def about(request):
    all_categories= Category.objects.all()
    sub_categories= SubCategory.objects.all()
    return render(request, "about.html", {"all_categories":all_categories,"sub_categories":sub_categories})

def contact(request):
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

def profile(request):
    if request.method== "POST":
        predata = User.objects.get(id=request.user.id)
        name = request.POST['name']
        email = request.POST['email']
        mobile_no = request.POST['mobile_no']
        address = request.POST['address']
        predata.first_name = name
        predata.email = email
        predata.username = email

        try:
            data_check =  Extended_user.objects.get(user = predata)
            print("data checker", data_check)
        except:
            data_check = False
        # if mobile no. or photo already uploaded
        if data_check:
            try:
                data_check.address = address
                if len(mobile_no)<=12:
                    data_check.mobile_no = mobile_no
                else:
                    messages.info(request,"Please enter valid mobile number (max length 12)")
                    return redirect('/')
            except:
                data_check.address= address
                if len(mobile_no)<=12:
                    data_check.mobile_no = mobile_no
                else:
                    messages.info(request,"Please enter valid mobile number (max length 12)")
                    return redirect('/')
            data_check.save()
        else:
            try:
                 
                if len(mobile_no)<=12:
                    ext_data = Extended_user(user=predata, mobile_no = mobile_no, address= address)  
                else:
                    messages.info(request,"Please enter valid mobile number (max length 12)")
                    return redirect('/')
            except:
                if len(mobile_no)<=12:
                    ext_data = Extended_user(user=predata, mobile_no = mobile_no, address= address) 
                else:
                    messages.info(request,"Please enter valid mobile number (max length 12)")
                    return redirect('/')
            ext_data.save()
                   
        predata.save()   

        messages.info(request,"Your account details successfully updated")

        return redirect('/')
    return render(request, "index.html")