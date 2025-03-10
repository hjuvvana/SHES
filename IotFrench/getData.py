import os
import re
import requests
output_file ='/Users/samuel/IotFrench/to_download.txt'

download_dir = '/Users/samuel/IotFrench/downloaded_files'
with open("Data.txt", "r") as data:
    content = data.read()

# Use regex to find all occurrences of contentUrl
content_urls = re.findall(r'"contentUrl":\s*"([^"]+)"', content)

with open(output_file, 'w') as file:
    for url in content_urls:
        file.write(url + '\n')

print(f'Extracted {len(content_urls)} content URLs and saved to {output_file}')


def download_file(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)

for url in content_urls:
    file_name = url.split('/')[-1]
    save_path = os.path.join(download_dir, file_name)
    print(f'Downloading {url} to {save_path}')
    download_file(url, save_path)