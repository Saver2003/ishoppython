from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Product
from webapp.forms import ProductForm

# Create your views here.

def index_view(request):
    CATEGORY_CHOISES = [
        ('other', 'Other'),
        ('phones', 'Phones'),
        ('headPhones', 'Head phones'),
        ('memory', 'Memory'),
        ('hdd', 'HDD')
    ]
    
    products = Product.objects.order_by("category", "title")
    return render(request, 'index.html', context={'products': products, 'choises': CATEGORY_CHOISES})

def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    print(product.category)
    return render(request, 'product_view.html', context={'product': product})

def create_product_view(request):
    if (request.method == 'GET'):
        form = ProductForm()
        return render(request, 'create_product.html', context={'form': form})
    elif (request.method == 'POST'):
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product = Product.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                category=form.cleaned_data['category'],
                remainder=form.cleaned_data['remainder'],
                cost=form.cleaned_data['cost']
            )
            return redirect(product_view, pk=product.pk)
        else:
            return render(request, 'create_product.html', context={'form': form})

def update_product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if (request.method == 'GET'):
        form = ProductForm(initial={
            'title': product.title,
            'description': product.description,
            'category': product.category,
            'remainder': product.remainder,
            'cost': product.cost
        })
        return render(request, 'update_product.html', context={'form': form, 'product': product})
    elif (request.method == 'POST'):
        form = ProductForm(data=request.POST)
        if (form.is_valid()):
            product.title = form.cleaned_data['title']
            product.description = form.cleaned_data['description']
            product.category = form.cleaned_data['category']
            product.remainder = form.cleaned_data['remainder']
            product.cost = form.cleaned_data['cost']
            product.save()
            return redirect(product_view, pk=product.pk)
        else:
            return render(request, 'update_product.html', context={'form': form, 'product': product})


def delete_product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if (request.method == 'GET'):
        return render(request, 'delete_product.html', context={'product': product})
    elif (request.method == 'POST'):
        product.delete()
        return redirect('index')
        
