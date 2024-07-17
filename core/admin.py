from django.contrib import admin
from core.models import Category, Vendor, Tags, Product, ProductImages, CartOrder, CartOrderItems, ProductReview, wishlist, Address


class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages
    
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ['vendor', 'title', 'product_image','category', 'formatted_price', 'featured', 'product_status', 'pid']
    
    readonly_fields = ['pid']
    def formatted_price(self, obj):
        return f"${obj.price}" 

    formatted_price.short_description = 'Price'  

    
class CategoryAdmin(admin.ModelAdmin):    
    list_display = ['title', 'category_image']
    
class VendorAdmin(admin.ModelAdmin):    
    list_display = ['title', 'vendor_image']
    
class CartOrderAdmin(admin.ModelAdmin):    
    list_display = ['user', 'formatted_price', 'paid_status', 'order_date', 'order_status']
    
    def formatted_price(self, obj):
        return f"${obj.price}" 

    
class CartOrderItemsAdmin(admin.ModelAdmin):    
    list_display = ['order', 'item', 'image', 'quantity', 'formatted_price', 'formatted_total', 'display_summary']

    def formatted_price(self, obj):
        return f"${obj.price}" 

class ProductReviewAdmin(admin.ModelAdmin):    
    list_display = ['user', 'product', 'review', 'rating']
    
class WishListAdmin(admin.ModelAdmin):    
    list_display = ['user', 'product', 'created_at']
    
class AddressAdmin(admin.ModelAdmin):    
    list_display = ['user', 'address', 'status']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(Tags)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderItems, CartOrderItemsAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(wishlist, WishListAdmin)
admin.site.register(Address, AddressAdmin)


