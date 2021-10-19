import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Template1").sheet1  # type your sheet's name

#data = sheet.get_all_records()

#row = sheet.row_values(1)  # Get a specific row
#col = sheet.col_values(3)  # Get a specific column
#cell = sheet.cell(row_number,column_number).value
#print(cell)  # Get the value of a specific cell

#sheet.add_rows(insertRow)  # Insert the list as a row at index 4

sheet.update_cell(1000,26, 2)  # Update one cell

cell = sheet.cell(1000,26).value
print(f"we start with filling the {cell} column ")
#numRows = sheet.row_count  # Get the number of rows in the sheet

# sheet.update_cell(12,2, 'test')  # Update one cell
#
# cell = sheet.cell(12,2).value
# print(f"we start with filling the {cell} column ")
# #numRows = sheet.row_count  # Get the number of rows in the sheet

# insertRow = [1,2,3,4,5,6,7,8,9]
# sheet.insert_row(insertRow, 11)
# sheet.delete_rows(10)
#
# sheet.update_cell(2,2, insertRow[0])
# sheet.update_cell(3,2, insertRow[1])
