from django.urls import path

from . import views

urlpatterns = [
    path('', views.getProducts, name='getProducts'),
    path('<product_name>', views.getProductByName, name='getProductByName'),
    path('<product_name>/prices', views.getProductPrices, name='getProductPrices'),
    path('<product_name>/best-price', views.getProductBestPrice, name='getProductBestPrice'),
    path('<product_name>/price-history', views.getProductPriceHistory, name='getProductPriceHistory'),
    path('<product_name>/companies', views.getProductCompanies, name='getProductCompanies'),
    path('<product_name>/locations', views.getProductLocations, name='getProductLocations'),
]
