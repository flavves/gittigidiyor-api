# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 16:17:04 2022

@author: okmen
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
import random
import datetime
import xlwings as xw
import pandas as pd
import time


#api bilgilerini çektim

global df1,df1uzunluk

def trendyolurunlerinicekme():
    print("ürünler çekiliyor")
    global df1
    excel_file = pd.ExcelFile('Ürünleriniz_28.05.2022-21.26.xlsx')
    df1 = excel_file.parse('Ürünler')
    
    

def skuolmayanlariduzelt():
    global df1,df1uzunluk
    isimler=df1.columns
    isimler=list(isimler)
    
    df1uzunluk=len(df1)
    sayac=0
    for sira in range(0,df1uzunluk): 
        sayac=sayac+1
        
        if pd.isna(df1["Tedarikçi Stok Kodu"][sira])==True:
            
            df1["Tedarikçi Stok Kodu"][sira]="Flavves"+str(random.randint(0,99999999))+str(datetime.datetime.now().minute)
            print(sayac)
        
        

trendyolurunlerinicekme()
print("trendyol veri çekme işlemi tamam")
skuolmayanlariduzelt()
print("sku olmayanları düzelttim")


















try:
    global df1,df1uzunluk,start_time
    
    # for baslabakalim in range(0,df1uzunluk):
    print("%s ürün işlenecek"%df1uzunluk)
    start_time=time.time()
    
    with open("butunrenkler.txt","r") as dosya:
                renklerinhepsi=dosya.readline()
    dosya.close()
    renklerinhepsi=renklerinhepsi.split(";")
    renklerinhepsi.pop(-1)
    
    with open("butunseriler.txt","r") as dosya:
        serilerinhepsi=dosya.readline()
    dosya.close()
    serilerinhepsi=serilerinhepsi.split(";")
    serilerinhepsi.pop(-1)
    
    
    
    with open("butunmarkalar2.txt","r") as dosya:
                butunmarkalar=dosya.readline()
    dosya.close()
    butunmarkalar=butunmarkalar.split(";")
    butunmarkalar.pop(-1)
    butunmarkalar.pop(0)
except:
    pass


#aPİİİİ


#api kısımları


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


















