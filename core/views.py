from django.shortcuts import render, get_object_or_404
from core.models import Category, Vendor, Tags, Product, ProductImages, CartOrder, CartOrderItems, ProductReview, wishlist, Address
from taggit.models import Tag
from django.db.models import Avg, Count
from core.forms import ProductReviewForm
from django.http import JsonResponse
from django.template.loader import render_to_string
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
    
    # Getting all reviews 
    reviews = ProductReview.objects.filter(product=product).order_by("-created_at")
    
    # Getting average reviews related to a product
    average_rating = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))
    
    # Product review form
    review_form = ProductReviewForm()
    
    # Calculate rating percentages
    total_reviews = reviews.count()
    rating_counts = reviews.values('rating').annotate(count=Count('rating')).order_by('-rating')
    rating_percentages = {rating: 0 for rating in range(1, 6)}
    for rating in rating_counts:
        rating_percentages[rating['rating']] = (rating['count'] / total_reviews) * 100 if total_reviews else 0

    # Make review 
    make_review = True
    
    if request.user.is_authenticated:
        user_review_count =ProductReview.objects.filter(user=request.user, product=product).count()
        
        if user_review_count > 0:
            make_review = False 

    context = {
        'product': product,
        'p_image': p_image,   
        'products': products,
        'reviews': reviews,   
        'review_form':review_form,
        'average_rating': average_rating,  
        'rating_percentages': rating_percentages,
        'total_reviews': total_reviews,
        'make_review': make_review
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
    
def ajax_add_review(request, pid):
    product = get_object_or_404(Product, pk=pid)
    user = request.user #This enables us to get the logged in user
    
    review = ProductReview.objects.create(
        user=user,
        product=product,
        review=request.POST['review'],       
        rating=request.POST['rating'],      
    )
    
    context = {
        'user':user.username,
        'review':request.POST['review'],
        'rating':request.POST['rating'],
    }
    
    average_reviews = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))
    
    return JsonResponse(
        {
            'bool':True,
            'average_reviews':average_reviews,
            'context':context,            
        }
    )
    

def search_view(request):
    query = request.GET.get("q")
    
    products = Product.objects.filter(title__icontains=query, description__icontains=query).order_by("-created_at")
    
    
    context = {
        'products':products,
        'query':query
    }
    
    return render(request, "core/search.html", context)

def filter_product_view(request):
    categories = request.GET.getlist('category[]')
    vendors = request.GET.getlist('vendor[]')
    min_price = request.GET['min_price']
    max_price = request.GET['max_price']
    
    
    products = Product.objects.filter(product_status="published").order_by("-id").distinct()
    
    products = products.filter(price__gte=min_price)
    products = products.filter(price__lte=max_price)
    
    if len(categories) > 0:
        products = products.filter(category__id__in=categories).distinct() 
        
    if len(vendors) > 0:
        products = products.filter(vendor__id__in=vendors).distinct() 
    
    context = {
        'products':products
    }
        
    data = render_to_string("core/async/product-list.html", context )
    return JsonResponse({'data':data})
        
        
    
