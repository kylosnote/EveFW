'''
1. Request to get the table
2. Use Beautifulsoup to access
3. Get the Link, and use Request to download all into destination path
4. On exception should delete all produced file
'''
import requests
from bs4 import BeautifulSoup
import argparse
from datetime import datetime
import pathlib
import asyncio
import aiohttp
import tarfile

parser = argparse.ArgumentParser()
parser.add_argument('--month', '-m', action="store", type=int, help="The month to retrieve in int format")
args = parser.parse_args()
base_path = pathlib.Path(__file__).parent.resolve()


async def download_file(url, year, month):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if "content-disposition" in response.headers:
                header = response.headers["content-disposition"]
                filename = header.split("filename=")[1]
            else:
                filename = url.split("/")[-1]
            
            filename = f"{base_path}/history/{year}/{month}/{filename}"
            with open(filename, mode="wb") as file:
                while True:
                    chunk = await response.content.read()
                    if not chunk:
                        break
                    file.write(chunk)
                print(f"Downloaded file {filename}")
            return filename

async def main(month):
    url = 'https://data.everef.net/killmails/2024/' #TODO: Dynamic Year
    page = requests.get(url = url)
    if not month:
        month = datetime.now().month-1
    year = datetime.now().year

    keyword = f'/killmails/2024/killmails-{year}-{str(month).zfill(2)}-'
    base_url = 'https://data.everef.net'

    final_url_list = []

    if page.status_code == 200:
        soup = BeautifulSoup(page.text, 'html.parser')
        data_elements = soup.find_all(attrs={'class':'data-file-url'})
        for each in data_elements:
             if keyword in each.attrs['href']:
                 final_url_list.append(f"{base_url}{each.attrs['href']}")
    else:
        raise Exception("Http Status Code is not 200")
    print(final_url_list)
    pathlib.Path(f"{base_path}/history/{year}/{month}").mkdir(parents=True, exist_ok=True)#Create directory incase doenst exist
    tasks = [download_file(url=url, year=year, month=month) for url in final_url_list]
    downloaded_filename_list = await asyncio.gather(*tasks)
    pathlib.Path(f"{base_path}/killmails/{year}/{month}").mkdir(parents=True, exist_ok=True)#Create directory incase doenst exist
    unpack_location = f"{base_path}/killmails/{year}/{month}"
    for each_tar in downloaded_filename_list:
        tar = tarfile.open(each_tar, 'r:bz2')
        tar.extractall(unpack_location)
        tar.close()

if __name__ == '__main__':
    asyncio.run(main(month=args.month))