from __future__ import print_function
import pickle
import os.path
import io
from apiclient.http import MediaIoBaseDownload
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

def GetFileFromDrive(fileName):

    # Dont do anything if the file is already there
    if os.path.exists('sounds/{0}'.format(fileName)):
        return fileName
    
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token2.pickle'):
        with open('token2.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token2.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    # Call the Drive v3 API
    #results = service.files().list(fields="*").execute()
    results = service.files().list(fields='*').execute()
    items = results.get('files', [])
    if not items:
        return None
    else:
        for item in items:
            #print(fileName, item['name'])
            if fileName == item['name']:
                #print(u'{0} ({1})'.format(item['name'], item['id']))

                request = service.files().get_media(fileId=item['id'])
                print(request)
                print(fileName)
                fh = io.FileIO('sounds/{0}'.format(fileName), 'wb')
                print(fh)
                downloader = MediaIoBaseDownload(fh, request)
                print(downloader)
                done = False
                while done is False:
                    status, done = downloader.next_chunk()
                    print(status.progress()*100)
                print('Done') 
                return fileName
    return None