while 1:
    sira=0
    if sira >len(df1):
        break
    print("başladık")
     
    listeleme_suresi="360"
    urun_gonderim_yeri="34"
    kargo_sirketleri="aras,mng"
    kargoucreti_Listeleme="S"
    gonderitarih_listeleme="tomorrow"
    gonderiyapılanyerler_listeleme="country"
    
    trendyoldangelen_kategori=df1["Kategori İsmi"][sira]
    if trendyoldangelen_kategori == "Oto Paspasları":
        
        kategori="rg1af"
        #+str(random.randint(0,9999999999))
        stok=df1["Tedarikçi Stok Kodu"][sira]
        baslik=df1["Ürün Adı"][sira]
        aciklama=df1["Ürün Açıklaması"][sira]
        Gorsel_1=df1["Görsel 1"][sira]      
        Gorsel_2=df1["Görsel 2"][sira]
        Gorsel_3=df1["Görsel 3"][sira]
        Gorsel_4=df1["Görsel 4"][sira]
        Gorsel_5=df1["Görsel 5"][sira]
        Gorsel_6=df1["Görsel 6"][sira]
        Gorsel_7=df1["Görsel 7"][sira]
        Gorsel_8=df1["Görsel 8"][sira]
        
        
        if pd.isna(Gorsel_2) == True:
            Gorsel_2=Gorsel_1
            Gorsel_3=Gorsel_1
            Gorsel_4=Gorsel_1
            Gorsel_5=Gorsel_1
            Gorsel_6=Gorsel_1
            Gorsel_7=Gorsel_1
            Gorsel_8=Gorsel_1
        elif pd.isna(Gorsel_3) == True:
            Gorsel_3=Gorsel_1
            Gorsel_4=Gorsel_1
            Gorsel_5=Gorsel_1
            Gorsel_6=Gorsel_1
            Gorsel_7=Gorsel_1
            Gorsel_8=Gorsel_1
        elif pd.isna(Gorsel_4 ) == True:  
            Gorsel_4=Gorsel_1
            Gorsel_5=Gorsel_1
            Gorsel_6=Gorsel_1
            Gorsel_7=Gorsel_1
            Gorsel_8=Gorsel_1
        elif pd.isna(Gorsel_5 ) == True:   
            Gorsel_5=Gorsel_1
            Gorsel_6=Gorsel_1
            Gorsel_7=Gorsel_1
            Gorsel_8=Gorsel_1
        elif pd.isna(Gorsel_6 ) == True:   
            Gorsel_6=Gorsel_1
            Gorsel_7=Gorsel_1
            Gorsel_8=Gorsel_1
        elif pd.isna(Gorsel_7) == True:    
            Gorsel_7=Gorsel_1
            Gorsel_8=Gorsel_1
        elif pd.isna(Gorsel_8 ) == True:    
            Gorsel_8=Gorsel_1
        
        pd.isna(Gorsel_8)
        
        hemenal_fiyat=df1["Trendyol'da Satılacak Fiyat (KDV Dahil)"][sira]
        piyasa_satis_fiyat=df1["Piyasa Satış Fiyatı (KDV Dahil)"][sira]
        sure=listeleme_suresi
        urunadet=df1["Ürün Stok Adedi"][sira]
        sehirno=urun_gonderim_yeri
        kargoolculeri=""
        kargodesi=df1["Desi"][sira]
        kargosirketler=kargo_sirketleri
        kargoucreti=kargoucreti_Listeleme
        gonderitarih=gonderitarih_listeleme
        gonderiyapılanyerler=gonderiyapılanyerler_listeleme
        ureticiparcano=df1["Barkod"][sira]        
        
        #Tanımlar
        uyumlu_seri="Universal"
        uyumlu_marka="Universal"
        ana_marka="Diğer"
        uruntipi="Üniversal Paspas"
        renk="Siyah"
        durum="Sıfır"
        
        try:
            
            ##########################################
                    #renk
                    
                    
                    
                    ozellikicin_urunadi=df1["Ürün Adı"][sira].lower().split(" ")
                    
                    for kelime in ozellikicin_urunadi:
                        kelime=kelime.lower()
                        if kelime in renklerinhepsi:                    
                            
                            renk=kelime[0].upper()+kelime[1:]
                            break
                    
                    ######################################################################
                    uyumlu_marka_icin=df1["Ürün Adı"][sira]
                    uyumlu_marka_icin=uyumlu_marka_icin.lower()
                    
                    for denememarka in butunmarkalar:
                        if denememarka.lower()  in uyumlu_marka_icin :
                            uyumlu_marka=denememarka
                            
                    if uyumlu_marka=="Universal":
                            
                        ########################################################################
                        #uyumlu marka 2. aşama
                        uyumlu_marka_icin=df1["Ürün Adı"][sira]
                        uyumlu_marka_icin=uyumlu_marka_icin.lower().split(" ")
                        
                        
                        
                        for marka in butunmarkalar:
                            marka=marka.lower()
                            if marka in uyumlu_marka_icin:
                                uyumlu_marka=marka[0].upper()+marka[1:]
                                
                                #uyumlu marka buldu
                        
                    #####################################################################    
                    #uyumlu seri deneme
                    uyumlu_seri_icin=df1["Ürün Adı"][sira]
                    uyumlu_seri_icin=uyumlu_seri_icin.lower()
                    uyumlu_seri_icin=uyumlu_seri_icin.split(" ")
                    #◘devam et
                    #uyumlu_seri_icin="BMW 2 Serisi F45 Active Tourer 2014 ve Sonra Turuncu Halı Yeşil Desen Mavi Kenar PLUS Paspas"
                    for denemeseri in serilerinhepsi:
                        
                        for parcalayici in uyumlu_seri_icin:
                            seri_denemesi=denemeseri.lower()                     
                            if  seri_denemesi  ==  parcalayici:
                                uyumlu_seri=denemeseri
                                #print(denemeseri)
                                break
                        
                            
                    #Ürün tipi için
                    #sonra
                    if uyumlu_seri=="Universal" or uyumlu_marka=="Universal":
                        uyumlu_marka="Universal"
                        uyumlu_seri="Universal"
                    urun_ozelligi_girme="Uyumlu Seri::"+uyumlu_seri+"|Uyumlu Marka::"+uyumlu_marka+"|Marka::"+ana_marka+"|Ürün Tipi::"+uruntipi+"|Renk::"+renk+"|Durum::Sıfır"
                    
                    
                    
                    parameters = {
    
                    "categoryCode" : kategori,
                    "storeCategoryId":"",
                    "title":baslik,
                    "subtitle":"",
                    "specs": {
                        "spec": [
                            {
                                
                                "name": "Durum",
                                "value": "Sıfır",
                                "type": "Combo",
                                "required": "false"
                                },
                            {
                                
                                "name": "Uyumlu Marka",
                                "value": uyumlu_marka,
                                "type": "Combo",
                                "required": "false"
                                },
                
                            {
                                "name": "Uyumlu Seri",
                                "value": uyumlu_seri,
                                "type": "Combo",
                                "required": "false"
                                },
                
                            {
                                "name": "Marka",
                                "value": ana_marka,
                                "type": "Combo",
                                "required": "false"
                                },
                            {
                                "name": "Ürün Tipi",
                                "value": uruntipi,
                                "type": "Combo",
                                "required": "false"
                                },
                            {
                                "name": "Renk",
                                "value": renk,
                                "type": "Combo",
                                "required": "false"
                                },
                            
                            ]
                        },
                
                
                
                      "photos": {
                        "photo": [
                          {
                            "photoId": "0",
                            "url": Gorsel_1,
                            "base64": ""
                            
                          },
                          {
                            "photoId": "1",
                            "url": Gorsel_2,
                            "base64": ""
                            
                          },
                          {
                            "photoId": "2",
                            "url": Gorsel_3,
                            "base64": ""
                            
                          },
                          {
                            "photoId": "3",
                            "url": Gorsel_4,
                            "base64": ""
                            
                          },
                          {
                            "photoId": "4",
                            "url": Gorsel_5,
                            "base64": ""
                            
                          },
                          {
                            "photoId": "5",
                            "url": Gorsel_6,
                            "base64": ""
                            
                          },
                          {
                            "photoId": "6",
                            "url": Gorsel_7,
                            "base64": ""
                            
                          },
                                               
                          {
                                "photoId": "7",
                                "url": Gorsel_8,
                                "base64": ""
                                
                              },
                
                        ]
                      },
                    "pageTemplate" : "1",
                    "description" : aciklama,
                    "startDate" : "",
                    "newCatalogId" : "0",
                    "catalogDetail" : "",
                    "catalogFilter" : "",
                    "format" : "S",
                    "startPrice" : piyasa_satis_fiyat,
                    "buyNowPrice" : "240",
                    "netEarning" : "",
                    "listingDays" : listeleme_suresi,
                    "productCount" : urunadet,
                    "cargoDetail" : {
                        "city" : "34",
                        "shippingPayment" : "S",
                        "shippingWhere" : "country",
                        "cargoCompanyDetails" : {
                            "cargoCompanyDetail" : {
                                "name" : "aras",
                                
                                }
                            
                            },
                        "shippingTime" : {
                            "days" : "2-3days",
                            "beforeTime" : "10.00"
                            
                
                
                            },
                        },
                    "affiliateOption" : "false",
                    "boldOption" : "false",
                    "catalogOption" : "false",
                    "vitrineOption" : "false",
                    "globalTradeItemNo" : "12345678",
                    "manufacturerPartNo" : ureticiparcano,
                    
                    }   
        
                    
                    sira=sira+1
                    
                    try:
                            
                        timeStamp = round(time.time() * 1000)
                        
                        hashStr = api_key + secret_key + str(timeStamp)
                        sign = hashlib.md5(hashStr.encode()).hexdigest()
                        # ürün yüklemek ve yayınlamak için
                        timeStamp = round(time.time() * 1000)
                        hashStr = api_key + secret_key + str(timeStamp)
                        sign = hashlib.md5(hashStr.encode()).hexdigest()
                        
                        
                        
                        
                        
                        client = Client('https://dev.gittigidiyor.com:8443/listingapi/ws/IndividualProductService?wsdl',transport=Transport(session=session))
                        sonuc_sistem=client.service.insertAndActivateProduct(api_key,sign,timeStamp,stok,parameters,False,False,"tr")
                        sonuc_sistem = helpers.serialize_object(sonuc_sistem, dict)
                        try:
                            if sonuc_sistem["error"]["errorId"]=="303":
                                if urunadet=="0":
                                    client.service.updateStock(api_key,sign,timeStamp,805553920,stok,int(urunadet),False,"tr")
                                    
                            
                        except:
                            pass
                    except Exception as e:
                         print(e)

            
        except Exception as e:
                    print("hata mesajı"+str(e))
                    print("nerede durdu"+str(sira-1))
                    aror_time=time.time()-start_time
                    print("hata aldığı süre: "+(time.strftime('%H:%M:%S', time.gmtime(aror_time))))
                    break 
    
















