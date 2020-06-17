import urllib.request
import re

AN = input('請輸入商品代號')
PG = int(input('請輸入頁數')) + 1
FILENAME = input('請輸入商品名稱')
DATA_LIST = []

for i in range(1,PG):
    url = 'https://rate.taobao.com/feedRateList.htm?auctionNumId='+ AN +'&currentPageNum=' + str(i)
    print('正在處理第'+str(i)+'頁評論')
    content = urllib.request.urlopen(url).read()
    content = content.decode('gbk')

    comments = re.findall(r',"content":"(.*?)","rateId',content)
    colors = re.findall(r'"sku":"(.*?)","title',content)
    vips = re.findall(r'displayRatePic":"(.*?).gif","nickUrl',content)
    vip_ranks = re.findall(r'rank":(.*?),"avatar',content)
    dates = re.findall(r'"date":"(.*?)","shareInfo',content)

    # for i in vips:
    #     print(i)
    #print(len(dates))

    for comment, color, vip, vip_rank, date in zip(comments, colors, vips, vip_ranks, dates):
        data = {
            '評論' : comment,
            '款式' : color,
            '會員級別': vip,
            '會員積分': vip_rank,
            '日期': date
            }
        DATA_LIST.append(data)


csv_column_name = ['日期','會員級別','會員積分','款式','評論']
f = open(FILENAME + AN +'.csv','a',encoding='utf-8')
f.write(",".join(csv_column_name))
f.write('\n')

for row in DATA_LIST:
    f.write(",".join([row[field] for field in csv_column_name]))
    f.write('\n')

f.close()
