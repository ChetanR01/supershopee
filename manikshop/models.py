from django.db import models

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
        


class ProductDetails(models.Model):
    name= models.CharField(max_length=100)
    price= models.FloatField()
    mrp= models.FloatField()
    main_img = models.ImageField(upload_to='product_img')
    img1 = models.ImageField(upload_to='product_img')
    img2 = models.ImageField(upload_to='product_img')
    img3 = models.ImageField(upload_to='product_img')
    # category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    # subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT, default=1)
    category = models.ForeignKey(Category, related_name='produits', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, related_name='produits', on_delete=models.CASCADE)
    product_details = RichTextField(blank=True, null=True)
    trending = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
