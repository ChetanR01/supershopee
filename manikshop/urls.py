from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index" ),
    path('product',views.product, name="product" ),
    path('single',views.single, name="single"),
    path('about',views.about, name="about" ),
    path('contact',views.contact, name="contact"),
    path('checkout',views.checkout, name="checkout"),
    path('faqs',views.faqs, name="faqs"),
    path('help',views.help, name="help"),
    path('terms',views.terms, name="terms"),
    path('payment',views.payment, name="payment"),
    path('privacy',views.privacy, name="privacy"),
    path('signup',views.signup, name="signup"),
    path('login',views.login, name="login"),
    path('logout',views.logout, name="logout"),
]