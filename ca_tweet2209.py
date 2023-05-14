import requests
import re
from urllib.parse import urljoin
import gzip
import shutil

# URL of the page containing the download links
#url = 'https://zenodo.org/record/1808741'
url = 'https://archive.org/details/archiveteam-twitter-stream-2022-09'

# Send a GET request to the URL and retrieve the HTML content
response = requests.get(url)
html_content = response.text

# Search for the download links in the HTML content
download_links = re.findall(r'<a class="stealth download-pill" href="([^"]+)"', html_content)

# Convert the relative URLs to absolute URLs
base_url = 'https://archive.org/'
download_links = [urljoin(base_url, link) for link in download_links]
#Test with 2 files
#download_links = download_links[17:]

# Download the files
for link in download_links:
    response = requests.get(link)
    filename = link.split('/')[-1]
    with open(filename, 'wb') as f:
        f.write(response.content)
        print(f'{filename} downloaded successfully')
        # Open the compressed file
        #with gzip.open(filename, 'rb') as f_in:
         #   # Create the extracted file
         #   with open(filename, 'wb') as f_out:
                # Copy the contents of the compressed file to the extracted file
          #      shutil.copyfileobj(f_in, f_out)

        print(f'{filename} extracted successfully')