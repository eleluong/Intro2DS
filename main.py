import time
import schedule
from utils.crawler import crawl_per_hour
from utils.predict_send_data_to_gui import send_data_to_gui

API_key = 'e681d53b3baa48a59681782f575cf292'

def job():
    print("I'm working...")
def job1():
    print("I'm working 1...")
if __name__ == "__main__":
    # schedule.every().hour.do(crawl_per_hour, API_key= API_key)
    # schedule.every().hour.do(send_data_to_gui)
    # schedule.every().week.do(retrain)
    schedule.every(10).seconds.do(job)
    schedule.every(10).seconds.do(job1)
    data_to_gui = send_data_to_gui()
    while True:
        schedule.run_pending()
        time.sleep(1)
