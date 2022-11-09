# sync file downloader
import requests
from bs4 import BeautifulSoup

from os import path, makedirs
from datetime import datetime

url = "https://builds-by.kaspersky.ru/"
headers = {"User-Agent": "Kaspersky PDF downloader/0.1"}
output_path = './Kaspersky-Products-Home'


def download(url, chunk_size=8192, filename=None, data_path='.'):
    output_file = url.split('/')[-1] if not filename else filename

    if not path.exists(data_path):
        makedirs(data_path)
    output_file = path.join(data_path, output_file)

    with requests.get(url, headers=headers, stream=True, timeout=5) as r:
        r.raise_for_status()
        with open(output_file, 'wb') as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)


def get_urls(url):
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'lxml')

    download_buttons = soup.find('div', class_='row product__content',
                                 id='home').find_all('a', class_='button transparent')

    pdf_links = [i.get('href') if i.get('href')[:4] == 'http' else url + i.get('href')
                 for i in download_buttons if i.get('href')[-3:] == 'pdf']

    return pdf_links


if __name__ == '__main__':
    urls, invalid = get_urls(url), 0
    start = datetime.now()

    for task_url in urls:
        try:
            download(task_url, data_path=output_path)
        except Exception as ex:
            print("[-] Error:", ex)  # File, HTTP or Requests raise
            invalid += 1

    delta = (datetime.now() - start).total_seconds()
    print(f"[+] Path:", path.abspath(output_path))
    print(f"[+] Valid/Invalid: [{len(urls) - invalid}/{invalid}] {delta:.03f}sec")
