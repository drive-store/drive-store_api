from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

import pymongo
from pymongo import MongoClient

import io, json

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# http://localhost:8000/companies
def getCompanies(requests):
    client = MongoClient("localhost", 27017)
    db = client['auchan-products']
    db.authenticate("scrapy59", "scrapy59")
    collection = db['products']
    cur_companies = collection.find({}, {"_id": 0, "Company": 1}).distinct("Company")
    json_data = cur_companies
    return JsonResponse(json_data, safe=False, json_dumps_params={'ensure_ascii':False})

# http://localhost:8000/companies/Auchan
def getCompanyByName(requests, company_name):
    json_return = {}
    return JsonResponse(json_return, safe=False,json_dumps_params={'ensure_ascii':False})

# http://localhost:8000/companies/Auchan/products
def getCompanyProducts(requests, company_name):
    json_return = []
    client = MongoClient("localhost", 27017)
    db = client['auchan-products']
    db.authenticate("scrapy59", "scrapy59")
    collection = db['products']
    cur_products = collection.find({"Company": company_name}, {"_id": 0, "Location": 1, "Product": 1, "Price": 1})
    for d in cur_products:
        json_return.append(d)
    return JsonResponse(json_return, safe=False,json_dumps_params={'ensure_ascii':False})

# http://localhost:8000/companies/Auchan/products/Jardin%20Bio%20pur%20jus%20de%20citron%20vert%2025cl
def getCompanyProductByName(requests, company_name, product_name):
    json_return = []
    client = MongoClient("localhost", 27017)
    db = client['auchan-products']
    db.authenticate("scrapy59", "scrapy59")
    collection = db['products']
    print(product_name)
    cur_products = collection.find({"Company": company_name, "Product": product_name}, {"_id": 0})
    for d in cur_products:
        json_return.append(d)
    return JsonResponse(json_return, safe=False,json_dumps_params={'ensure_ascii':False})

# http://localhost:8000/companies/Auchan/products/Jardin%20Bio%20pur%20jus%20de%20citron%20vert%2025cl/prices
def getCompanyProductPrices(requests, company_name, product_name):
    json_return = []
    client = MongoClient("localhost", 27017)
    db = client['auchan-products']
    db.authenticate("scrapy59", "scrapy59")
    collection = db['products']
    print(product_name)
    cur_products = collection.find({"Company": company_name, "Product": product_name}, {"_id": 0, "Location": 1, "Price": 1}).sort("Date", 1)
    for d in cur_products:
        json_return.append(d)
    return JsonResponse(json_return, safe=False,json_dumps_params={'ensure_ascii':False})

# http://localhost:8000/companies/Auchan/products/Jardin%20Bio%20pur%20jus%20de%20citron%20vert%2025cl/locations/best-price
def getCompanyProductBestPrice(requests, company_name, product_name):
    json_return = []
    client = MongoClient("localhost", 27017)
    db = client['auchan-products']
    db.authenticate("scrapy59", "scrapy59")
    collection = db['products']
    print(product_name)
    cur_products = collection.find({"Company": company_name, "Product": product_name}, {"_id": 0, "Location": 1, "Price": 1}).sort("Date", 1).limit(1)
    for d in cur_products:
        json_return.append(d)
    return JsonResponse(json_return, safe=False,json_dumps_params={'ensure_ascii':False})

# http://localhost:8000/companies/Auchan/products/Jardin%20Bio%20pur%20jus%20de%20citron%20vert%2025cl/locations
def getCompanyProductLocations(requests, company_name, product_name):
    json_return = []
    client = MongoClient("localhost", 27017)
    db = client['auchan-products']
    db.authenticate("scrapy59", "scrapy59")
    collection = db['products']
    print(product_name)
    cur_products = collection.find({"Company": company_name, "Product": product_name}, {"_id": 0, "Location": 1}).distinct("Location")
    for d in cur_products:
        json_return.append(d)
    return JsonResponse(json_return, safe=False,json_dumps_params={'ensure_ascii':False})

