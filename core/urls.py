from django.urls import path

from .import views

app_name = "core"

urlpatterns = [
    # homepage url
    path('', views.index, name="index"),
    
    # products urls
    path('products/', views.product_list_view, name='product-list'),
    path('products/<str:pid>/', views.product_detail_view, name='product-detail'),
    
    # category urls
    path('categories/', views.category_list_view, name='category-list'),
    path('categories/<str:title>/', views.category_product_list_view, name='category-product-list'),
    
    # Vendors urls
    path('vendors/', views.vendor_list_view, name='vendor-list'),
    path('vendors/<str:vid>/', views.vendor_detail_view, name='vendor-detail'),
    
    # Tags
    path('products/tags/<slug:tag_slug>/', views.tag_list, name='tags'),
    
    # Add review
    path('ajax_add_review/<str:pid>/', views.ajax_add_review, name='ajax_add_review'),
    
    # Search
    
    path("search/", views.search_view, name="search"),
    
    path('filter-products/', views.filter_product_view, name='filter-products'),
]
