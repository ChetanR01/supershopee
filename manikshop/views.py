from django.shortcuts import render

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