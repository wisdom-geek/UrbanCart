from django.shortcuts import render
from django.http import HttpResponse
from core.models import Category, Vendor, Tags, Product, ProductImages, CartOrder, CartOrderItems, ProductReview, wishlist, Address


# Create your views here.

def index(request):
    # products = Product.objects.all().order_by("-created_at")    
    products = Product.objects.filter(featured=True, product_status="published")  
    
    context ={
        "products":products,
    }
    
    return render(request, 'core/index.html', context)

def product_list_view(request):
    products = Product.objects.filter(product_status="published") 
    context ={
        "products":products,
    }
    
    return render(request, 'core/product-list.html', context)

def category_list_view(request):
    categories = Category.objects.all()
    
    context = {
        "categories":categories
    }
    
    return render(request, 'core/category-list.html', context)
    
    