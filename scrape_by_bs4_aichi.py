from bs4 import BeautifulSoup

with open('/Users/masanari/dev/src/github.com/Waddles1729/wget_train/www.baitoru.com/area/aichi/index.html') as f:
    soup = BeautifulSoup(f, 'html.parser')

print(soup.find_all('ul', class_="ul03"))
