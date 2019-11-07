from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from datetime import datetime

def home(request):
    products = Product.objects.all()
    return render(request, 'products/home.html', {'products': products})

@login_required(login_url="/accounts/login/")
def create_product(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['description'] and request.POST['url'] and request.FILES['image'] and request.FILES['icon']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['description']
            product.url = request.POST['url']
            product.pub_date = datetime.now()
            product.image = request.FILES['image']
            product.icon = request.FILES['icon']
            product.hunter = request.user
            product.save()
            return redirect(f'/products/{product.id}')
        else:
            return render(request, 'products/create_product.html', {'error': 'All fields are required'})
    else:
        return render(request, 'products/create_product.html')

def product_detail(request, product_id):
    # throws 404 if product is not found, pk is taken from url
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/product_detail.html', {'product': product})

@login_required(login_url="/accounts/login/")
def upvote_product(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.votes_total += 1
        product.save()
    return redirect(f'/products/{product_id}')