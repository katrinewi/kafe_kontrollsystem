from django import forms

# Form with fields for name, price and default value for number(numbersSold in models)
class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)
    number = 0
