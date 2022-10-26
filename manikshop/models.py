from datetime import date
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# for rich text
from ckeditor.fields import RichTextField

# for category
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

# for Sub-category
class SubCategory(models.Model):
    # category = models.ForeignKey(Category, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, related_name='souscategories', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name
        

# For Product details
class ProductDetails(models.Model):
    name= models.CharField(max_length=100)
    price= models.FloatField()
    mrp= models.FloatField()
    main_img = models.ImageField(upload_to='product_img')
    img1 = models.ImageField(upload_to='product_img')
    img2 = models.ImageField(upload_to='product_img')
    img3 = models.ImageField(upload_to='product_img')
    category = models.ForeignKey(Category, related_name='produits', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, related_name='produits', on_delete=models.CASCADE)
    product_details = RichTextField(blank=True, null=True)
    trending = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name


# For Order Table
class Order(models.Model):
    order_id = models.CharField(max_length=100, default="")
    cutomer_name = models.CharField(max_length=100)
    date = models.DateTimeField()
    address = models.CharField(max_length= 500)
    mobile_no = models.CharField(max_length = 12)
    order_list = models.ManyToManyField(to=ProductDetails, related_name="order_list", blank=False)
    order_state_list = [
        ('pending', 'Pending'),
        ('cancelled', 'Cancelled'),
        ('confirm', 'Confirm'),
        ('on_the_way', 'On the way'),    
        ('delivered', 'Delivered'),    
        ]
    order_status = models.CharField(max_length=50, choices=order_state_list, default="pending")

    payment_state_list = [
        ('pending', 'Pending'),
        ('cancelled', 'Cancelled'),
        ('confirm', 'Confirm') 
        ]
    payment_status = models.CharField(max_length=50, choices=payment_state_list, default="pending")
    transaction_id = models.CharField(max_length=100)

    # Generate Order Id
    def get_order_id(self):
        today = date.today()
        no_date = str(today).split("-")
        return f"{no_date[2]}{no_date[1]}{no_date[0]}{self.id}"

    def save(self, *args, **kwargs):
        self.order_id = self.get_order_id()
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return self.order_id


# for Cart
class Cart(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    products= models.ManyToManyField(to=ProductDetails, related_name="cart", blank=True)

    def __str__(self):
        return self.name.first_name

# for Deals
class Deal(models.Model):
    id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=100)
    banner = models.ImageField(upload_to='deals')
    offer_line= models.CharField(max_length=300)
    products= models.ManyToManyField(to=ProductDetails, related_name="deals", blank=True)
    start_date= models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name

# Extended user
class Extended_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=12)
    address = models.CharField(max_length=500)
    # user_image = CloudinaryField('profile_img')
    # user_image = models.ImageField(upload_to='profile_img', default="/assets/assets/images/profile_photo.jpg")

    def __str__(self):
        return self.user.first_name

# Subscription table
class Subscription(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    date = models.DateField()

    def __str__(self):
        return self.name