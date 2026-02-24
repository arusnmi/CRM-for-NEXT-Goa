import gspread
from google.oauth2.service_account import Credentials
import sys
from io import StringIO


old_stdout = sys.stdout
sys.stdout = StringIO()

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
credentials = Credentials.from_service_account_file("Creds.json", scopes=scopes)
client = gspread.authorize(credentials)

sys.stdout = old_stdout
sheet_id = "1NaTDtP9V5mWVBKagHOQV2kADs9nMTk8YVJfXwriEFQU"

def get_sheet_vals(sheet_id):
    sheet=client.open_by_key(sheet_id)

    value=sheet.sheet1.get_all_records()
    return value


def get_raw_data(value):
    VALS=[]
    for i in range(len(value)):
        mapvals= map(value[i].get, value[i])
        VALS.append(list(mapvals))
    return VALS

def update_status(sheet_id, row, col, status):
    sheet=client.open_by_key(sheet_id)
    sheet.sheet1.update_cell(row, col, status)


print(get_raw_data(get_sheet_vals(sheet_id)))
