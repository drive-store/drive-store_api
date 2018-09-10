# coding: utf8
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

import pymongo
from pymongo import MongoClient

import io, json

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def getCompanies(requests):
    client = MongoClient("ds141872.mlab.com", 41872)
    db = client['auchan-products']
    db.authenticate("scrapy59", "scrapy59")
    collection = db['products']
    cur_companies = collection.find({}, {"_id": 0, "Company": 1}).distinct("Company")
    json_data = cur_companies
    return JsonResponse(json_data, safe=False, json_dumps_params={'ensure_ascii':False})
    

def getCompanyProducts(request, company_name):
    client = MongoClient("ds141872.mlab.com", 41872)
    db = client['auchan-products']
    db.authenticate("scrapy59", "scrapy59")
    collection = db['products']
    cur_products = collection.find({"Company": company_name}, {"_id": 0, "Location": 1, "Product": 1, "Price": 1})
    json_data = []
    for d in cur_products:
        json_data.append(d)

    return JsonResponse(json_data, safe=False,json_dumps_params={'ensure_ascii':False})
    #return HttpResponse(json.dumps(response), content_type="application/json; charset=utf-8") # Don't Work

def getCompanyProductDetails(request, company_name, product_name):
    return JsonResponse({})