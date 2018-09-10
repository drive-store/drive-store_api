from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

import pymongo
from pymongo import MongoClient

import io, json

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def getProducts(requests):
    json_return = {}
    return JsonResponse(json_return, safe=False, json_dumps_params={'ensure_ascii':False})

def getProductByName(requests, product_name):
    json_return = {}
    return JsonResponse(json_return, safe=False, json_dumps_params={'ensure_ascii':False})

def getProductPrices(request, product_names):
    json_return = {}
    return JsonResponse(json_return, safe=False, json_dumps_params={'ensure_ascii':False})

def getProductBestPrice(requests, product_name):
    json_return = {}
    return JsonResponse(json_return, safe=False, json_dumps_params={'ensure_ascii':False})

def getProductPriceHistory(requests, product_name):
    json_return = {}
    return JsonResponse(json_return, safe=False, json_dumps_params={'ensure_ascii':False})

def getProductCompanies(requests, product_name):
    json_return = {}
    return JsonResponse(json_return, safe=False, json_dumps_params={'ensure_ascii':False})

def getProductLocations(requests, product_name):
    json_return = {}
    return JsonResponse(json_return, safe=False, json_dumps_params={'ensure_ascii':False})
