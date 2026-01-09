from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:slug>/', views.CategoryView.as_view()  , name='category'),
    path('product/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('catalog/<slug:slug>/', views.CatalogView.as_view(), name='catalog'),
    path('catalog/',views.CatalogView.as_view(), name='catalog_all'),  
    
]
