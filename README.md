# Drive Store API

**Summary**
1. [Global View](#global-view)
   1. [Global application](#global-application)
   1. [Workflow](#workflow)
1. [Zoom on the API](#zoom-on-the-api)
   1. [General](#general)
   1. [Configuration](#configuration)
1. [Dependencies](#dependencies)
1. [Run the app](#run-the-app)
   1. [Quickstart](#quickstart)
1. [Production eligibility](#production-eligibility)
   1. [Application](#application)
   1. [Reverse Proxy](#reverse-proxy)
   1. [Resiliency](#resiliency)


## Global View

### Global application

This application is part of a fullchain applications which have the goal to provide the best product prices from all drive stores for a registered cart.

### Workflow

To provide a structured data requestable application a chain of steps is required. This chain catch the raw data and store it in a structured way. This data is thus queryable and optimized for processing.

You can find a quick sight of the Data Journey below.

**Global application schema**
```
                                                             Customer  
                                                                 |     
                                                                 |     
+-------------+      +--------------+      +---------+      +---------+
|   Scraper   |------|   Database   |------|   Api   |------|   Gui   |
+------+------+      +--------------+      +---------+      +---------+
       |                                                               
       |                                                               
  Drive Stores                                                         
 +----+                                                                 
 |   +----+                                                             
 +---|   +----+                                                         
     +---|    |                                                         
         +----+                                                         
```

Quick description of each step :
* Scraper : Catches product prices,
* Database : Stores product prices,
* Api : Provides REST Api to process/read Product Prices,
* Gui : Offers a interface to interact with the Api.


## Zoom on the API

### General

The aim of the api is to provides a endpoint in order to retrieve informations about product prices in time (last entry or history) and to call processing functions making correlation between products and Drive Stores.

The API application only requests the database to process on product prices from different Drive Stores.

The API is RESTful and follow the norm.

### Configuration

All the application configuration is stored in the `conf/` directory.

## Dependencies

Code run from Visual Studio Code 2017 with Python and C++ environements configured. Python version selected is python-3.6 because of dependencies with scrapy package (not compatible with python-3.7 yet).

Required python libs :
* `pywin32` (Visual Studio)
* `pymongo`


## Run the app

### Quickstart

```shell
django-admin runserver 8080
```

## Production eligibility

The application don't have to be run as it is on production server. You need to tune some stuff to make it eligible to Production environment.

### Application

You need to tune the app to reduce the loglevel.

### Reverse Proxy

You need to run the app behind a Reverse Proxy to protect it from Hack and DDoS. You can choose between Apache and NGinx to shield your app. Mind to tune your Middleware to deactivate all banners and version displaying.

### Resiliency

To allow a large amount of connection of the application you need to dispatch requests on multiple servers. You need to pop up several servers with the app and balance all requests on them.

The RESTful property of the app allow it to be deployed on servers without configuring anything (or almost).
