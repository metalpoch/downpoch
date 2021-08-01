'''
Utilities library
'''
import requests
from os import path

from clint.textui import progress


def download(url: str, output_dir: str):
    '''
    Function responsible for downloads
    '''
    request = requests.get(url, stream=True)
    filename = path.basename(request.url)
    print(filename, u'\u21b4')

    with open(path.join(output_dir, filename), 'wb') as f:
        total_length = int(request.headers.get('content-length'))
        for download in progress.bar(
            request.iter_content(chunk_size=1024),
            expected_size=(total_length/1024) + 1
        ):
            if download:
                f.write(download)
