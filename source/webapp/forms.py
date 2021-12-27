from django import forms
from django.db.models.fields import DecimalField
from django.forms.forms import Form

class ProductForm(forms.Form):
    CATEGORY_CHOISES = [
        ('other', 'Other'),
        ('phones', 'Phones'),
        ('headPhones', 'Head phones'),
        ('memory', 'Memory'),
        ('hdd', 'HDD')
    ]
    title = forms.CharField(max_length=100, required=True, label='Title')
    description = forms.CharField(max_length=2000, required=False, label='Description')
    category = forms.ChoiceField(choices=CATEGORY_CHOISES, required=False, label='Category')
    remainder = forms.IntegerField(min_value=0, label='Remainder')
    cost = forms.DecimalField(max_digits=7, decimal_places=2, label='Cost')