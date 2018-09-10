from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.getCompanies, name='getCompanies'),
    path('<company_name>', views.getCompanyProducts, name='getCompanyProducts'),
]
