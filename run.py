import requests
from lxml import etree

from pymongo import MongoClient

client = MongoClient('mongodb://root:123456@172.16.10.136:27017/')
db = client['spider']
collection = db['result']



cookies = {
    'HMACCOUNT_BFESS': '98606595895E1C2C',
    'BAIDUID_BFESS': 'B583E88F61A0F53325F7BAB499A2194B:FG=1',
}

headers = {
    'authority': 'www.315jiage.cn',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',
    'origin': 'https://www.315jiage.cn',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.315jiage.cn/n364243.aspx?__cf_chl_captcha_tk__=f3166e4b242382ab221e27fdaf48baf80c920262-1614216896-0-AdpQtoxuR2OFDSBD4OGWFzE0t6Xsb5kdWdaQMp10tf2Uys_xhHj0ucnP8rAi7daUsD9Ht01Zh99TJNiEDqAsAntDE5iGm2AAjc2Q4vTpwRCijltZgaMlM1VdLwziM3rarEiiG42SuSU7YlA7WAhwFDhpMeNYOZulKWLGCSjaMBihYBigS2PGLxPOYJoxWJpspznijNM08MYfJkR0JmoYflHehhWgmXCBlf2zqgy2XKaIA8xu99fyS8z-MgnFKCGRPIB7nKAsKy52ZMRwAGLC4ImwUfF1NHfsbmPwmmRR0l1yUTpVJFsHXH-F4717KNBjX_2h3IdJc4gRDcqeF2CWvmZGfjNv5sXGBeD61jUR9BDY',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': '__cfduid=d28e514d3b45380fb95958c27498274c11613642406; iwmsGid=0FVZL399S8DAZVXFHT4S; Hm_lvt_4cce664ec5d8326cc457ab09053c15b2=1613642407,1613642563,1613973475; cf_clearance=74281cf73a10221979655952d2862407c56b893e-1614216903-0-250; rtv=529DFA,38042239; Hm_lpvt_4cce664ec5d8326cc457ab09053c15b2=1614216902',
    'if-none-match': '"80823d71f7bad11:0"',
    'if-modified-since': 'Tue, 31 May 2016 04:46:49 GMT',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Dest': 'image',
    'Referer': 'https://www.315jiage.cn/n364243.aspx?__cf_chl_captcha_tk__=f3166e4b242382ab221e27fdaf48baf80c920262-1614216896-0-AdpQtoxuR2OFDSBD4OGWFzE0t6Xsb5kdWdaQMp10tf2Uys_xhHj0ucnP8rAi7daUsD9Ht01Zh99TJNiEDqAsAntDE5iGm2AAjc2Q4vTpwRCijltZgaMlM1VdLwziM3rarEiiG42SuSU7YlA7WAhwFDhpMeNYOZulKWLGCSjaMBihYBigS2PGLxPOYJoxWJpspznijNM08MYfJkR0JmoYflHehhWgmXCBlf2zqgy2XKaIA8xu99fyS8z-MgnFKCGRPIB7nKAsKy52ZMRwAGLC4ImwUfF1NHfsbmPwmmRR0l1yUTpVJFsHXH-F4717KNBjX_2h3IdJc4gRDcqeF2CWvmZGfjNv5sXGBeD61jUR9BDY',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'If-None-Match': 'e20946816f7a56ad5f166b26e3ccfff5',
    'x-requested-with': 'XMLHttpRequest',
}

params = (
    ('__cf_chl_captcha_tk__', 'f3166e4b242382ab221e27fdaf48baf80c920262-1614216896-0-AdpQtoxuR2OFDSBD4OGWFzE0t6Xsb5kdWdaQMp10tf2Uys_xhHj0ucnP8rAi7daUsD9Ht01Zh99TJNiEDqAsAntDE5iGm2AAjc2Q4vTpwRCijltZgaMlM1VdLwziM3rarEiiG42SuSU7YlA7WAhwFDhpMeNYOZulKWLGCSjaMBihYBigS2PGLxPOYJoxWJpspznijNM08MYfJkR0JmoYflHehhWgmXCBlf2zqgy2XKaIA8xu99fyS8z-MgnFKCGRPIB7nKAsKy52ZMRwAGLC4ImwUfF1NHfsbmPwmmRR0l1yUTpVJFsHXH-F4717KNBjX_2h3IdJc4gRDcqeF2CWvmZGfjNv5sXGBeD61jUR9BDY'),
)

data = [
  ('r', 'aed92099376cf5032e297195a13e6d8ea54178d4-1614216896-0-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'),
  ('id', '626dafd1bef86680'),
  ('id', '364243'),
  ('captcha_challenge_field', '19C3D72721D45F4F23C7AF4E2488B669C9B5AADF74A12ECED9E2008ECCA99575344222AE85ACCF2498DC69E4A0914CD9'),
  ('manual_captcha_challenge_field', 'n7dstm'),
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
for i in range(276959, 400000):
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

