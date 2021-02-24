import requests
from lxml import etree

from pymongo import MongoClient

client = MongoClient('mongodb://root:123456@172.16.10.136:27017/')
db = client['spider']
collection = db['result']



cookies = {
    'HMACCOUNT_BFESS': '98606595895E1C2C',
    'BAIDUID_BFESS': 'EA0F60982311110CC238B5EE68522A28:FG=1',
}

headers = {
    'authority': 'www.315jiage.cn',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
    'origin': 'https://www.315jiage.cn',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.315jiage.cn/n364233.aspx',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': '__cfduid=d28e514d3b45380fb95958c27498274c11613642406; iwmsGid=0FVZL399S8DAZVXFHT4S; Hm_lvt_4cce664ec5d8326cc457ab09053c15b2=1613642407,1613642563,1613973475; cf_clearance=7162d87d6a95ba2ba2d9b02b2e7ce79350cdffee-1614130873-0-250; rtv=52985B,42154072; Hm_lpvt_4cce664ec5d8326cc457ab09053c15b2=1614131087',
    'if-modified-since': 'Wed, 24 Feb 2021 01:41:14 GMT',
    'Referer': 'https://www.315jiage.cn/n364233.aspx',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
    'Connection': 'keep-alive',
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Dest': 'image',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'If-None-Match': 'e20946816f7a56ad5f166b26e3ccfff5',
    'if-none-match': '"bdc8d91aa8efd61:0"',
    'X-Requested-With': 'XMLHttpRequest',
    'x-requested-with': 'XMLHttpRequest',
}

params = (
    ('__cf_chl_captcha_tk__', '0abb4a9aea84c6ee33363acc04397fffefcadff0-1614130863-0-Aeq-nGjXogvMxWsQtCOzKevQ7Yt8QbjYh-RnoR9OYzkKP4y3Mbnb9OZHEoFaOd6_nQDuDCDpfkzj1c2n4OI3VXHrxzWA14ftOOHSg6ecY-aIRmZVUPMKUch5yw90wclpJcmDYpn-NpxWV-gEeJj5zBpORDkKiirrjOf778ubq4StdEnJzVsxfchDbWJmNssoDAhIReRZ0cnrJhnl-RwMJ-k4LRH7vPR80DqOXF6IbzCP4sUyn0X13oilM_zf4N3ytUYkVLO9k6uFOSWFRqS1WDz7w4KWo7X2_-KrzQl3Xaa_Hjf3NmsrR6N5Iau2yi6PpS_ueoT5Ypne6wYsBc0fniqCuHTxa9OVcMsRiI_WyPUs'),
)

data = [
  ('r', 'c59d5d17858cd68cfdd253c36c57f555ff0f28cc-1614130863-0-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'),
  ('id', '62657b69ed4a66c2'),
  ('id', '364233'),
  ('captcha_challenge_field', '79DE3658AA3E3422067926AFD5C86F7885363B438FAE226AE64FBDE7D6E84319D3EB3696E78A37B0962F400253E4BBD3'),
  ('manual_captcha_challenge_field', '7gdwy'),
  ('cmd', 'logVisit'),
]


#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('https://www.315jiage.cn/n364233.aspx?__cf_chl_captcha_tk__=0abb4a9aea84c6ee33363acc04397fffefcadff0-1614130863-0-Aeq-nGjXogvMxWsQtCOzKevQ7Yt8QbjYh-RnoR9OYzkKP4y3Mbnb9OZHEoFaOd6_nQDuDCDpfkzj1c2n4OI3VXHrxzWA14ftOOHSg6ecY-aIRmZVUPMKUch5yw90wclpJcmDYpn-NpxWV-gEeJj5zBpORDkKiirrjOf778ubq4StdEnJzVsxfchDbWJmNssoDAhIReRZ0cnrJhnl-RwMJ-k4LRH7vPR80DqOXF6IbzCP4sUyn0X13oilM_zf4N3ytUYkVLO9k6uFOSWFRqS1WDz7w4KWo7X2_-KrzQl3Xaa_Hjf3NmsrR6N5Iau2yi6PpS_ueoT5Ypne6wYsBc0fniqCuHTxa9OVcMsRiI_WyPUs', headers=headers, cookies=cookies, data=data)


# url = 'https://www.315jiage.cn/n325021.aspx'
# url = 'https://www.315jiage.cn/n327184.aspx'
# url = 'https://www.315jiage.cn/n134488.aspx'
# for i in range(2000, 400000):
for i in range(237016, 400000):
    url = 'https://www.315jiage.cn/n{}.aspx'.format(i)
    response = requests.post(url, headers=headers, params=params, cookies=cookies, data=data)
    print(response.status_code)
    if response.status_code == 200:
        print(url)
        response.encoding = 'utf8'
        root = etree.HTML(response.content)
        commodity_name_list = root.xpath('//*[@class="block-info-prop text-oneline"]/*[@itemprop="name"]/text()')
        commodity_code_list = root.xpath('//div/span[contains(text(), "条形码")]/following::text()')
        approval_no_list = root.xpath('//div[@class="block-info-prop text-oneline"]/u/a/text()')
        if commodity_name_list:
            try:
                result = {'id': i,'commodity_name': commodity_name_list[0], 'commodity_code': commodity_code_list[0], 'approval_no': approval_no_list[0]}
                collection.update({'id': i}, result, upsert=True)
                print(result)
            except:
                pass

