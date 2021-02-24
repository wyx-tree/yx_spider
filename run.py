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
    'referer': 'https://www.315jiage.cn/n364243.aspx?__cf_chl_captcha_tk__=5bbcedceb385ed0e88a91ed3579c9032fa4edac0-1614168220-0-AWdh6cMZgDaivw_Fuw6bwqARkh366D75x2Kys6lTW988hK3CFX4BNcY7SoTpE2raReCjHM7OduDJ438BqcVvJDfDMPnKThh6Zi3VR3biXwSUwZLrPSCTQV-sw-zitql2KyYgi3gLQTJUSSvrpzk8vxqfDFL7SxtIdTLSrA0Vrp0E5dx1d2tY9BthmBuVgqNZMI2cTYIMfoJGaNgFmsjp7kZM3mG1cuFYPs2K7IQvQmRKbeNFWivZL7cnmmpiW43jsyOVmlJmxOkyZzy4x0Pl3j9FDcZ9pEGbnTUUJwoVuShoPdpcXOnBnGp08ccRvU7MnvpcLbwiE3qvHOFd4ox-vQoBme5VrDCt6XWFEPJD1TWI',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': '__cfduid=d28e514d3b45380fb95958c27498274c11613642406; iwmsGid=0FVZL399S8DAZVXFHT4S; Hm_lvt_4cce664ec5d8326cc457ab09053c15b2=1613642407,1613642563,1613973475; cf_clearance=3d508990fde67d2dc27f84eede83d2c69e1641b0-1614168227-0-250; rtv=529AEB,33302333; Hm_lpvt_4cce664ec5d8326cc457ab09053c15b2=1614168228',
    'if-none-match': '"80823d71f7bad11:0"',
    'if-modified-since': 'Tue, 31 May 2016 04:46:49 GMT',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Dest': 'image',
    'Referer': 'https://www.315jiage.cn/n364243.aspx?__cf_chl_captcha_tk__=5bbcedceb385ed0e88a91ed3579c9032fa4edac0-1614168220-0-AWdh6cMZgDaivw_Fuw6bwqARkh366D75x2Kys6lTW988hK3CFX4BNcY7SoTpE2raReCjHM7OduDJ438BqcVvJDfDMPnKThh6Zi3VR3biXwSUwZLrPSCTQV-sw-zitql2KyYgi3gLQTJUSSvrpzk8vxqfDFL7SxtIdTLSrA0Vrp0E5dx1d2tY9BthmBuVgqNZMI2cTYIMfoJGaNgFmsjp7kZM3mG1cuFYPs2K7IQvQmRKbeNFWivZL7cnmmpiW43jsyOVmlJmxOkyZzy4x0Pl3j9FDcZ9pEGbnTUUJwoVuShoPdpcXOnBnGp08ccRvU7MnvpcLbwiE3qvHOFd4ox-vQoBme5VrDCt6XWFEPJD1TWI',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'If-None-Match': 'e20946816f7a56ad5f166b26e3ccfff5',
    'x-requested-with': 'XMLHttpRequest',
}

params = (
    ('__cf_chl_captcha_tk__', '5bbcedceb385ed0e88a91ed3579c9032fa4edac0-1614168220-0-AWdh6cMZgDaivw_Fuw6bwqARkh366D75x2Kys6lTW988hK3CFX4BNcY7SoTpE2raReCjHM7OduDJ438BqcVvJDfDMPnKThh6Zi3VR3biXwSUwZLrPSCTQV-sw-zitql2KyYgi3gLQTJUSSvrpzk8vxqfDFL7SxtIdTLSrA0Vrp0E5dx1d2tY9BthmBuVgqNZMI2cTYIMfoJGaNgFmsjp7kZM3mG1cuFYPs2K7IQvQmRKbeNFWivZL7cnmmpiW43jsyOVmlJmxOkyZzy4x0Pl3j9FDcZ9pEGbnTUUJwoVuShoPdpcXOnBnGp08ccRvU7MnvpcLbwiE3qvHOFd4ox-vQoBme5VrDCt6XWFEPJD1TWI'),
)

