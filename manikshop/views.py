import datetime
from traceback import print_tb
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth 
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.core.paginator import Paginator
from django.template.loader import render_to_string, get_template
from django.db.models import Q


from .models import ProductDetails


from django.shortcuts import render
from .models import SubCategory, Category, Extended_user,Deal, Subscription, Cart, Order
from django.http import HttpResponse
import json

def get_subcategory(request):
    id = request.GET.get('id', '')
    result = list(SubCategory.objects.filter(category_id=int(id)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")

# Create your views here.
def index(request):
    products = ProductDetails.objects.all()
    deals = Deal.objects.filter(end_date__gte=datetime.datetime.now())
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
    deal_product = Deal.objects.get(id=id)
    products = deal_product.products.all()

    print("Products",products)
    # print("Deal Products",deal_product)
    # print("Deal Products. products",deal_product)
    # for products in deal_product:
    #     # for products in deal.products:
    #     no_pro = len(products)
    #     print("No product",no_pro)


    p = Paginator(products, 21)
    page_no= request.GET.get('page')

    try:
        page_obj = p.get_page(page_no)
    except PageNotAnInteger:
        page_obj=p.page(1)
    except EmptyPage:
        page_obj=p.page(p.num_pages)

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
    return render(request, "deal-product.html", {"all_categories":all_categories,"sub_categories":sub_categories,"products":page_obj,"no_col":no_col,"deals":deals,"deal_product":deal_product})

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
        

# add item to cart
def add_cart(request,id):
    if request.method == "POST":
        if request.user.is_authenticated:
            try:
                my_cart = Cart.objects.get(name=request.user)
                if my_cart:
                    my_cart.products.add(id)
                    messages.info(request,"Item Added to Cart")
                    my_cart.save()
            except:
                new_cart = Cart.objects.create(name=request.user)
                new_cart.products.add(id)
                messages.info(request,"Item Added to Cart")
                new_cart.save()
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
        else:
            messages.info(request, "Please login before adding products to cart")
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
            

    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)

# remove item from cart
def remove_cart(request,id):
    if request.user.is_authenticated:
        my_cart = Cart.objects.get(name=request.user)
        if my_cart:
            my_cart.products.remove(id)
            messages.info(request,"Item Removed from Cart")
            my_cart.save()
        return redirect("/checkout")

# track order
def track_order(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            order_id = request.POST['order_id']
            order_date = request.POST['order_date']
            print("Order date", order_date)
            orders = Order.objects.filter(order_id=order_id)
            for order in orders:
                one_order = order
            status = one_order.order_status
            print("Status",status)
            messages.info(request, f"Your Order status is '{status}'")
        return redirect("/")

# to place order item from cart
def place_order(request):
    if request.method== "POST":
        item_count = request.POST['item_count']
        product_dict = {}
        for i in range(1,int(item_count)+1):
            product_dict[f"product{i}"]= request.POST[f'product{i}']
            product_dict[f"quantity{i}"]= request.POST[f'quantity{i}']

        from itertools import islice
        values = product_dict.values()
        length_to_split =  [2 for i in range(len(values)//2)]
        Inputt = iter(values)
        Output = [list(islice(Inputt, elem)) for elem in length_to_split]
        # print(Output)
        
        for rec in Output:
            product = ProductDetails.objects.get(id=int(rec[0]))
            create_order = Order.objects.create(cutomer_name=request.user, date= datetime.datetime.now(), product= product, quantity= int(rec[1]))
            create_order.save()
        messages.info(request, "Order placed successfully!, Thank For Shopping With Us 🙂")
            
        # print("Product Dict is : ",product_dict)
        
        return redirect("/checkout")
    return redirect("/checkout")

def about(request):
    return render(request, "about.html", {})

def contact(request):
    return render(request, "contact.html", {})

def checkout(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(name=request.user.id)
        return render(request, "checkout.html", {"cart":cart})
    else:
        messages.info(request, "Please login to check your cart")
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

        
        if password == confirm_pass:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username is Already Used!")
                return redirect('/')
            else:
                user = User.objects.create_user(username=username,password= password, email=email, first_name=name)
                user.save()
                messages.info(request,"Your have successfully created account, Login Now!")

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
        if request.user.is_authenticated:
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
        else:
            messages.info(request,"Please login to check/update your profile")
            return redirect('/')

    return render(request, "index.html")


def subscription(request):
    if request.method== "POST":
        if request.user.is_authenticated:
            predata = User.objects.get(id=request.user.id)
            name= predata.first_name
        else:
            temp_name = request.POST['email']
            name = temp_name.split('@')[0]
        email = request.POST['email']
        sub_data = Subscription(name=name, email = email, date= datetime.date.today())
        sub_data.save()
        messages.info(request,"Your Email is added to our subscribers list, Thank You!")
        
        return redirect("/")
    return redirect("/")

