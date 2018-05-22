from django import forms

class ProductForm(forms.Form):
    Produktnavn = forms.CharField(required=True)
    Pris = forms.FloatField(required=True)
    number = 0
