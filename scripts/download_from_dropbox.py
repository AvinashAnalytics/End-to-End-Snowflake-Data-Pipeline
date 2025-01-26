import os
import dropbox
from dropbox.files import WriteMode

# Get the access token from the environment variable
access_token = os.getenv('DROPBOX_ACCESS_TOKEN')
dbx = dropbox.Dropbox(access_token)

# Download file
file_from = '/raw-data/sales_raw.csv'
file_to = 'sales_raw.csv'

with open(file_to, "wb") as f:
    metadata, res = dbx.files_download(path=file_from)
    f.write(res.content)
