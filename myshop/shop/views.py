from .models import Category, Product
from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }

    return render(request, 'shop/product/list.html', context)


def home(request):
    return render(request, 'shop/base.html')


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'shop/product/detail.html', {'product': product})
