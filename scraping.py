from lxml import html
import csv
import os
import requests
from time import sleep
from random import randint
import xlrd
import urllib3
import random
#from jsWriteFile import jsWriter
from openpyxl import Workbook
from PIL import Image  
import aggdraw
from bs4 import BeautifulSoup
import re
from lxml.html import fromstring
from itertools import cycle
import random
import time
import bottlenose
import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET


ACCESS_KEY = 'AKIAJTCMYV6TGSZQU5DA'
SECRET_KEY = '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'
AFFILIATE_TAG = 'glance09d-21'

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def parse(url, folder_name, j):
    
    if "amazon" in url :
        merchant_name = "amazon"
    elif "flipkart" in url :
        merchant_name = "flipkart"
    else :
        merchant_name = "others"

    try:
        if(merchant_name == "amazon"):
            result = url.find('/dp/')
            asin_id = url[result+4:result+14]
            print(str(j) + " " + merchant_name + " " + asin_id)

            amazon = bottlenose.Amazon(ACCESS_KEY, SECRET_KEY, AFFILIATE_TAG, MaxQPS=0.9,Parser=lambda text_response: BeautifulSoup(text_response,'xml'), Region='IN')
   
            response = amazon.ItemLookup(ItemId=asin_id, ResponseGroup='ItemAttributes, Offers, Images')

            if response.find('Error') is None:
                if response.find('Title') is not None:
                    RAW_NAME = response.Title.string
                else:
                    RAW_NAME = "Unavailable"
                if response.find('LowestNewPrice') is not None:
                    RAW_SALE_PRICE = response.LowestNewPrice.FormattedPrice.string
                    RAW_SALE_PRICE = RAW_SALE_PRICE[4:]
                else:
                    RAW_SALE_PRICE = "-1"
                if response.find('ListPrice') is not None:
                    RAW_ORIGINAL_PRICE = response.ListPrice.FormattedPrice.string
                    RAW_ORIGINAL_PRICE = RAW_ORIGINAL_PRICE[4:]                    
 
                else:
                    RAW_ORIGINAL_PRICE = "-1"
                if response.find('LargeImage') is not None:
                    img_url = response.LargeImage.URL.string
                else:
                    img_url = ''

                if not img_url == '':
                    img_data = requests.get(img_url).content
                    with open(folder_name +'/images/' + str(j) +'.jpeg', 'wb') as handler:
                        handler.write(img_data)

                    size = 300, 300
                    im = Image.new("RGB", (344,344), "white")
                    draw = aggdraw.Draw(im)

                    im1 = Image.open(folder_name +'/images/' + str(j) +'.jpeg')
                    im1.thumbnail(size, Image.ANTIALIAS)
                    im1.save(folder_name +'/images/' + str(j) +'resize.jpeg')

                    icon = Image.open(folder_name +'/images/' + str(j) +'resize.jpeg')
                    # get the correct size
                    x, y = icon.size
                    l, b = im.size

                    offset = ((l - x) // 2, (b - y) // 2)
                    im.paste(icon, offset)

                    del draw
                    
                    im.save(folder_name +'/images/' + str(j) +'.webp')
                    
                    os.remove(folder_name +'/images/' + str(j) +'.jpeg')
                    os.remove(folder_name +'/images/' + str(j) +'resize.jpeg')
        
                    IMG = ''
                else: 
                    IMG = 'Not Found'
            else:
                data = {
                'NAME': "Unavailable",
                'SALE_PRICE': "-1",
                'ORIGINAL_PRICE': "-1",
                'URL': "-1",
                'IMAGE' : "-1",
                "MERCHANT NAME" : "Unavailable"
                }
                return data
            data = {
                'NAME': RAW_NAME,
                'SALE_PRICE': RAW_SALE_PRICE,
                'ORIGINAL_PRICE': RAW_ORIGINAL_PRICE,
                'URL': url,
                'IMAGE' : IMG,
                'MERCHANT NAME' : merchant_name
            }
            return data
        elif(merchant_name == "flipkart") :
            result = url.find('&pid=')
            pid = url[result+5:result+21]
            print(str(j) + " " + merchant_name + " " + pid)
            apiurl = "https://affiliate-api.flipkart.net/affiliate/1.0/product.xml?id="+pid
            headers = {"Fk-Affiliate-Id":"glance", "Fk-Affiliate-Token":"497756fb19f64929aea7fa8233f8008b", "Content-Type": "application/xml"}
            res = requests.get(apiurl, headers=headers)

            if res.status_code == 200:
                root = ET.fromstring(res.content)
                response = ET.tostring(root).decode()

                RAW_NAME = root.find('./productBaseInfoV1/title').text


                if root.find('./productBaseInfoV1/flipkartSpecialPrice/amount') is not None:
                    RAW_SALE_PRICE = root.find('./productBaseInfoV1/flipkartSpecialPrice/amount').text

                else:
                    RAW_SALE_PRICE = "-1"
                if root.find('./productBaseInfoV1/maximumRetailPrice/amount') is not None:
                    RAW_ORIGINAL_PRICE = root.find('./productBaseInfoV1/maximumRetailPrice/amount').text

                else:
                    RAW_ORIGINAL_PRICE = "-1"
                if root.find('./productBaseInfoV1/imageUrls/entry[3]/value') is not None:
                    img_url = root.find('./productBaseInfoV1/imageUrls/entry[3]/value').text
                else:
                    img_url = ""

                if not img_url == '':
                    img_data = requests.get(img_url).content
                    with open(folder_name +'/images/' + str(j) +'.jpeg', 'wb') as handler:
                        handler.write(img_data)

                    size = 300, 300
                    im = Image.new("RGB", (344,344), "white")
                    draw = aggdraw.Draw(im)

                    im1 = Image.open(folder_name +'/images/' + str(j) +'.jpeg')
                    im1.thumbnail(size, Image.ANTIALIAS)
                    im1.save(folder_name +'/images/' + str(j) +'resize.jpeg')

                    icon = Image.open(folder_name +'/images/' + str(j) +'resize.jpeg')
                    # get the correct size
                    x, y = icon.size
                    l, b = im.size

                    offset = ((l - x) // 2, (b - y) // 2)
                    im.paste(icon, offset)

                    del draw
                    
                    im.save(folder_name +'/images/' + str(j) +'.webp')
                    
                    os.remove(folder_name +'/images/' + str(j) +'.jpeg')
                    os.remove(folder_name +'/images/' + str(j) +'resize.jpeg')
        
                    IMG = ''
                else: 
                    IMG = 'Not Found'
            else:
                data = {
                'NAME': "",
                'SALE_PRICE': "",
                'ORIGINAL_PRICE': "",
                'URL': "",
                'IMAGE' : "",
                'MERCHANT NAME' : ''
                }
                return data      

            data = {
                'NAME': RAW_NAME,
                'SALE_PRICE': RAW_SALE_PRICE,
                'ORIGINAL_PRICE': RAW_ORIGINAL_PRICE,
                'URL': url,
                'IMAGE' : IMG,
                'MERCHANT NAME' : merchant_name
            }
            return data
        else:
            data = {
                'NAME': "",
                'SALE_PRICE': "",
                'ORIGINAL_PRICE': "",
                'URL': "",
                'IMAGE' : "",
                'MERCHANT NAME' : merchant_name
            }
            return data  
    except Exception as e:
        print (e)

def ReadAsin(url_array, folder_name):

    if not os.path.exists(folder_name + '/images'):
        os.mkdir(folder_name + '/images')

    j=1
    extracted_data = []
    for i in url_array:
        parsed_data = parse(i, folder_name,j)
        j=j+1
        extracted_data.append(parsed_data)
                        
    # Writing scraped data to csv file
    with open(folder_name +'/scraped_data.csv', 'w', newline='', encoding="utf-8") as csvfile:
        fieldnames = ['NAME','SALE_PRICE','ORIGINAL_PRICE','URL', 'IMAGE', 'MERCHANT NAME']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()    
        # print(extracted_data)
        for data in extracted_data:
            writer.writerow(data) 

    wb = Workbook()
    ws = wb.active
    with open(folder_name +'/scraped_data.csv','r', encoding="utf-8") as f:
        for row in csv.reader(f):
            ws.append(row)
    wb.save(folder_name +'/scraped_data.xlsx')
    
#    jsWriter(folder_name)
  
    
