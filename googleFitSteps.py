import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import time

print("loading data from Google Fit")

#function for getting the 1st and last day of previous month as example data
from function import PreMonthFirstLast

# If modifying these scopes, delete the file auth/token.pickle
SCOPES = ['https://www.googleapis.com/auth/fitness.activity.read']

creds = None
DATA_SOURCE = "derived:com.google.step_count.delta:com.google.android.gms:estimated_steps"

#get array with 1st and last of previos month in an array (example data)
firstLast = PreMonthFirstLast()

#time.mktime() converts a struct_time object or a 9-element tuple into the number of seconds since the epoch
#https://www.geeksforgeeks.org/python/python-time-mktime-method/    
START = int(time.mktime(firstLast[0])*1000000000)
END = int(time.mktime(firstLast[1])*1000000000)
DATA_SET = "%s-%s" % (START, END)

    # The file auth/token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
if os.path.exists('auth/token.pickle'):
    with open('auth/token.pickle', 'rb') as token:
        creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        #JSON file containing authentication credentials for Google Cloud or other Google APIs
        flow = InstalledAppFlow.from_client_secrets_file('auth/googlecred.json', SCOPES)
        creds = flow.run_local_server()
        # Save the credentials for the next run
    with open('auth/token.pickle', 'wb') as token:
        pickle.dump(creds, token)

fit = build('fitness', 'v1', credentials=creds)

# Call the Drive v3 API
response = fit.users().dataSources().datasets().get(userId='me', dataSourceId=DATA_SOURCE, datasetId=DATA_SET).execute()
...
    
starts = []
ends = []
values = []
#adding up distance measured in steps
for point in response["point"]:
    if int(point["startTimeNanos"]) > START:
        starts.append(int(point["startTimeNanos"]))
        ends.append(int(point["endTimeNanos"]))
        values.append(point['value'][0]['intVal'])

KMwalkRun = (sum(values)) #total steps
print(str(KMwalkRun) + " Steps taken last month")
KMwalkRun = (sum(values)/1400) # converting steps to kilometres
KMwalkRun = str(round(KMwalkRun, 2)) #rounding to 2 decimal places and converting to a string
print(KMwalkRun + " km walked/ran last month")

#Troubleshoot links    
#https://developers.google.com/explorer-help/code-samples#python
#https://stackoverflow.com/questions/63446427/google-fit-data-not-retrieved-with-python
#https://gist.github.com/danielperna84/a02c307e123036973845e85b326cc940
#https://www.codingem.com/python-floor-division/
#https://www.epochconverter.com/