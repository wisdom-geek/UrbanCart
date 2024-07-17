from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from userauths.models import User


# Create your models here.

'''
######################## Cart order choices ########################
'''
STATUS_CHOICE = (
    ('process', 'Processing'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered'),
)
'''
######################## Product status choices ########################
'''
STATUS = (
    ('draft', 'Draft'),
    ('disabled', 'Disabled'),
    ('rejected', 'Rejected'),
    ('in_review', 'In Review'),
    ('published', 'Published'),
)

'''
######################## Ratings choices ########################
'''
RATING = (
    (1, '★☆☆☆☆'),
    (2, '★★☆☆☆'),
    (3, '★★★☆☆'),
    (4, '★★★★☆'),
    (5, '★★★★★'),
)


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

'''
######################## Categories, Vendor, Tags, Product, Product Images ########################
'''

'''
######################## Product categories ########################
'''
class Category(models.Model):
    cid = ShortUUIDField(unique=True,length=10,max_length=20, prefix='cat', alphabet= 'abcdefghij12345')
    title = models.CharField(max_length=100, default="phones")
    image = models.ImageField(upload_to='category', default="category.jpg")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'categories'
        
    def category_image(self):
        return mark_safe(f'<img src="{self.image.url}" width="50" height="50"/>')
    
    def __str__(self):
        return self.title
'''
######################## Vendors ########################
'''
class Vendor(models.Model):
    vid = ShortUUIDField(unique=True,length=10,max_length=20, prefix='ven', alphabet= 'abcdefghij12345')
    title = models.CharField(max_length=100, default="John Doe")
    image = models.ImageField(upload_to=user_directory_path, default="vendor.jpg")
    description = models.TextField(default="Welcome to [Vendor Name]! We are passionate about delivering high-quality products and exceptional customer service. Our extensive collection includes everything from the latest trends to timeless classics, ensuring that you find exactly what you're looking for. At [Vendor Name], we believe in the power of choice and strive to offer a diverse range of products to suit every need and preference. Whether you're shopping for yourself or looking for the perfect gift, our dedicated team is here to make your experience seamless and enjoyable. Explore our store today and discover why [Vendor Name] is your go-to destination for quality and value.")
    address = models.CharField(max_length=100, default='123 Main street, London')
    contact = models.CharField(max_length=100, default="+123 (456) (789) ")
    chat_resp_time = models.CharField(max_length=100, default="100")
    shop_on_time = models.CharField(max_length=100, default="100")
    authentic_rating = models.CharField(max_length=100, default="100")
    days_return = models.CharField(max_length=100, default="100")
    warranty_period = models.CharField(max_length=100, default="100")
    user = models.ForeignKey(User, related_name='vendors', on_delete=models.SET_NULL, null=True)
    
    class Meta:
        verbose_name_plural = 'Vendors'
        
    def vendor_image(self):
        return mark_safe(f'<img src="{self.image.url}" width="50" height="50"/>')
    
    def __str__(self):
        return self.title

'''
######################## Tags ########################
'''    
class Tags(models.Model):
    class Meta:
        verbose_name_plural = 'Tags'        

'''
######################## Products ########################
'''    
class Product(models.Model):
    pid = ShortUUIDField(unique=True,length=10,max_length=20, prefix='prod', alphabet= 'abcdefghij12345')
    user = models.ForeignKey(User, related_name='products', on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.SET_NULL, null=True)
    vendor = models.ForeignKey(Vendor, related_name='products', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100, default="iphone 15")
    image = models.ImageField(upload_to=user_directory_path, default="product.jpg")
    description = models.TextField(null=True, blank=True, default="Introducing the [Product Name], the ultimate blend of innovation and style. Designed to cater to your dynamic lifestyle, this product stands out with its state-of-the-art features and sleek design. Whether you're at home, work, or on the go, the [Product Name] ensures seamless performance and unparalleled convenience. Explore a world of possibilities with this top-tier product that combines cutting-edge technology with user-friendly functionality. Experience the perfect harmony of efficiency and elegance, crafted to meet your every need and exceed your expectations.")
    price= models.DecimalField(max_digits=10, decimal_places=2, default="$1.99")
    old_price= models.DecimalField(max_digits=10, decimal_places=2, default="$2.99")
    specification = models.TextField(null=True, blank=True, default="- **Display**: 6.5-inch Full HD+ OLED, 1080 x 2400 pixels\n- **Processor**: Octa-core, 2.84 GHz\n- **RAM**: 8GB\n- **Storage**: 128GB internal, expandable up to 1TB via microSD\n- **Camera**: Triple rear cameras (64MP + 12MP + 5MP), 32MP front camera\n- **Battery**: 4500mAh, fast charging support\n- **Operating System**: Android 11, upgradable to Android 12\n- **Connectivity**: 5G, Wi-Fi 6, Bluetooth 5.1, NFC\n- **Ports**: USB Type-C, 3.5mm headphone jack\n- **Dimensions**: 160.8 x 78.1 x 7.4 mm\n- **Weight**: 190g\n- **Additional Features**: In-display fingerprint sensor, face recognition, IP68 water and dust resistance")
    # tags = models.ForeignKey(Tags, related_name='products', on_delete=models.SET_NULL, null=True)
    product_status = models.CharField(choices=STATUS, max_length=10, default="in_review")
    status = models.BooleanField(default=True)
    
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    digital = models.BooleanField(default=False)
    
    sku = ShortUUIDField(unique=True,length=4,max_length=10, prefix='sku', alphabet= '1234567890')  
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Products'
        ordering = ['-created_at']
        
    def product_image(self):
        return mark_safe(f'<img src="{self.image.url}" width="50" height="50"/>')
    
    def formatted_price(self):
        return f"${self.price}"
    
    def __str__(self):
        return self.title
    
    def get_percentage(self):
        new_price = ((self.old_price - self.price) / self.old_price) * 100
        return new_price
    
'''
######################## Product Images ########################
'''   
class ProductImages(models.Model):
    images = models.ImageField(upload_to='product-image', default='productr.jp')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Product Images'        
  
'''
######################## End of Categories, Vendor, Tags, Product, Product Images ########################
'''

'''
######################## Cart, Order, and Items Section ########################
'''

'''
######################## Cart Orders ########################
'''    

class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price= models.DecimalField(max_digits=10, decimal_places=2, default="$1.99")
    paid_status = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(choices=STATUS_CHOICE, max_length=30, default="processing")
    
    class Meta:
        verbose_name_plural = 'Cart Orders'
        
    def formatted_price(self):
        return f"${self.price}"
        
'''
######################## Cart Order Items ########################
'''   
class CartOrderItems(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    invoice_no = models.CharField(max_length=200)
    product_status = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    price= models.DecimalField(max_digits=10, decimal_places=2, default="$1.99")
    total= models.DecimalField(max_digits=10, decimal_places=2, default="$1.99")
    
    class Meta:
        verbose_name_plural = 'Cart Order Items'     
        
    def subtotal(self):
        return self.quantity * self.price
    
    def formatted_price(self):
        return f"${self.price}"
    
    def formatted_total(self):
        return f"${self.total}"
        
    def display_summary(self):
        return f"{self.item} - Quantity: {self.quantity}, Price: {self.formatted_price()}, Total: {self.formatted_total()}"
    
'''
######################## End of Cart, Order, and Address Section ########################
'''  

'''
######################## Product Review, wishlists, and Address Section ########################
'''
    
'''
######################## Product Review ########################
'''    
class ProductReview(models.Model):
   user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
   product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
   review = models.TextField()
   rating = models.IntegerField(choices=RATING, default=None)
   created_at = models.DateTimeField(auto_now_add=True)
   
   class Meta:
        verbose_name_plural = 'Product Reviews'
       
   def __str__(self):
        return self.product.title
    
   def get_rating(self):
       return self.rating

'''
######################## Wishlists ########################
'''   
class wishlist(models.Model):
   user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
   product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
   created_at = models.DateTimeField(auto_now_add=True)
   
   class Meta:
        verbose_name_plural = 'Wishlists'
       
   def __str__(self):
        return self.product.title
    
'''
######################## Address ########################
'''   
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=100, null=True)
    status = models.BooleanField(default=False)
    
    
    class Meta:
        verbose_name_plural = 'Addresses'
        
'''
######################## End of Product Review, wishlists, and Address Section ########################
'''  
       
    
    
    
    
   