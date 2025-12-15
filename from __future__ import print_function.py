from __future__ import print_function
from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

credtiantls = service_account.Credentials.from_service_account_file('crm-system-481306-0a53d82b097a.json', scopes=SCOPES)
sheet_service = build('sheets', 'v4', credentials=credtiantls)
drive_service = build('drive', 'v3', credentials=credtiantls)
