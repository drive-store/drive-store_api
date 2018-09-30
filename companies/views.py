from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

import pymongo
from pymongo import MongoClient

from datetime import *
import io, json

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# http://localhost:8000/companies
def getCompanies(requests):
    client = MongoClient("ds141872.mlab.com", 41872)
    db = client['auchan-products']
    db.authenticate("scrapy59", "scrapy59")
    collection = db['products']
    cur_companies = collection.find({}, {"_id": 0, "Company": 1}).distinct("Company")
    json_data = cur_companies
    return JsonResponse(json_data, safe=False, json_dumps_params={'ensure_ascii':False, 'indent': 2})

# http://localhost:8000/companies/Auchan
def getCompanyByName(requests, company_name):
    json_return = {
        "Company": company_name,
        "actions": ["locations", "products"]
    }
    return JsonResponse(json_return, safe=False,json_dumps_params={'ensure_ascii':False, 'indent': 2})

# http://localhost:8000/companies/Auchan/products
def getCompanyProducts(requests, company_name):
    json_return = []
    client = MongoClient("ds141872.mlab.com", 41872)
    db = client['auchan-products']
    db.authenticate("scrapy59", "scrapy59")
    collection = db['products']
    cur_products = collection.aggregate([
        # Filter on 14 days
        {
            "$match": {
                "Date": { "$gt": datetime.now()-timedelta(days = 14) }
            }
        },
        # Sort on most recent first
        {
            "$sort": {
                "Date": pymongo.DESCENDING
            }
        },
        # Group by Product
        {
            "$group": {
                "_id": {
                    "Product": "$Product",
                    "Location": "$Location"
                },
                "Date": { "$first": "$Date" }
            }
        }
    ])
    for d in cur_products:
        d["_id"]["Date"] = d["Date"]
        json_return.append(d["_id"])
    return JsonResponse(json_return, safe=False,json_dumps_params={'ensure_ascii':False, 'indent': 2})

# http://localhost:8000/companies/Auchan/products/Jardin%20Bio%20pur%20jus%20de%20citron%20vert%2025cl
def getCompanyProductByName(requests, company_name, product_name):
    json_return = []
    client = MongoClient("ds141872.mlab.com", 41872)
    db = client['auchan-products']
    db.authenticate("scrapy59", "scrapy59")
    collection = db['products']
    cur_products = collection.aggregate([
        # Filter on 14 days
        {
            "$match": {
                "Date": { "$gt": datetime.now()-timedelta(days = 14) },
                "Company": company_name,
                "Product": product_name
            }
        },
        # Sort on most recent first
        {
            "$sort": {
                "Date": pymongo.DESCENDING
            }
        },
        # Filter on Fields 
        {
            "$project": {
                "_id": 0,
                "Date": 1,
                "Company": 1,
                "Location": 1,
                "Product": 1,
                "Price": 1,
                "Priceper": 1,
            }
        },
        # Group by Product
        {
            "$group": {
                "_id": {
                    "Product": "$Product",
                    "Location": "$Location",
                    "Price": "$Price",
                    "Priceper": "$Priceper",
                },
                "Date": { "$first": "$Date" }
            }
        }
    ])
    for d in cur_products:
        print(d)
        d["_id"]["Date"] = d["Date"]
        json_return.append(d["_id"])
    return JsonResponse(json_return, safe=False,json_dumps_params={'ensure_ascii':False, 'indent': 2})

# http://localhost:8000/companies/Auchan/products/Jardin%20Bio%20pur%20jus%20de%20citron%20vert%2025cl/best-price
def getCompanyProductBestPrice(requests, company_name, product_name):
    json_return = []
    client = MongoClient("ds141872.mlab.com", 41872)
    db = client['auchan-products']
    db.authenticate("scrapy59", "scrapy59")
    collection = db['products']
    cur_products = collection.find({"Company": company_name, "Product": product_name}, {"_id": 0, "Company": 1, "Product": 1, "Location": 1, "Price": 1, "Priceper": 1}).sort([["Price", pymongo.ASCENDING], ["Date", pymongo.DESCENDING]]).limit(1)
    for d in cur_products:
        json_return = d
    return JsonResponse(json_return, safe=False,json_dumps_params={'ensure_ascii':False, 'indent': 2})

# http://localhost:8000/companies/Auchan/products/Jardin%20Bio%20pur%20jus%20de%20citron%20vert%2025cl/locations
def getCompanyProductLocations(requests, company_name, product_name):
    json_return = []
    client = MongoClient("ds141872.mlab.com", 41872)
    db = client['auchan-products']
    db.authenticate("scrapy59", "scrapy59")
    collection = db['products']
    print(product_name)
    cur_products = collection.find({"Company": company_name, "Product": product_name}, {"_id": 0, "Location": 1}).distinct("Location")
    for d in cur_products:
        json_return.append(d)
    return JsonResponse(json_return, safe=False,json_dumps_params={'ensure_ascii':False, 'indent': 2})

# http://localhost:8000/companies/Auchan/products/Jardin%20Bio%20pur%20jus%20de%20citron%20vert%2025cl/locations/Englos
def getCompanyProductLocationByName(requests, company_name, product_name, location_name):
    json_return = []
    client = MongoClient("ds141872.mlab.com", 41872)
    db = client['auchan-products']
    db.authenticate("scrapy59", "scrapy59")
    collection = db['products']
    print(product_name)
    cur_products = collection.find({"Company": company_name, "Product": product_name, "Location": location_name}, {"_id": 0, "Date": 1, "Product": 1, "Location": 1, "Price": 1, "Priceper": 1}).sort("Date", pymongo.ASCENDING).limit(1)
    for d in cur_products:
        json_return = d
    return JsonResponse(json_return, safe=False,json_dumps_params={'ensure_ascii':False, 'indent': 2})