data = [
  ('r', '15119ffadb88b420984e4c5ec51478047679b0b3-1614168220-0-AUTkxHhFBwC7vKBkvi8/V4YDOCKp9o+KST0BopbSvRa5io5675YGnOLyfyCWnOQZiFwbExzEKr+XtGos8aH6kI5gSulHmXAem4wSaQX/EVLnpKyLuliwF1fs/8zjd6y87guU7yBNSsPb1XYyFPyU7Spg/bkZtChY8T6lPc7mZJvJQ95Ex1krn98GDa+F7HhYq/80xG9caA21TOLtBS5jAmy5/69Y9ZZuP74KnRQ70T5K3drKx/VR0y+H1O5hHkqJVr63dXe4W7Gh/62Sr9S2Y+n1gvOYUCXC1AFGvVRyKSHlepTpMDSubacLR/oIZ5JWtPCWMxYi/kBGvEZfLteKtx4H9XaIQsFPMClu22GQjGsM9pduj1PS/D6nSiIncIOvbqsFrC9GqRzN/e3YgVBRYFTVwBpgdXJwIjnxbaokmfGe55RlzYS/38QHYy/5dh0MYJAljMm3p1Kl0jU7sFGwULtCldiBoK4ciOIbshgNRxDdhcPijAmNR3H06R/yonkgPloWUFs1n21B9xB6VUKSud/tDnwkSHD8OXGjEoWhmqdpZ0Jci+f2CydIG7g7DSBbjF38GFnpfVPgzjsCbgSgPRXCSkgx3kKqdLHTXFEM6LqG+rxzxm3EVNltnXpKMfb7zckzwbEgj5cWZ2PyNW6iRNnQR6SjICj9NtcW07qZtuDGPzKtVTkwQEhAcwj7SPE4PaBiqbRbvACUdCqvlBwMyRr0dI4j09IrUwNnBlrM4/RlXZLSc2vBFSt1eGJ4ZJEz4UrfB+yUUV5JyW/wK0MPwTMFCJa9O3QP4FOiGGA0Mj4zXHqOItnHQGn0INVswiiGj6K9k2K0qT9Ti9xJPqyMkY4OzK3n+qQDJRFMVybC32hZ48M6Tmr7yeY0gfmOfihvWQAXWerjIGnGgFpeVnHv8HD15CPRax1tk/A8s9otkMky1afKbMALq2f0B/ukXIJce9jjmZ0sY7ggCXTB2CxOKHlkfSGeLjW4R4F1BFROIFSTHLgV6BZPEgArcKfJELTW7J93J+qGzhm/66KtS1+uqAL7v1v4XYzqygTKAy2KR63U8XgPBUhZEzsNRktpKZWzYmZWPlnp4an3WPabhpjv8j/PXRLU4fJ4fInkzDN1/BmShgpuFTNJQo5bAE1A6T2jHXpz4Db3lCE2fRzPMQMCuAab47IMKT6xJI+zIisUorquHXRnvFpdudWi+TXdITXrc23aQU9gN562Ajwb6N3Zzau/OIlucy81pYJIZqBypLXzqp1APAWip2qMtLfyPkH2DK8dSSwq8pqkS1TE+mXqGBktzN++CGox6+1wGgoiTbV7y7t6z7Jc8zAGT/Mjp/muXmbsY1YS9/FYcmXp1DdrTXt+w/BfXagFMsEC5uUv8AH4NLodKS3+0QHY4BExzBVmcI4k+E//RVdJ2eR8gEBXbcjt95LeMH4KNEHjxh1JDi4EYXWbDnMQ0J/uxOa+ogulNLRGdEMS9P+NE5kN7JwId52vrTJupi02jW7neM5W2fgH6LFDA9PzKClQyjoVXce1u4xSJR3at/QKiZtYTlJKeqRd9hsj6VUJyO6IgSuKzV0MotXut77d1AaUTD9jGSgToBaXwFNx6LEbgBvFnZ3XVRPKc/DskBjHhJaObmazqlJn1GYLFtfTuqcmDB2xkXV/6jbL9UIPau4ULRnzYVIcvSs4QL2KAbQ8NcvyXx6O/Boc1zNt7vFRhPP/7uXFfG0O5w9TgvU8esZwgORKrF/BLJ4yjALlc06TGKPHUS0EUnwBoAXzUXcIpRrYoh21/RgKqnLOhfqXoQzpPl8wndc1VY2V+x7z/D1GNAUCqxjGID0WAeBUj/7TJtBEw8yme/jaqG9InM71Fhm4pktGMrS+5otneDirN3RYTJQ/HGFBQpV2T4xKuiR40OPUjzwqZzVwX1H8lMyvpkyWNdvZPzWZ7xvWwANBsOcZVuuPconFn7oD56fc+v6bzRTX8A0dVw+mSg=='),
  ('id', '62690b743d7366aa'),
  ('id', '364243'),
  ('captcha_challenge_field', 'B4E479DA43B380CD5B1BCCB5190FFDB9262BEFAFBA9166CA15EE99CE6C893C6D845D9EF256344953358C085648817F46'),
  ('manual_captcha_challenge_field', '7yatp'),
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
for i in range(267281, 400000):
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

