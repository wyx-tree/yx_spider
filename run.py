import requests
from lxml import etree

from pymongo import MongoClient

client = MongoClient('mongodb://root:123456@172.16.10.136:27017/')
db = client['spider']
collection = db['result']



cookies = {
    'HMACCOUNT_BFESS': '98606595895E1C2C',
    'ab_sr': '1.0.0_ZmRkYTRkZTkyOGFhMDFiMWEzMGVmNzM5MDQzN2NkYjFjM2Q1YTAyZjY2MTkxNjZmYjNmYTc5ZGYzOGJiM2Y0Mzc2ZTRkN2JlNzA5MTYyNzFlZmEwZDJhYzMwZjQ4N2Fj',
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
    'referer': 'https://www.315jiage.cn/n364243.aspx?__cf_chl_captcha_tk__=78ffdae346aab01f9581aee4f3b4a0bc725132b5-1614145390-0-AbY79Y0wKo6zVPAGmBYaIZCoPteKygvqT9dWJra0jd3bAICa6rKxO4ULaD0WQTSSZiuft7XkBnaxDv-Sq5rpqxeto3ByTnOew1_dI1jrwbdvDXR1-pVsG0hB9-oGSy6le3Mnc1Q9wxwAT57OpB_fHXRd-9mzbzahM9YFdMfsOfhMe85k_rlt_j-9ZmWCH8iWFq0tqaegd7Il0lbzidJm6cOuyLfRImMzRBvEagmFW2FwYGccMbaRJBl0dGzEvziBtlDiLfLrWOBhLtRsLzIQslFdKOGm5sIcFpp1fh__pBysKAskN2h7-S8bjbYfFkp_H1FgbTFnmA5QE08Ugo9wLrUk5L5fG0HTuqluEdpVHJMW',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': '__cfduid=d28e514d3b45380fb95958c27498274c11613642406; iwmsGid=0FVZL399S8DAZVXFHT4S; Hm_lvt_4cce664ec5d8326cc457ab09053c15b2=1613642407,1613642563,1613973475; cf_clearance=7fb58bb8cb093f3f1a2dcd884db4cf5a02db5174-1614145398-0-250; rtv=5299FC,20143442; Hm_lpvt_4cce664ec5d8326cc457ab09053c15b2=1614154790',
    'if-modified-since': 'Tue, 31 May 2016 04:46:49 GMT',
    'if-none-match': '"80823d71f7bad11:0"',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Dest': 'image',
    'Referer': 'https://www.315jiage.cn/n364243.aspx?__cf_chl_captcha_tk__=78ffdae346aab01f9581aee4f3b4a0bc725132b5-1614145390-0-AbY79Y0wKo6zVPAGmBYaIZCoPteKygvqT9dWJra0jd3bAICa6rKxO4ULaD0WQTSSZiuft7XkBnaxDv-Sq5rpqxeto3ByTnOew1_dI1jrwbdvDXR1-pVsG0hB9-oGSy6le3Mnc1Q9wxwAT57OpB_fHXRd-9mzbzahM9YFdMfsOfhMe85k_rlt_j-9ZmWCH8iWFq0tqaegd7Il0lbzidJm6cOuyLfRImMzRBvEagmFW2FwYGccMbaRJBl0dGzEvziBtlDiLfLrWOBhLtRsLzIQslFdKOGm5sIcFpp1fh__pBysKAskN2h7-S8bjbYfFkp_H1FgbTFnmA5QE08Ugo9wLrUk5L5fG0HTuqluEdpVHJMW',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'If-None-Match': 'e20946816f7a56ad5f166b26e3ccfff5',
    'x-requested-with': 'XMLHttpRequest',
    'pragma': 'no-cache',
}

params = (
    ('__cf_chl_captcha_tk__', '78ffdae346aab01f9581aee4f3b4a0bc725132b5-1614145390-0-AbY79Y0wKo6zVPAGmBYaIZCoPteKygvqT9dWJra0jd3bAICa6rKxO4ULaD0WQTSSZiuft7XkBnaxDv-Sq5rpqxeto3ByTnOew1_dI1jrwbdvDXR1-pVsG0hB9-oGSy6le3Mnc1Q9wxwAT57OpB_fHXRd-9mzbzahM9YFdMfsOfhMe85k_rlt_j-9ZmWCH8iWFq0tqaegd7Il0lbzidJm6cOuyLfRImMzRBvEagmFW2FwYGccMbaRJBl0dGzEvziBtlDiLfLrWOBhLtRsLzIQslFdKOGm5sIcFpp1fh__pBysKAskN2h7-S8bjbYfFkp_H1FgbTFnmA5QE08Ugo9wLrUk5L5fG0HTuqluEdpVHJMW'),
)

data = [
  ('r', 'c46de1d30912099e7119067969318511082d2208-1614145390-0-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'),
  ('id', '6266de14faae66bc'),
  ('id', '364243'),
  ('captcha_challenge_field', '364527B3CD663E654B6F1D3B2D733188465E2076C09EE86E8D15942F43ADB2D4EF9C760D2BB07A067EEF783153358444'),
  ('manual_captcha_challenge_field', 'bhq8h'),
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
for i in range(247330, 400000):
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