# http://localhost:8000/companies/Auchan/products/Jardin%20Bio%20pur%20jus%20de%20citron%20vert%2025cl/locations/Englos/price-history
def getCompanyProductLocationPriceHistory(requests, company_name, product_name, location_name):
    json_return = []
    client = MongoClient("ds141872.mlab.com", 41872)
    db = client['auchan-products']
    db.authenticate("scrapy59", "scrapy59")
    collection = db['products']
    print(product_name)
    cur_products = collection.find({"Company": company_name, "Product": product_name, "Location": location_name}, {"_id": 0, "Date": 1, "Product": 1, "Location": 1, "Price": 1, "Priceper": 1}).sort("Date", pymongo.DESCENDING)
    for d in cur_products:
        json_return.append(d)
    return JsonResponse(json_return, safe=False,json_dumps_params={'ensure_ascii':False, 'indent': 2})

# http://localhost:8000/companies/Auchan/locations
def getCompanyLocations(requests, company_name):
    json_return = []
    client = MongoClient("ds141872.mlab.com", 41872)
    db = client['auchan-products']
    db.authenticate("scrapy59", "scrapy59")
    collection = db['products']
    cur_products = collection.find({"Company": company_name}, {"_id": 0, "Location": 1}).distinct("Location")
    for d in cur_products:
        json_return.append(d)
    return JsonResponse(json_return, safe=False,json_dumps_params={'ensure_ascii':False, 'indent': 2})

# http://localhost:8000/companies/Auchan/locations/Englos
def getCompanyLocationByName(requests, company_name, location_name):
    json_return = {
        "Company": company_name,
        "Location": location_name
    }
    return JsonResponse(json_return, safe=False,json_dumps_params={'ensure_ascii':False, 'indent': 2})

# http://localhost:8000/companies/Auchan/locations/Englos/products
def getCompanyLocationProducts(requests, company_name, location_name):
    json_return = []
    client = MongoClient("ds141872.mlab.com", 41872)
    db = client['auchan-products']
    db.authenticate("scrapy59", "scrapy59")
    collection = db['products']
    #cur_products = collection.find({"Company": company_name, "Location": location_name}, {"_id": 0})
    cur_products = collection.aggregate([
        # Filter on 14 days
        {
            "$match": {
                "Date": { "$gt": datetime.now()-timedelta(days = 14) },
                "Location": location_name
            }
        },
        # Sort on most recent first
        {
            "$sort": {
                "Date": pymongo.DESCENDING
            }
        },
        # Group by Product
        {
            "$group": {
                "_id": {
                    "Product": "$Product",
                    "Location": "$Location"
                },
                "Date": { "$first": "$Date" }
            }
        }
    ])
    for d in cur_products:
        d["_id"]["Date"] = d["Date"]
        json_return.append(d["_id"])
    return JsonResponse(json_return, safe=False,json_dumps_params={'ensure_ascii':False, 'indent': 2})

# http://localhost:8000/companies/Auchan/locations/Englos/products/Jardin%20Bio%20pur%20jus%20de%20citron%20vert%2025cl
def getCompanyLocationProductByName(requests, company_name, location_name, product_name):
    json_return = []
    client = MongoClient("ds141872.mlab.com", 41872)
    db = client['auchan-products']
    db.authenticate("scrapy59", "scrapy59")
    collection = db['products']
    #cur_products = collection.find({"Company": company_name, "Location": location_name, "Product": product_name}, {"_id": 0}).sort("Date", pymongo.ASCENDING).limit(1)
    cur_products = collection.find({"Company": company_name, "Product": product_name, "Location": location_name}, {"_id": 0, "Date": 1, "Product": 1, "Location": 1, "Price": 1, "Priceper": 1}).sort("Date", pymongo.ASCENDING).limit(1)
    for d in cur_products:
        json_return = d
    return JsonResponse(json_return, safe=False,json_dumps_params={'ensure_ascii':False, 'indent': 2})

# http://localhost:8000/companies/Auchan/locations/Englos/products/Jardin%20Bio%20pur%20jus%20de%20citron%20vert%2025cl/price-history
def getCompanyLocationPriceHistory(requests, company_name, location_name, product_name):
    json_return = []
    client = MongoClient("ds141872.mlab.com", 41872)
    db = client['auchan-products']
    db.authenticate("scrapy59", "scrapy59")
    collection = db['products']
    print(product_name)
    #cur_products = collection.find({"Company": company_name, "Product": product_name, "Location": location_name}, {"_id": 0, "Date": 1, "Price": 1, "Priceper": 1}).sort("Date", pymongo.DESCENDING)
    cur_products = collection.find({"Company": company_name, "Product": product_name, "Location": location_name}, {"_id": 0, "Date": 1, "Product": 1, "Location": 1, "Price": 1, "Priceper": 1}).sort("Date", pymongo.DESCENDING)
    for d in cur_products:
        json_return.append(d)
    return JsonResponse(json_return, safe=False,json_dumps_params={'ensure_ascii':False, 'indent': 2})
