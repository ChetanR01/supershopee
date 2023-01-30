from django import forms
from django.forms import ModelForm
from manikshop.models import ProductDetails


class ProductForm(ModelForm):
    def __init__(self, p_id, *args, **kwargs):
        self.product = ProductDetails.objects.get(id=p_id)
       
        super(ProductForm, self).__init__(*args, **kwargs)

    class Meta:
        model= ProductDetails
        fields= ("name","category","subcategory","price","mrp","product_details","main_img","img1","img2","img3")

        labels={
            "name":"Product Name",
            "product_details":"Description",
            "category":"Category",
            "subcategory":"Sub-Category",
            "price":"Price",
            "mrp":"MRP",
            "main_img":"Main Image",
            "img1":"Image 1",
            "img2":"Image 2",
            "img3":"Image 3",
        }

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control validate',}),
            'product_details':forms.TextInput(attrs={'class':'form-control validate',}),

            'category':forms.TextInput(attrs={'class':'custom-select tm-select-accounts',}),
            'subcategory':forms.TextInput(attrs={'class':'custom-select tm-select-accounts',}),

            'price':forms.TextInput(attrs={'class':'form-control validate',}),
            'mrp':forms.TextInput(attrs={'class':'form-control validate',}),

            'main_img':forms.FileInput(attrs={'class':'btn btn-primary btn-block mx-auto',}),
            'img1':forms.FileInput(attrs={'class':'btn btn-primary btn-block mx-auto',}),
            'img2':forms.FileInput(attrs={'class':'btn btn-primary btn-block mx-auto',}),
            'img3':forms.FileInput(attrs={'class':'btn btn-primary btn-block mx-auto',}),
            
        }