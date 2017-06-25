import urllib.request
import os.path

def download_file(url):
    filename = os.path.basename(url) or 'index.html'
    urllib.request.urlretrieve(url, filename)

if __name__ == '__main__':
    for i in range(1, 1478):
        download_file('http://www.baitoru.com/kanto/jlist/tokyo/page' + str(i) + '/')
