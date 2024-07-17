from core.models import Category, Vendor, Tags, Product, ProductImages, CartOrder, CartOrderItems, ProductReview, wishlist, Address

def default(request):
    categories = Category.objects.all()
    
    address = None
    if request.user.is_authenticated:
        try:
            address = Address.objects.get(user=request.user)
        except Address.DoesNotExist:
            address = None
    
    return {
        'categories': categories,
        'address': address,
    }