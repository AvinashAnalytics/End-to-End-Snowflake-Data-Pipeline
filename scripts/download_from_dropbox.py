import os
import dropbox

# Load environment variables
dropbox_access_token = os.getenv('DROPBOX_ACCESS_TOKEN')

# Check if the token is loaded correctly
if dropbox_access_token is None:
    raise Exception("Missing Dropbox access token")
else:
    print("Dropbox access token loaded successfully.")

# Initialize Dropbox client
dbx = dropbox.Dropbox(dropbox_access_token)
print("Dropbox client initialized.")

# Download file from Dropbox
file_from = '/raw-data/sales_raw.csv'
file_to = 'sales_raw.csv'

try:
    with open(file_to, "wb") as f:
        metadata, res = dbx.files_download(path=file_from)
        f.write(res.content)
    print(f"File downloaded successfully from {file_from} to {file_to}.")
except dropbox.exceptions.ApiError as err:
    print(f"Failed to download file from Dropbox: {err}")
