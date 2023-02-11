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
# for city in ["Hanoi", "Danang", "HoChiMinh", "HungYen", "NinhBinh" ]:
lst_proxy = []
with open("proxies.txt", 'r') as f:
    for line in f:
        lst_proxy.append(line.strip())
proxies = { 
        "http": lst_proxy 
    } 
api_key = "e681d53b3baa48a59681782f575cf292"
api_key = "d39aaf4719634d26a2b85eca23097d01"
for city in [ "NinhBinh"]:
    response = requests.get(f"https://api.weatherbit.io/v2.0/history/airquality?city={city}&start_date=2022-10-01&end_date=2022-11-01&tz=local&key={api_key}",
                            proxies=proxies)

    print("status: ", response.status_code)
    # print(response.json())
    
    # Open our existing CSV file in append mode
    # Create a file object for this file
    with open(f'{city}_10_11.csv', 'a') as f_object:
    
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