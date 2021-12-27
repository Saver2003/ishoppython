from django.contrib import admin
from webapp.models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'cost']
    list_filter = ['id', 'title', 'category', 'cost']
    search_fields = ['title', 'category']
    fields = ['title', 'description', 'category', 'remainder', 'cost']

admin.site.register(Product, ProductAdmin)