from lxml import etree # 解析文档
import requests # 获取网页
import pandas as pd # 保存文档


# 获得网页的源代码
max_page = 20 # 最大爬取页面
all_title = [] # 爬取的标题储存列表
all_time = [] # 爬取的发表时间储存列表
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
    }  # 构造头文件，模拟真人登录。
for page in range(1,20):
    print('crawling the page is {}'.format(page))
    url_start = f'http://guba.eastmoney.com/list,zssh000001_{page}.html'
    data = requests.get(url_start, headers=headers)
    data = data.content.decode('utf-8')
    data = etree.HTML(data)  # 直接传入解码后的响应内容
    title = data.xpath('//tr[@class="listitem"]/td/div[@class="title"]/text()')
    publish_time = data.xpath('//tr[@class="listitem"]/td/div[@class="update mod_time"]/text()')

    print(title)
    print(publish_time)
    all_title += title
    all_time += publish_time

data_raw = pd.DataFrame
data_raw['title'] = all_title
data_raw['item'] = all_time
print(data_raw)