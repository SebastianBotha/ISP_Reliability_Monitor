import schedule
import time

def job():
    print("I'm working...")
    
#schedule.every(10).seconds.do(job)
schedule.every().day.at("19:51").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)