# http://localhost:8000/companies/Auchan/products/Jardin%20Bio%20pur%20jus%20de%20citron%20vert%2025cl/locations/Englos/price-history
def getCompanyProductLocationPriceHistory(requests, company_name, product_name, location_name):
    json_return = []
    client = MongoClient("localhost", 27017)
    db = client['auchan-products']
    db.authenticate("scrapy59", "scrapy59")
    collection = db['products']
    print(product_name)
    cur_products = collection.find({"Company": company_name, "Product": product_name, "Location": location_name}, {"_id": 0, "Date": 1, "Price": 1})
    for d in cur_products:
        json_return.append(d)
    return JsonResponse(json_return, safe=False,json_dumps_params={'ensure_ascii':False})

# http://localhost:8000/companies/Auchan/locations
def getCompanyLocations(requests, company_name):
    json_return = []
    client = MongoClient("localhost", 27017)
    db = client['auchan-products']
    db.authenticate("scrapy59", "scrapy59")
    collection = db['products']
    cur_products = collection.find({"Company": company_name}, {"_id": 0, "Location": 1}).distinct("Location")
    for d in cur_products:
        json_return.append(d)
    return JsonResponse(json_return, safe=False,json_dumps_params={'ensure_ascii':False})

# http://localhost:8000/companies/Auchan/locations/Englos
def getCompanyLocationByName(requests, company_name, location_name):
    json_return = []
    client = MongoClient("localhost", 27017)
    db = client['auchan-products']
    db.authenticate("scrapy59", "scrapy59")
    collection = db['products']
    cur_products = collection.find({"Company": company_name, "Location": location_name}, {"_id": 0, "Location": 1})
    for d in cur_products:
        json_return.append(d)
    return JsonResponse(json_return, safe=False,json_dumps_params={'ensure_ascii':False})

# http://localhost:8000/companies/Auchan/locations/Englos/products
def getCompanyLocationProducts(requests, company_name, location_name):
    json_return = []
    client = MongoClient("localhost", 27017)
    db = client['auchan-products']
    db.authenticate("scrapy59", "scrapy59")
    collection = db['products']
    cur_products = collection.find({"Company": company_name, "Location": location_name}, {"_id": 0})
    for d in cur_products:
        json_return.append(d)
    return JsonResponse(json_return, safe=False,json_dumps_params={'ensure_ascii':False})

# http://localhost:8000/companies/Auchan/locations/Englos/products/Jardin%20Bio%20pur%20jus%20de%20citron%20vert%2025cl
def getCompanyLocationProductByName(requests, company_name, location_name, product_name):
    json_return = []
    client = MongoClient("localhost", 27017)
    db = client['auchan-products']
    db.authenticate("scrapy59", "scrapy59")
    collection = db['products']
    cur_products = collection.find({"Company": company_name, "Location": location_name, "Product": product_name}, {"_id": 0}).sort("Date", 1).limit(1)
    for d in cur_products:
        json_return = d
    return JsonResponse(json_return, safe=False,json_dumps_params={'ensure_ascii':False})

# http://localhost:8000/companies/Auchan/locations/Englos/products/Jardin%20Bio%20pur%20jus%20de%20citron%20vert%2025cl/prices
def getCompanyLocationProductPrices(requests, company_name, location_name, product_name):
    json_return = []
    client = MongoClient("localhost", 27017)
    db = client['auchan-products']
    db.authenticate("scrapy59", "scrapy59")
    collection = db['products']
    cur_products = collection.find({"Company": company_name, "Location": location_name, "Product": product_name}, {"_id": 0, "Price": 1}).sort("Date", 1).limit(1)
    for d in cur_products:
        json_return = d
    return JsonResponse(json_return, safe=False,json_dumps_params={'ensure_ascii':False})

def getCompanyLocationPriceHistory(requests, company_name, location_name, product_name):
    json_return = []
    client = MongoClient("localhost", 27017)
    db = client['auchan-products']
    db.authenticate("scrapy59", "scrapy59")
    collection = db['products']
    print(product_name)
    cur_products = collection.find({"Company": company_name, "Product": product_name, "Location": location_name}, {"_id": 0, "Date": 1, "Price": 1})
    for d in cur_products:
        json_return.append(d)
    return JsonResponse(json_return, safe=False,json_dumps_params={'ensure_ascii':False})
