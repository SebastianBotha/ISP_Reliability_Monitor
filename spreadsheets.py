import gspread
from oauth2client.service_account import ServiceAccountCredentials

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
        self.creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", self.scope)
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
        
        
