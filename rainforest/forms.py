from .models import Product, Review
from django.forms import CharField, PasswordInput, Form, ModelForm

class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'description', 'price_in_cents']

class ReviewForm(ModelForm):

    class Meta:
        model = Review
        fields = ['message']
    # def clean(self): 
        

    #     cleaned_data = super().clean()     
    #     body = cleaned_data.get('body')

    #     if len(body) < 2: 
    #         self.add_error('body', 'Body must be longer than one character.')      
    #     return cleaned_data 