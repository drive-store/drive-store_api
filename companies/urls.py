from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.getCompanies, name='getCompanies'),
    path('<company_name>', views.getCompanyByName, name='getCompanyByName'),
    path('<company_name>/products', views.getCompanyProducts, name='getCompanyProducts'),
    path('<company_name>/products/<product_name>', views.getCompanyProductByName, name='getCompanyProductByName'),
    path('<company_name>/products/<product_name>/locations', views.getCompanyProductLocations, name='getCompanyProductLocations'),
    path('<company_name>/products/<product_name>/prices', views.getCompanyProductPrices, name='getCompanyProductPrices'),
    path('<company_name>/products/<product_name>/best-price', views.getCompanyProductBestPrice, name='getCompanyProductBestPrice'),
    path('<company_name>/products/<product_name>/history', views.getCompanyProductHistory, name='getCompanyProductHistory'),
    path('<company_name>/locations', views.getCompanyLocations, name='getCompanyLocations'),
    path('<company_name>/locations/<location_name>', views.getCompanyLocationByName, name='getCompanyLocationByName'),
    path('<company_name>/locations/<location_name>/products', views.getCompanyLocationProducts, name='getCompanyLocationProducts'),
    path('<company_name>/locations/<location_name>/products/<product_name>', views.getCompanyLocationProductByName, name='getCompanyLocationProductByName'),
    path('<company_name>/locations/<location_name>/products/<product_name>/prices', views.getCompanyLocationProductPrices, name='getCompanyLocationProductPrices'),
    path('<company_name>/locations/<location_name>/products/<product_name>/best-price', views.getCompanyLocationBestPrice, name='getCompanyLocationBestPrice'),
    path('<company_name>/locations/<location_name>/products/<product_name>/price-history', views.getCompanyLocationPriceHistory, name='getCompanyLocationPriceHistory'),
]
