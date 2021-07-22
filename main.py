from spreadsheets import *

# http://speedtest.mybroadband.co.za/

my_gsheet1 = GSheet("ISP test results", "data")
cell_value = my_gsheet1.GetCellValue(1,1)
print("the cell value is ", cell_value)

speed_test_data = ("date", "time", "ping", "download", "upload", "server")
print(speed_test_data)
my_gsheet1.InsertRow(2, speed_test_data)