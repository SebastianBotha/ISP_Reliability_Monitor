import time
import schedule
from os import wait
from spreadsheets import *
from datetime import date
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



#browser = webdriver.Chrome(executable_path = '/usr/lib/chromium-browser/chromedriver')
#browser.get('https://automatetheboringstuff.com')

def run_ISP_tester():
    """
    Running web scraper and speed test online 
    """
    now = datetime.now() 
    current_time = now.strftime("%H:%M:%S")
    print("running ISP Test ", now)
    # current date and time
    now = datetime.now() 
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%m/%d/%Y")

    # path to chrome driver: MACBOOK 
    ChromDriver_path = '/usr/lib/chromium-browser/chromedriver'
    
    #path to chrome driver: PI
    

    # initiate a Chrome window using Chrome web driver 
    driver = webdriver.Chrome(ChromDriver_path)

    # start webpage 
    driver.get("http://speedtest.net")

    xpath_start = "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a"

    # wait for start button to load
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, xpath_start))
        )
    except:
        driver.quit()


    # click button
    python_button = driver.find_elements_by_xpath(xpath_start)[0]
    python_button.click()

    # wait for test to finish and generate results 
    time.sleep(70)

    print("done waiting")

    # read results 

    ping_value = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span")
    upload_value = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span")
    download_vlaue = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")
    server_value = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[3]/div/div/div[1]/div[2]/div[2]/a")

    # save values 
    speed_test_data = (current_date, current_time, ping_value.text, download_vlaue.text, upload_value.text,server_value.text)

    # close browswer 
    driver.quit()

    """
    Writing value to google sheet 
    """

    my_gsheet1 = GSheet("ISP test results", "data")
    my_gsheet1.InsertRow(2, speed_test_data)
    
    # clear speedtest data 
    speed_test_data = ("","","","","","")
    now = datetime.now() 
    current_time = now.strftime("%H:%M:%S")
    print("finished ISP Test ", now)
    
"""
   Schedule the job to be run
"""
#run_ISP_tester()

schedule.every(60).minutes.do(run_ISP_tester)
#schedule.every(1).minutes.do(run_ISP_tester)
#schedule.every().day.at("19:51").do(run_ISP_tester)
now = datetime.now() 
current_time = now.strftime("%H:%M:%S")
print("schedule started ", now)

while True:
    schedule.run_pending()
    time.sleep(1)