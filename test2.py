import urllib.request

if __name__ == "__main__":
        for i in range(1, 1478):
            url = 'http://www.baitoru.com/kanto/jlist/tokyo/page' + str(i) + '/'
        path = '/Users/masanari/dev/src/github.com/Waddles1729/wget_train/bitle_scraping/index.html'
        urllib.request.urlretrieve(url, path)
