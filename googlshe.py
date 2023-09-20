

from __future__ import print_function
import pandas as pd
import os.path
import google.auth
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from amazonSc import  AmazonGetirme
from google.oauth2 import service_account

from anakazimaalgo import  MainAs
SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds=None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)




# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = ''

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range='Kategori İnceleme!A3:C100000').execute()

Amazonlinks=[]
URLS3= result.get('values', [])
Counter=0
URLS=[]
for count, i in enumerate(URLS3):
    if len(i)<=1:
        if Counter==0:
            Counter=count+3
        if  'amazon.com' not in i[0]:
             URLS.append(i)
        if 'amazon.com'  in i[0]:
            Amazonlinks.append([i[0]])
Urls2=[]
Result=[]
KazimaLinks=[]
Notkazimakinks=[]
for i in URLS:
    
    Urls2.append(i[0])
kazima=MainAs(Urls2)
result=kazima.Main()

#%%

for i in range(len(result)):
    if len(result[i])>0:
   
        for j in result[i]:
            KazimaLinks.append(j[0])
            Result.append(list(j))
for i in Urls2:
    if i  in KazimaLinks:
        pass
    else:
        Notkazimakinks.append(i)
if len(Notkazimakinks)>0:
    count=0
    while True:
        print('Conter:',count)
        kazima=MainAs(Notkazimakinks)
        result=kazima.Main()
        Notkazimakinks=[]
        for i in range(len(result)):
            if len(result[i])>0:
               
                for j in result[i]:
                    KazimaLinks.append(j[0])
                    Result.append(list(j))
        for i in Urls2:
            if i  in KazimaLinks:
                pass
            else:
                Notkazimakinks.append(i)
        count+=1
        if len(Notkazimakinks)==0:
            break

#%% resul yazdırma
for i in Amazonlinks:
    amazonsonuc= AmazonGetirme(i[0])
    Result.append(list(amazonsonuc))
import json
import google.auth
for i in range(len( Result)):
    for j in range(len(Result[i])):
        if Result[i][j]==None:
            Result[i][j]='None'
    
namee="Kategori İnceleme!A" + str(Counter) +":AZ10000"
myBody = {u'range': namee, u'values': Result, u'majorDimension': u'ROWS'}
rangeOutput = namee
res = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rangeOutput, valueInputOption='RAW', body=myBody ).execute()