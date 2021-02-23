import scrapy
from pymongo import MongoClient

cookies = {
    'HMACCOUNT_BFESS': '98606595895E1C2C',
    'BAIDUID_BFESS': 'A0D185949257010435344FBD96EC16C3:FG=1',
}

headers = {
    'authority': 'www.315jiage.cn',
    'cache-control': 'no-cache',
    'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.315jiage.cn/n85230.aspx',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': '__cfduid=d28e514d3b45380fb95958c27498274c11613642406; iwmsGid=0FVZL399S8DAZVXFHT4S; Hm_lvt_4cce664ec5d8326cc457ab09053c15b2=1613642407,1613642563,1613973475; cf_clearance=cb6dffcd3eb037ce1f0c1ea1ebce029d04b526ae-1614044748-0-250; rtv=5292BC,34211904; Hm_lpvt_4cce664ec5d8326cc457ab09053c15b2=1614045574',
    'if-modified-since': 'Tue, 23 Feb 2021 01:59:22 GMT',
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
    'Connection': 'keep-alive',
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Dest': 'image',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'If-None-Match': 'e20946816f7a56ad5f166b26e3ccfff5',
    'Upgrade-Insecure-Requests': '1',
    'if-none-match': '"bdc8d91aa8efd61:0"',
    'X-Requested-With': 'XMLHttpRequest',
    'x-requested-with': 'XMLHttpRequest',
    'pragma': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.315jiage.cn',
}

formdata = {
    'cmd': 'logVisit',
    'id': '85230'
}


class RunSpider(scrapy.Spider):
    name = 'run'
    allowed_domains = []
    start_urls = []
    client = MongoClient('mongodb://root:123456@172.16.10.136:27017/')
    db = client['spider']
    collection = db['result']

    def start_requests(self):
        for i in range(107680, 400000):
            # url = 'https://www.315jiage.cn/n327184.aspx'
            url = 'https://www.315jiage.cn/n{}.aspx'.format(i)
            print(url)
            yield scrapy.FormRequest(url, callback=self.parse_first, formdata=formdata, cookies=cookies,
                                     headers=headers, meta={'i': i}, dont_filter=True)

    def parse_first(self, response):
        i = response.meta['i']
        print(response.status)
        if response.status == 200:
            print(response.url)
            commodity_name_list = response.xpath(
                '//*[@class="block-info-prop text-oneline"]/*[@itemprop="name"]/text()').extract()
            commodity_code_list = response.xpath('//div/span[contains(text(), "条形码")]/following::text()').extract()
            approval_no_list = response.xpath('//div[@class="block-info-prop text-oneline"]/u/a/text()').extract()
            if commodity_name_list:
                result = {'id': i, 'commodity_name': commodity_name_list[0], 'commodity_code': commodity_code_list[0],
                          'approval_no': approval_no_list[0]}
                # self.collection.update({'id': i}, result, upsert=True)
                print(result)
