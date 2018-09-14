from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.getCompanies, name='getCompanies'),
    path('<company_name>', views.getCompanyByName, name='getCompanyByName'),
    path('<company_name>/products', views.getCompanyProducts, name='getCompanyProducts'),
    path('<company_name>/products/<product_name>', views.getCompanyProductByName, name='getCompanyProductByName'),
    path('<company_name>/products/<product_name>/best-price', views.getCompanyProductBestPrice, name='getCompanyProductBestPrice'),
    path('<company_name>/products/<product_name>/locations', views.getCompanyProductLocations, name='getCompanyProductLocations'),
    path('<company_name>/products/<product_name>/locations/<location_name>', views.getCompanyProductLocationByName, name='getCompanyProductLocationByName'),
    path('<company_name>/products/<product_name>/locations/<location_name>/price-history', views.getCompanyProductLocationPriceHistory, name='getCompanyProductLocationPriceHistory'),
    path('<company_name>/locations', views.getCompanyLocations, name='getCompanyLocations'),
    path('<company_name>/locations/<location_name>', views.getCompanyLocationByName, name='getCompanyLocationByName'),
    path('<company_name>/locations/<location_name>/products', views.getCompanyLocationProducts, name='getCompanyLocationProducts'),
    path('<company_name>/locations/<location_name>/products/<product_name>', views.getCompanyLocationProductByName, name='getCompanyLocationProductByName'),
    path('<company_name>/locations/<location_name>/products/<product_name>/price-history', views.getCompanyLocationPriceHistory, name='getCompanyLocationPriceHistory'),
]
