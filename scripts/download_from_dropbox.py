import os
import dropbox

# Get the Dropbox access token from an environment variable
access_token = os.getenv('DROPBOX_ACCESS_TOKEN')

# Check if the token is set properly
if not access_token:
    print("Error: DROPBOX_ACCESS_TOKEN not set.")
    exit(1)

# Initialize Dropbox client
dbx = dropbox.Dropbox(access_token)

# Path to the file on Dropbox
file_from = '/raw-data/sales_raw.csv'

try:
    # Try downloading the file
    metadata, res = dbx.files_download(path=file_from)
    
    # Write the content to a local file
    with open('sales_raw.csv', 'wb') as f:
        f.write(res.content)
    
    print("File downloaded successfully!")

except dropbox.exceptions.ApiError as e:
    print(f"Error downloading file: {e}")
    if isinstance(e, dropbox.exceptions.AuthError):
        print("Authorization error. Please check the access token permissions.")
except Exception as e:
    print(f"Unexpected error: {e}")
