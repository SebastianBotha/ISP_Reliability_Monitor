import time
import schedule
from os import wait
from datetime import date
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def create_keyfile_dict():
    variables_keys = {
        "type": "service_account",
        "project_id": "bastionworkplace1",
        "private_key_id": "c07f7419d52d5764b088612731b08ec1baa47f7a",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDTkjRLsFls6O0M\nj7vNbQGjMOGG+ysBjSVBw/8Te210oc/I8vlEErwNeHlBr6TTqE5dxEAKatcPgbCh\nOXVxhTDTqe9xdPCBEelwRNviaSxNICXCT6S98PXkETP2NRhipFh/DU84KX5uJbq6\ndojSlT16PYMpup/2jseEOx5W2Gh+1cXPZg+6+tQqXqskIQl3+xU6+euY6Dw3B5XF\nbu4d3zMjksnL5dXMCBjcfswGPdpP/kvWVfextOfXtsii/PL1ZRwee6Du0LEw0Z9Y\nAl7U5T2PsQTB/bbfLO7pOYyLkYrz16tc1BBqhW+ZEla+4YUsl2J6w8wu4NpBj6jM\nFzhv7IqjAgMBAAECggEAVxZg+WDjRn3QibGmg+YhXOuzgazkpHRViC8l0X6mbPJo\nRdah/T/a8Y6MFxo2Njua2mT8WW1mDgd7zbmJmstQ8GeMXL7eerqFRQXLHvTc2/hm\nIohHDzpe9NyR74AmhAATP2UanUsTNELKjJNbOZdd4XHtiiE8VDCsdsUg9W2KAd67\nknrWA69c9/EmmXwXZWaraOW+9rULTAp486fr6J8398cnWjZub1cF8SFYZAuQhP11\nXxX7S4Jd2KJxHf+LGgobcSB5xoeNFcevqcRI6GecuOUZNJS8tFHz4EVLU/Ldvqav\nqiY29gv7WwmVyIdq56zVYszVaEPh3GHCKiShj1sn/QKBgQD9JtEpelRBNFRplKVA\nRhgFc2fuQFeeXidFMORK7rCW+pdY1PXYV0SQT24MguKXmdyKZGigGYlGn0xNqxsn\nbp60xXh+PtIJtf2BxusjZbzGoPQJdkXP4MzcqtHtCELMf6indcR+rncI8TVCni7j\nN9HEruX//ntu9p4vK4LsflAFdwKBgQDV854uMa6I1SgvtEml42ugJEFN7uuYPh/c\n5in9EhqzHaVCSmM2jaVz92GJ72DuGur5Ac1vHWU3AtzTGGgVWeL1YOFJWUArmPrK\nngyrHf8yfhPkeKN7gLhaOxdboWg+7QDBJz7ueHnBLtPGj+9DYp93kM9Fh1faMmRl\nOuEx4V4fNQKBgHn9I5vGPCWzrt216LABVwABbdrMnKxPGMNp3QkS3nvSw+3lqZaX\n7w1PiWt0AvclCLaTzisgQxuKFf3zb0FgOBBKfFbxtMtDLKdGEPdcxkw9MXwBx4B2\nBqJrmn+LlIzxE3em84pMTkY73ft9OID73BTYZzMmEZsWMoHuiMen0q3fAoGANqpl\nazYkey/DcdTl0G34LNW2ndwC9EZDS+S/K7s5eTSE6hgpm2G7uZKmqGCyaoQUL4Vn\nYRGor9Kaa5Fb3sC1va6AQYZ9X+ZZhfW2FO64KsWN/Z1ZYA/2io94m1/1S8awn6mQ\nacv8iACX+a8DGjuTtTAZ1ZEMQGMJxdeyfFUyAFUCgYEAguRTmrjEOKX1+vB94UFO\noTD7vdNtGoFkefCu37265Bcr2mGV2UK23kj4Nl2vRMkkk783XhmERCbWD8ualWQA\n5TlZN3Di+jITLFkmekB5QR2v6HgUUXBvXKTOvYkBoOiqUxXBUXvVuJ85EhrDWt/7\nuZwIemvfRJLriZL684FXJqY=\n-----END PRIVATE KEY-----\n",
        "client_email": "bastion@bastionworkplace1.iam.gserviceaccount.com",
        "client_id": "114949527424484279138",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/bastion%40bastionworkplace1.iam.gserviceaccount.com"
        }
    return variables_keys

class GSheet():
    """use this class to quickly setup and access Google Sheet commands 
    1. scope is required for back end connection to google sheets API
    2. credentials required to verify with the sheet you are accessing. 
        Json file is from the google developer download online
    3. workbook_name is the name of the google sheet we are accessing 
    4. sheet_name is the specifc sheet to access within the workbook 
    5. Setup refernce: https://www.youtube.com/watch?v=cnPlKLEGR7E
    6. module reference https://docs.gspread.org/en/v3.7.0/
    """
    def __init__(self, workbook_name, sheet_name):
        # print(" Accessing the init scripts")
        self.scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
                 "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
        self.creds = ServiceAccountCredentials.from_json_keyfile_dict(create_keyfile_dict(), self.scope)
        #self.creds = ServiceAccountCredentials.from_json_keyfile_name(create_keyfile_dict(), self.scope)
        self.client = gspread.authorize(self.creds)
        self.sheet = self.client.open(workbook_name).worksheet(sheet_name)

    def GetAllData(self):
        data = self.sheet.get_all_records()
        return data

    def GetRowData(self, row_number):
        data = self.sheet.row_values(row_number)
        return data

    def GetColData(self, col_number):
        data = self.sheet.col_values(col_number)
        return data

    def GetCellValue(self, row_num, col_num):
        data = self.sheet.cell(row_num, col_num).value
        return data

    def InsertRow(self, row_number, data):
        self.sheet.insert_row(data,row_number,"RAW")
        

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
run_ISP_tester()

#schedule.every(60).minutes.do(run_ISP_tester)
# schedule.every().hour.do(run_ISP_tester)
schedule.every().hour.at(":59").do(run_ISP_tester)
#schedule.every(1).minutes.do(run_ISP_tester)
#schedule.every().day.at("19:51").do(run_ISP_tester)
now = datetime.now() 
current_time = now.strftime("%H:%M:%S")
print("schedule started ", now)

while True:
    schedule.run_pending()
    time.sleep(1)