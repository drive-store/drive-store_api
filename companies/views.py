from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

import pymongo
from pymongo import MongoClient

import io, json

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def getCompanies(requests):
    client = MongoClient("localhost", 27017)
    db = client['auchan-products']
    db.authenticate("scrapy59", "scrapy59")
    collection = db['products']
    cur_companies = collection.find({}, {"_id": 0, "Company": 1}).distinct("Company")
    json_data = cur_companies
    return JsonResponse(json_data, safe=False, json_dumps_params={'ensure_ascii':False})

def getCompanyByName(requests, company_name):
    json_return = {}
    return JsonResponse(json_return, safe=False,json_dumps_params={'ensure_ascii':False})

def getCompanyProductDetails(request, company_name, product_name):
    json_return = {}
    return JsonResponse(json_return, safe=False,json_dumps_params={'ensure_ascii':False})

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

def getCompanyProductPrices(requests, company_name, product_name):
    json_return = []
    client = MongoClient("localhost", 27017)
    db = client['auchan-products']
    db.authenticate("scrapy59", "scrapy59")
    collection = db['products']
    print(product_name)
    cur_products = collection.find({"Company": company_name, "Product": product_name}, {"_id": 0, "Location": 1, "Price": 1})
    for d in cur_products:
        json_return.append(d)
    return JsonResponse(json_return, safe=False,json_dumps_params={'ensure_ascii':False})

def getCompanyProductBestPrice(requests, company_name, product_name):
    json_return = []
    client = MongoClient("localhost", 27017)
    db = client['auchan-products']
    db.authenticate("scrapy59", "scrapy59")
    collection = db['products']
    print(product_name)
    cur_products = collection.find({"Company": company_name, "Product": product_name}, {"_id": 0, "Location": 1, "Price": 1}).sort([("Price", 1)]).limit(1)
    print(cur_products)
    for d in cur_products:
        json_return.append(d)
    return JsonResponse(json_return, safe=False,json_dumps_params={'ensure_ascii':False})

def getCompanyProductHistory(requests, company_name, product_name):
    json_return = {}
    return JsonResponse(json_return, safe=False,json_dumps_params={'ensure_ascii':False})

def getCompanyLocations(requests, company_name):
    json_return = {}
    return JsonResponse(json_return, safe=False,json_dumps_params={'ensure_ascii':False})

def getCompanyLocationByName(requests, company_name):
    json_return = {}
    return JsonResponse(json_return, safe=False,json_dumps_params={'ensure_ascii':False})

def getCompanyLocationProducts(requests, company_name):
    json_return = {}
    return JsonResponse(json_return, safe=False,json_dumps_params={'ensure_ascii':False})

def getCompanyLocationProductByName(requests, company_name, product_name):
    json_return = {}
    return JsonResponse(json_return, safe=False,json_dumps_params={'ensure_ascii':False})

def getCompanyLocationProductPrices(requests, company_name, product_name):
    json_return = {}
    return JsonResponse(json_return, safe=False,json_dumps_params={'ensure_ascii':False})

def getCompanyLocationBestPrice(requests, company_name, product_name):
    json_return = {}
    return JsonResponse(json_return, safe=False,json_dumps_params={'ensure_ascii':False})

def getCompanyLocationPriceHistory(requests, company_name, product_name):
    json_return = {}
    return JsonResponse(json_return, safe=False,json_dumps_params={'ensure_ascii':False})
