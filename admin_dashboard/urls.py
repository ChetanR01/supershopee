from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from . import views

# from django.conf.urls import url
from . import views
app_name = 'admin_dashboard'

urlpatterns = [
    # re_path(r'^getSubcategory/$', views.get_subcategory),
    path('',views.index, name="index"),
    path('products/',views.product, name="products"),
    path('orders/',views.orders, name="orders"),
    path('create-order/',views.create_order, name="create-order"),
    path('update-order/<str:id>',views.update_order, name="update-order"),
    path('accounts/',views.account, name="accounts"),
    path('login/',views.login, name="login"),
    path('add-product/<int:id>',views.add_product, name="add-product"),
    path('edit-product/<int:id>',views.edit_product, name="edit-product"),
    path('add-category/',views.add_category, name="add-category"),
    
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)