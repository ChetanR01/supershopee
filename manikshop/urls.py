from django.urls import path, re_path
from . import views

# from django.conf.urls import url
from . import views
app_name = 'manikshop'

urlpatterns = [
    re_path(r'^getSubcategory/$', views.get_subcategory),
    path('',views.index, name="index" ),
    path('product/<int:id>',views.product, name="product" ),
    path('search/<str:search_type>/<int:id>',views.search, name="search" ),
    path('default_search',views.default_search, name="default_search"),
    path('single/<int:id>',views.single, name="single"),
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