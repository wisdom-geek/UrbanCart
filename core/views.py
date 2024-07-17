from django.shortcuts import render, get_object_or_404
from core.models import Category, Vendor, Tags, Product, ProductImages, CartOrder, CartOrderItems, ProductReview, wishlist, Address
from taggit.models import Tag

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

def category_product_list_view(request, title):
    category = Category.objects.get(title=title)
    products = Product.objects.filter(product_status="published", category=category) 
    
    context = {
        'category':category,
        'products':products
    }
    
    return render(request, 'core/category-product-list.html', context)
    
def vendor_list_view(request):
    vendors = Vendor.objects.all()
    context = {
        'vendors': vendors
    }  
    
    return render(request, 'core/vendor-list.html', context)

def vendor_detail_view(request, vid):
    vendors = Vendor.objects.get(vid=vid)
    products = Product.objects.filter(product_status="published", vendor=vendors )
    
    context = {
        'vendors': vendors,
        'products':products
    }  
    
    return render(request, 'core/vendor-detail.html', context)

def product_detail_view(request, pid):
    product = get_object_or_404(Product, pid=pid)
    products = Product.objects.filter(category=product.category).exclude(pid=pid)
    
    p_image = product.p_images.all()
    
    context ={
        'product':product,
        'p_image':p_image,   
        'products': products     
    }
    
    return render(request, 'core/product-detail.html', context)

def tag_list(request, tag_slug=None):
    products = Product.objects.filter(product_status="published").order_by("-created_at")
    
    tag = None
    
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        products = products.filter(tags__in=[tag])
        
    context ={
        'products':products,
        'tag':tag
    }
    
    return render(request, 'core/tag.html', context)
    

    