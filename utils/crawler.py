import requests
import json
import time 
import datetime
import csv
from csv import writer
from mongodb_database import insert_one_document
def crawl_per_hour(API_key):
    # API_key = 'f86292eeb4604dc5be9082f4c07cda2e'
    lst_proxy = []
    with open("proxies.txt", 'r') as f:
        for line in f:
            lst_proxy.append(line.strip())
    proxies = { 
            "http": lst_proxy 
        }      
    # print(lst_proxy)
    for city in ["HaNoi", "DaNang", "HoChiMinh", "HungYen", "NinhBinh"]:
        response = requests.get(f"https://api.weatherbit.io/v2.0/current/airquality?city={city}&key={API_key}", proxies=proxies)

        print(response.status_code)
        current_time_UTC = time.time()
        formated_time_UTC = time.gmtime(current_time_UTC)
        document = {}
        document['year'] = formated_time_UTC.tm_year
        document['month'] = formated_time_UTC.tm_mon
        document['day'] = formated_time_UTC.tm_mday
        document['hour'] = formated_time_UTC.tm_hour

        res_ = response.json()['data']
        document['co'] = res_['co']
        document['no2'] = res_['no2']
        document['o3'] = res_['o3']
        document['pm10'] = res_['pm10']
        document['so2'] = res_['so2']
        document['pm25'] = res_['pm25']

        insert_one_document(city=city, document=document)
            
            
    

