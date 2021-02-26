import requests
from lxml import etree

from pymongo import MongoClient

client = MongoClient('mongodb://root:123456@172.16.10.136:27017/')
db = client['spider']
collection = db['result']


cookies = {
    'HMACCOUNT_BFESS': '98606595895E1C2C',
    'BAIDUID_BFESS': '32E8EFF771C1D3601D855D6311D9C98F:FG=1',
    'ab_sr': '1.0.0_Y2EwMWJmNjMxYTlmMzI5MzQ5MTdjOTJjYmZjYTA2OGY5MTk4NmZmZTE4Mzc3NDhhNWQ4ZmM1M2YwOThlMDAzMTA5NzYyMTg5NTYyNjk4NjRhYjFiNWQ0ZjAyYTlmNzEx',
}

headers = {
    'authority': 'www.315jiage.cn',
    'cache-control': 'no-cache',
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
    'referer': 'https://www.315jiage.cn/n345178.aspx?__cf_chl_captcha_tk__=112ce74387a9a2f7170a4d0afb80fc6ee6105d54-1614305913-0-Ac0Pk5FvlD28PR9UyS6iu7aa4-p2_AFY6B97S0qqn1065FoPwi8_7r0kHUHYENNGoY2YIyE8SQRkPL2L8i27mgMcmWOur2UJDOthVhCfCf1LT8i6xT30QmOjmU0Y_huBoRgEifJnziWuZvsT_QPerHlgyij6GivOzgy2BYlQiPAYmxxZg5etgcF9_Llsq51ZlR5FRTQ1Zec9ZeRWVILohrOEYqsO0c0q_moDml_Q5j8M1CfGCryc_qHhgRqEpU59QZhoGwpUHkNGnc9Ll8J5b54Rvj9MOke7h3YBaK_lFGjNpfPyMktWYeFU_ZGUxT5Qecr7aLBF7GUYg77-sRVWdeNERq5LeMo1YBg7o9P7b-I1',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': '__cfduid=d28e514d3b45380fb95958c27498274c11613642406; iwmsGid=0FVZL399S8DAZVXFHT4S; Hm_lvt_4cce664ec5d8326cc457ab09053c15b2=1613642407,1613642563,1613973475; cf_clearance=580a04b83cbef8f4a461fbd2e1c837819f56ff29-1614305926-0-250; rtv=52A3D7,16552827; Hm_lpvt_4cce664ec5d8326cc457ab09053c15b2=1614307598',
    'if-modified-since': 'Fri, 26 Feb 2021 02:19:07 GMT',
    'Referer': 'https://www.315jiage.cn/n345178.aspx?__cf_chl_captcha_tk__=112ce74387a9a2f7170a4d0afb80fc6ee6105d54-1614305913-0-Ac0Pk5FvlD28PR9UyS6iu7aa4-p2_AFY6B97S0qqn1065FoPwi8_7r0kHUHYENNGoY2YIyE8SQRkPL2L8i27mgMcmWOur2UJDOthVhCfCf1LT8i6xT30QmOjmU0Y_huBoRgEifJnziWuZvsT_QPerHlgyij6GivOzgy2BYlQiPAYmxxZg5etgcF9_Llsq51ZlR5FRTQ1Zec9ZeRWVILohrOEYqsO0c0q_moDml_Q5j8M1CfGCryc_qHhgRqEpU59QZhoGwpUHkNGnc9Ll8J5b54Rvj9MOke7h3YBaK_lFGjNpfPyMktWYeFU_ZGUxT5Qecr7aLBF7GUYg77-sRVWdeNERq5LeMo1YBg7o9P7b-I1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
    'Connection': 'keep-alive',
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Dest': 'image',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'If-None-Match': 'e20946816f7a56ad5f166b26e3ccfff5',
    'X-Requested-With': 'XMLHttpRequest',
    'x-requested-with': 'XMLHttpRequest',
    'pragma': 'no-cache',
}

params = (
    ('__cf_chl_captcha_tk__', '112ce74387a9a2f7170a4d0afb80fc6ee6105d54-1614305913-0-Ac0Pk5FvlD28PR9UyS6iu7aa4-p2_AFY6B97S0qqn1065FoPwi8_7r0kHUHYENNGoY2YIyE8SQRkPL2L8i27mgMcmWOur2UJDOthVhCfCf1LT8i6xT30QmOjmU0Y_huBoRgEifJnziWuZvsT_QPerHlgyij6GivOzgy2BYlQiPAYmxxZg5etgcF9_Llsq51ZlR5FRTQ1Zec9ZeRWVILohrOEYqsO0c0q_moDml_Q5j8M1CfGCryc_qHhgRqEpU59QZhoGwpUHkNGnc9Ll8J5b54Rvj9MOke7h3YBaK_lFGjNpfPyMktWYeFU_ZGUxT5Qecr7aLBF7GUYg77-sRVWdeNERq5LeMo1YBg7o9P7b-I1'),
)

data = [
  ('r', 'cdf087f298f8568e29d1f341e2f2c6f5d10657bc-1614305913-0-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'),
  ('id', '62762d18ad1266c2'),
  ('id', '345178'),
  ('captcha_challenge_field', 'D27E19A8AFA7CF48C0904564786EC178B4AFE42EED2B889914A22440BBB9DE1BDEDA86BA5310C0DD27BE2A9CEA329F89'),
  ('manual_captcha_challenge_field', 'oyrzz'),
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
for i in range(357270, 400000):
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

