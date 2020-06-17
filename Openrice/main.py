import requests
import re
from bs4 import BeautifulSoup
#input:
L =[]
urls = []
#url = 'https://www.openrice.com/zh/hongkong/restaurants?where=%E7%B2%89%E5%B6%BA'
#https://www.openrice.com/zh/hongkong/restaurants?where=%E7%B2%89%E5%B6%BA&page=2
def getdata():
    titles = soup.select('ul > li > div > section > div > h2 > a')
    comments = soup.select('ul > li > div > section > div > div > span')
    #rates = soup.select('ul > li > div > section > div > div > div > span')    #both good and bad length *2
    bookmarks = soup.select('#or-route-poi-list-main > ul > li > div > section.content-wrapper > section > div.text.bookmarkedUserCount.js-bookmark-count')
    addresss = soup.select('#or-route-poi-list-main > ul > li > div > section.content-wrapper > div.details-wrapper > div.central-content-container > div > div.icon-info.address > span')
    prices = soup.select('#or-route-poi-list-main > ul > li > div > section.content-wrapper > div.details-wrapper > div.central-content-container > div > div > div > div > span')
    #cates = soup.select('#or-route-poi-list-main > ul > li > div > section.content-wrapper > div.details-wrapper > div.central-content-container > div > div > div > div > ul > li > a')

    for title, comment, bookmark,address, price in zip(titles,comments,bookmarks,addresss,prices):
        data = {
            'title': title.get_text(),
            'comment': comment.get_text().replace(" 食評)","").replace("(",""),
            'bookmark': re.findall(r'data-count="(.*?)"></div>',str(bookmark))[0],
            'address': address.get_text().strip(),
            'price' : price.get_text()
        }
        #print(data)
        L.append(data)

#頁數
for page in range(1,18):
    url = 'https://www.openrice.com/zh/hongkong/restaurants/district/%E4%B8%AD%E7%92%B0?page='
    link = url + str(page)
    urls.append(link)

for i in urls:
    headers = {"Host": "www.openrice.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"}
    wb_data = requests.get(i, headers= headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    getdata()
    print(i)
def csv(filename,datalist):
    csv_column_name = ['title','comment','bookmark','address','price']
    f = open(filename + '.csv', 'w', encoding='utf-8')
    f.write("|".join(csv_column_name))
    f.write('\n')
    for row in datalist:
        f.write("|".join([row[field] for field in csv_column_name]))
        f.write('\n')
    f.close()
print(L)
csv("openrice",L)

