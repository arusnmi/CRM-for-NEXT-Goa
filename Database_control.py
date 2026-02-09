import gspread
from google.oauth2.service_account import Credentials


scopes = ["https://www.googleapis.com/auth/spreadsheets"]
credentials = Credentials.from_service_account_file("Creds.json", scopes=scopes)
client = gspread.authorize(credentials)

sheet_id = "1NaTDtP9V5mWVBKagHOQV2kADs9nMTk8YVJfXwriEFQU"

def get_sheet_vals(sheet_id):
    sheet=client.open_by_key(sheet_id)

    value=sheet.sheet1.get_all_records()
    return value


def get_raw_data(value):
    for i in range(len(value)):
        mapvals= map(value[i].get, value[i])
        print(list(mapvals))

get_raw_data(get_sheet_vals(sheet_id))