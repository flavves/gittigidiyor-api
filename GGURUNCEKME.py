# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 15:46:46 2022

@author: okmen
"""

"""

GG ÜRÜN ÇEKME


"""



import requests
from zeep import Client
from zeep.transports import Transport
from zeep import xsd
from zeep import helpers
import xmltodict
import json
from requests.auth import HTTPBasicAuth
import time
import hashlib
import xmltodict
session = requests.Session()


### Auth Role Name ve Password
session.auth = HTTPBasicAuth("id", "pass")

with open("api.txt","r") as dosya:
    apibilgiler=dosya.readlines()
    
    
    
api_key=apibilgiler[4].split(":")[1][:-1]
secret_key=apibilgiler[5].split(":")[1][:-1]
Developer_Id=apibilgiler[0].split(":")[1][:-1]
Role_Name=apibilgiler[1].split(":")[1][:-1]
Role_Password=apibilgiler[2].split(":")[1][:-1]
Uygulama_Api_Key=apibilgiler[3].split(":")[1][:-1]


timeStamp = round(time.time() * 1000)

hashStr = api_key + secret_key + str(timeStamp)
sign = hashlib.md5(hashStr.encode()).hexdigest()


# ürün çekmek için 
client = Client('https://dev.gittigidiyor.com:8443/listingapi/ws/IndividualProductService?wsdl',transport=Transport(session=session))
veri=client.service.getProducts(api_key,sign,timeStamp,0,100,"A",True,"tr")
_json = helpers.serialize_object(veri, dict)
ajson_cikti=_json
item_id_kullanabilirsin=ajson_cikti["products"]["product"][0]["itemId"]
item_adi_kullanabilirsin=ajson_cikti["products"]["product"][0]["product"]["title"]
item_gg_deki_nosu=ajson_cikti["products"]["product"][0]["productId"]
