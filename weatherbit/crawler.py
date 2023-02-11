import requests
import json
import time 
import datetime
import csv
from csv import writer
# start_time = datetime.datetime(2022, 7, 26, 21, 00)
# end_time = datetime.datetime(2022, 7, 26, 22, 00)
 
# start = time.mktime(start_time.timetuple())
# end = time.mktime(end_time.timetuple())

# API_key = 'f86292eeb4604dc5be9082f4c07cda2e'

# parameters = {
#     # "lat" : 10,
#     # "lon" : 10,
#     "city": "Hanoi",
#     "country": "Vietnam",
#     "start_data": '2022-01-14',
#     "end_date" : '2022-02-14',
#     "tz": 'local',
#     "key": API_key
# }
# response = requests.get("https://api.weatherbit.io/v2.0/history/airquality", params=parameters)
lst_proxy = []
with open("proxies.txt", 'r') as f:
    for line in f:
        lst_proxy.append(line.strip())
proxies = { 
        "http": lst_proxy 
    }      
# print(lst_proxy)
for city in ["Hanoi", "Danang", "HoChiMinh", "HungYen", "NinhBinh"]:
    response = requests.get(f"https://api.weatherbit.io/v2.0/history/airquality?city={city}&start_date=2022-01-01&end_date=2022-02-01&tz=local&key=c488d55f1db6402d88c842038d9a5c10", proxies=proxies)

    print(response.status_code)
    # print(response.json())
    
    # Open our existing CSV file in append mode
    # Create a file object for this file
    with open(f'{city}.csv', 'a') as f_object:
    
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)
        for res_ in reversed(response.json()['data']):
            List = [
                res_['timestamp_utc'].split('-')[0], 
                res_['timestamp_utc'].split('-')[1], 
                res_['timestamp_utc'].split('-')[2].split('T')[0], 
                res_['timestamp_utc'].split('T')[1].split(':')[0],
                res_['co'],
                res_['no2'],
                res_['o3'],
                res_['pm10'],
                res_['so2'],
                res_['pm25'],
            ]
        
            # Pass the list as an argument into
            # the writerow()
            writer_object.writerow(List)
    
        # Close the file object
        f_object.close()

