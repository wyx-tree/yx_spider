import re
import time

import requests
from lxml import etree
from setting import *
from pymongo import MongoClient

client = MongoClient('mongodb://root:123456@172.16.10.136:27017/')
db = client['spider']
collection = db['result']
params = {}
for i in collection.find({'is_crawl': {'$exists': False}}):
    try:

        url = 'https://www.315jiage.cn/n{}.aspx'.format(i['id'])
        response = requests.post(url, headers=headers, params=params, cookies=cookies, data=data, proxies=proxies)
        print(response.status_code)
        if response.status_code == 200:
            response.encoding = 'utf8'
            root = etree.HTML(response.content)

            commodity_name_list = root.xpath('//*[@class="block-info-prop text-oneline"]/*[@itemprop="name"]/text()')
            commodity_name = ''.join(commodity_name_list[0].split())
            commodity_name_new = commodity_name.strip()

            commodity_code_list = root.xpath('//div/span[contains(text(), "条形码")]/following::text()')
            commodity_code = ''.join(commodity_code_list[0].split())

            approval_no_list = root.xpath('//div[@class="block-info-prop text-oneline"]/u/a/text()')
            approval_no = ''.join(approval_no_list[0].split())

            guige_list = root.xpath('//div/span[contains(text(), "规格：")]/following::text()')
            guige = ''.join(guige_list[0].split())

            baozhuangdanwei_list = root.xpath('//div/span[contains(text(), "包装单位：")]/following::text()')
            baozhuangdanwei = ''.join(baozhuangdanwei_list[0].split())

            shengchanchangjia_list = root.xpath('//div/span[contains(text(), "生产厂家：")]/following::text()')
            shengchanchangjia = ''.join(shengchanchangjia_list[0].split())

            if commodity_name_list:
                try:
                    result = {'id': i['id'], 'commodity_name': commodity_name, 'commodity_code': commodity_code,
                              'approval_no': approval_no, 'guige': guige, 'danwei': baozhuangdanwei,
                              'changjia': shengchanchangjia, 'is_crawl': 1}
                    collection.update({'id': i['id']}, result, upsert=True)
                    print(result)
                except Exception as ex:
                    print(ex)
    except Exception as ex:
        print(ex)
        pass