import requests
from lxml import etree

from pymongo import MongoClient

client = MongoClient('mongodb://root:123456@172.16.10.136:27017/')
db = client['spider']
collection = db['result']



cookies = {
    'HMACCOUNT_BFESS': '98606595895E1C2C',
    'BAIDUID_BFESS': 'B583E88F61A0F53325F7BAB499A2194B:FG=1',
    'ab_sr': '1.0.0_YmQzYzFiZTBjODBkNzUyMWI3ZGI5ZWU4ZDc3MjhkNDFiNWQxYjc3Y2I0NjViNjcyNzI2N2Q4NmVhYjE5ZWI5MGE0NjNjZTU5ZGY0ZTZmYTkwZWMzNjJiZDc4YjdjZmJi',
}

headers = {
    'authority': 'www.315jiage.cn',
    'cache-control': 'no-cache',
    'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
    'origin': 'https://www.315jiage.cn',
    'content-type': 'application/x-www-form-urlencoded',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'image',
    'referer': 'https://www.315jiage.cn/n364243.aspx?__cf_chl_captcha_tk__=cbda2ef9a0128a0e132010464c0636eed4b908a3-1614237585-0-AUIG8x4k1h2sv3KVqeNf--NdChKCDWqPjzxkKkPOCOCXbnD8IYgq3SwB7kCadIDZrcFELkWLRTqIFQYyJlU1zvzSt1-ZRmWkk0tTWXFX8WZ6Clm8U0auNxjTi2Esf-IfY4WhMXekXhkaMIQ7rpSK3yPs3txhzixf9LRnFuDPZKOE18zBF4WPS7B8kT4qouriRzvwd5yMLE_RFx5vHLiw9A8QUVpNi-ZrOmoN84jKLyiApmG3h8YmbO1MVqirICxJan3oV1w_FN6wTbKObK-p6bqDmW2vdyqoPFVcpugH5W1pJBtFrPaFb8sO8PjYgYL-5P3bE7lqHMsL8BbGMsJOL4xLsDcp8CX2fNDZsZulD52r',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': '__cfduid=d28e514d3b45380fb95958c27498274c11613642406; iwmsGid=0FVZL399S8DAZVXFHT4S; Hm_lvt_4cce664ec5d8326cc457ab09053c15b2=1613642407,1613642563,1613973475; cf_clearance=6393cee43d181fdeef52e9a84999a07bddcabd81-1614237595-0-250; rtv=529F61,18341662; Hm_lpvt_4cce664ec5d8326cc457ab09053c15b2=1614237614',
    'if-modified-since': 'Wed, 03 Aug 2016 03:53:40 GMT',
    'if-none-match': '"b719299f3aedd11:0"',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Dest': 'image',
    'Referer': 'https://www.315jiage.cn/n364243.aspx?__cf_chl_captcha_tk__=cbda2ef9a0128a0e132010464c0636eed4b908a3-1614237585-0-AUIG8x4k1h2sv3KVqeNf--NdChKCDWqPjzxkKkPOCOCXbnD8IYgq3SwB7kCadIDZrcFELkWLRTqIFQYyJlU1zvzSt1-ZRmWkk0tTWXFX8WZ6Clm8U0auNxjTi2Esf-IfY4WhMXekXhkaMIQ7rpSK3yPs3txhzixf9LRnFuDPZKOE18zBF4WPS7B8kT4qouriRzvwd5yMLE_RFx5vHLiw9A8QUVpNi-ZrOmoN84jKLyiApmG3h8YmbO1MVqirICxJan3oV1w_FN6wTbKObK-p6bqDmW2vdyqoPFVcpugH5W1pJBtFrPaFb8sO8PjYgYL-5P3bE7lqHMsL8BbGMsJOL4xLsDcp8CX2fNDZsZulD52r',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'If-None-Match': 'e20946816f7a56ad5f166b26e3ccfff5',
    'X-Requested-With': 'XMLHttpRequest',
    'x-requested-with': 'XMLHttpRequest',
    'pragma': 'no-cache',
}

params = (
    ('__cf_chl_captcha_tk__', 'cbda2ef9a0128a0e132010464c0636eed4b908a3-1614237585-0-AUIG8x4k1h2sv3KVqeNf--NdChKCDWqPjzxkKkPOCOCXbnD8IYgq3SwB7kCadIDZrcFELkWLRTqIFQYyJlU1zvzSt1-ZRmWkk0tTWXFX8WZ6Clm8U0auNxjTi2Esf-IfY4WhMXekXhkaMIQ7rpSK3yPs3txhzixf9LRnFuDPZKOE18zBF4WPS7B8kT4qouriRzvwd5yMLE_RFx5vHLiw9A8QUVpNi-ZrOmoN84jKLyiApmG3h8YmbO1MVqirICxJan3oV1w_FN6wTbKObK-p6bqDmW2vdyqoPFVcpugH5W1pJBtFrPaFb8sO8PjYgYL-5P3bE7lqHMsL8BbGMsJOL4xLsDcp8CX2fNDZsZulD52r'),
)

data = {
  'r': '7f472e2e0b1ed15f64eb3c9b81d3b4134c01108a-1614237585-0-AdBA/qYECgFU/vkunOVNFtVVi1Fvv+4tO1vMuvI+/B7HaYQ5tfhJa5BVet9i7d9CM/Fe0ORnJiA3vLe/B7+nWRq1JjUJPXQwD+sHuzwkoTRV6/m92wEb3G2HH6V4FXdsbAjcQxVOAzBK/h9JsmOLwj9NjdXSaPFbvWM+tGEOLHj+oYTteOooraoFpAW6WGafwF2MOc/J5p8J9O0M6yQ1LaFE9sL76beSn/WR5GU+RUzzaorMZYLa2cqGdXqZqs9GJKojtWBeuwLCB8gwcZzkmp7PG2C+U4ala2+iWJnXFIXIAnWfskIWECCuCvjDi7LOXGykjKgoPbsxNJS4spuTtrlJzAYHvGNmvHHxyLjQUv3u18NTJWIeJArFno2bpkAYKJtvsPaoE082t7Y3BSQY9Wi8zwL2GkHgAfgoOJUZ/zbPE5s0JVsmgH4RNHVaiN61pHlIfL0v5S6iVqorzeC5jbGgNMTsCt4C9FnXSQ7urc8MpiE/t9iVGt/47tSw+S0GB3NWp2oyAae4/bnMyWNwZ7fkzQ62szpIci+WQdVmQfyJgrFwtCvGtUDz4n925rOaODgpdGrQOgwaXy/RjJHuWv+K2NrROMib0fuunlZrEPBX3FQ7DVoCoqLPnTxVYA+WnrQ4yY+WifjwwArIN+npCgFQ63ryqrtABQtVUoOlSIo8YnkPSg7x3mC5/6Q2+n/S8lkrNO4KWKrduOGiuuhV5z3y1aA9rlNHyDh5yHrkEeoOwa6pwT0aoP3EtBTwqXAnHrATrAcZnNaD0bawOF6suxjKL+biGHqxKSG99BTMiJFyya0ZORW6qZ6YqBW5w+6d7psZTxgMNy90y2yQoKVb7SnjnEkHgq0iEg8WTt4nXfrReLs3gjuPQx/MyWA7+Fp6AAqn9tHRWvik7ma+DnZAF3X2eQ9TqKUNw57p7C62kQqocoXliyo+UXq5s2VxSvKB0sxfvIVcSAtH9fNO7MYQ8zCxt1WApRXXkE+KutUcnMiqn7T+tXqJKUGMY2hQQ1scG8d12pLloWtlVCrOhIZmDZ++OZuvoNU+HIFeI6zM719o/aSnJgmmQsMiyJVgOr0lM9017SB+JU73F57mKDfGsfFschDwsdbiHjMpKfjyuA5N9Hdl+JgOHcsghfViZc+ouMgDStb8KvS9lPEFO3hOqMJtMqIA2AntsBygiPqh3Pj45ztbWxjbphVC+PFVsDcNgcyhUi/uHfUXcY0bq2flBpu8jJR1alKMixr04eW9zYryTOBdPG6E45qbUXttpo7qRuPT9YncAPjgQNEhtcQHGcEIyvfV1HG2Ri/UE1VXQAg06pvhsjV15E5HYkadFI1q3ACIqNiD5padJLSBNTxwrhjOk9khBiyHEAdU/4oH1rCvzqacrP3FObd9lNM+dVi7UO7F9aldD7bEsOD1rTK27wrKcQYIzt6dVfHKsssTOOImKIeFb6Ql4c9jMQcbFHiTpEmGIlBeA+FVOMk+m6SkXWqfzgFr5G+DS+7fzw3sj/+nxOOlC0fpz/VwTv5eBM0mq5mzsdhysj9ZUwsejblbRTD8HlldO7OIfgK2JQZwzdYyPbFjhIWjBc5Z+BmCnCw+Zaqdg2VLM0WNbUHY66jVb2GcTAGVD1/8EUJXrPITTNiLids6B1CoH8JaLaff4ttwM6PeAro/B4NPwIqUl1vnvd5z6PhhWk4N97XY2SJgucfJzK3OTG1Nu0/dKX9GWxNcnKzZhab/jw+TakmL0IabecbagLZ8yFQ2E8gMoNNIWn4meZnVEfdANF0ASvMDDVXbicUvqzpKnKlddv89edEKFBdN891DYqGn72YORqyPR8zSPUD5wMtmWcmF93IRmeHo+cvZSYoGW5syMSqLe92RwCQi8PoS0MKiZsfbImteF4+OKd7Cj3K9dkTDHqj8oZ4JP0IHG1R1YFD4J0XGqlZ/gz8bXwM7AtI4TSVUVZ6L67yqJulVYiJ5vNqCqylwabHaFWnn3S5rKSWx9E8Z8ykU5Hg7YH079y0w5yE1kC9KOPGID5PR5xElPPjfBPPNzq2PuDxJwVV4j7KY2/X4otWFwgozzlDM9N4nn+YvMs7BuZrSEltSEERTs+gYc/eSRuEzLBsMyb3KefiUyQfSgwH3xuYHHSmIJEYI2VAAc1g/pbebh1ruR9R2MoIk00rRotyaB+2v160lGcjZ/cw1hTEitMz8msNTtkh58+B02Ho7VccpvWhGmmadQJEMWz7hG2twAV10OncWekgVlhS0nGH3rvyDDFR8XdR3kWkteUYH6BYIPHXmrZUSKwELraaIzS8ZMtnqI6cRc2InNqU4Mwdi5jzQB1CrbsV2lfOCyaFTpxzEkDvAqVjR/u7DQR1neHA373qtNCUwKUcWvVtbNPUjHDTObWp/IV0GaOkvJjhBA17wKnsCTIYorYqKrRq1D411f3V/s0xf/LgQ1ViiaM8JdE/o6xmo0Cgga0F6/MGpaFncisa5oZ3Q8FQeBUd/rcgducsGHdCgzG9EN4maq9fyfe0wA7BGNJ5R1LPKPW+5tEmotyugMqBg7lOyperNxxejxmLyarm8iLNOO7zTE2onfGoPUTaLRzD+SiS/qFDrp4ml/raGXUg69otophVp1E1SZVOelZl6flbWL/PpTw1ekV4rQeIG/bjkSxLjl2s2cNhRPRBK9UgOj5slL8anoyMP6LGHMtgJ2DClOq2TzLVFavEiODXG04WDHOzj8mis1y5eCyCroBQ3FRzU0yHaTvKXY3y/bBF6kWcFL4+9QG/Ldp+VekWiTb9nHaFhdqRRGmLf+PgcZpqwXLzm8WFH/AvPtAZRdBI+W1fLtDi5Gain+DZp1n/KfIk7n0VGAub2Bxno1/gvFvT61wSyw5nL1oT1An1egLWfYY/lrbO8hcNsAVBgIlyABpHAqBjHfxOn25Nsl0UPSwedqHJDYdBDGQeIEDv2r2B7jPdArZutgQmc6SmeRGhrL0ih+4NToEC2S2aDViLN7Vh6iKO4LaEsjgAq7njdTtGTyqacgPbuTd+0O3bfkUSmWW0AKADLPkxlXYI6hDbZiuW6umbyLMKGScyFtIEMTptXIG1yKhUOOt56HzdOw1k57HKQHdDgLEuNWytSBiKvIq0iurw5dPIcOd2k3dSOBMraHyF2Z4AeKb56Da0ae7BHNgPexrDQMmvWkH9ucN9/WG9aHpVANtXQZYfFtovy0uHT9Z5Cy+q8jW3EdnppQMeJPxL6kXmnCrNdV/1KXRIAS2tB/CAumV51mTUtwBTLM7yg5BZHG3Pslj6dQ63FZLm9yvRKXKkxcCQbe7Rcr5bLOTX0h7WbGTiw5r6Cm1viBZIORGIqsPk5WQLhkchFaZCKWKK0w4xqVjjm3y9EDhBv27fgmwKx0Ap+uBNblA/zOeH+dVNjFa/YYj18Jv/+hJG957FR1jeH/qW0rvZIQ9FP5CQA9QM8m3lMhW/MAjt9+JqRBNdbzX5JioRzQJhWJIVVkgFrtZrwXB2SbSyygs9AAntaqsIBIggryQRZ9plfrmtvahYANfVocTW6Iw9JS1QmgBC+VWJYsC24d2eQUk/dNe9WdPFzmkGVJnpr6O2rVCjmhGo4GlPGn11tXjgkA52JSCN+4I/ytEubO2axe5X1qZy1wDBfJD6t6yyVj/zt6aUoBRsyguhhNIxeinsx5mguLoVpaKyyf26o7zBVfZEImQYK0mPd5vgi1LXAwbMj/JigLZk2gayu+0IiUFRye+tfSFq9OQ/qWftQUAAsGXhD8LILVf1Ud1Kb1X81QZW1av3z0vaKpKumoUiN8oan3EIKtfAyD+egHf0Ssmw3y20pRaFVHZ4JiMlNkNMJ0yK7lD/U6xx9j/XK9o7Kv2ruP1yRM6Px3B/d6w7YYe0v1vXymbNlQbJgTpoSnnKZ9qwZKLQdn0HI6saIVPQRY7RFL7zefKual+pVJCad4iF5Zs9N/RgI3MMxIZvGrAjCZKzn8MTWN5mvqK9ymFbrcorvQGP95ULvTZEr6tf0GHps1OlTcMrWRauc0/h0Yxvr3rN4a1stuOz8HWl7hrtnGafp21zJIN/OqB2xQu7pDaNUhAu6e5aHIzYIcAqqUSKgxTsOr0S7ZOd2zd0qcbq2gX5EPZD4ypIi0mkElnV1cbtvI7s/gBFT/V7M3dTTNMJrIoHpjYruInXqerE18qiLC5gEBkUHTAob3Gn/z5lPQl2ImnigMGIEBbSm/RHWF1caRWLFH6Drvi1l3rMhNk476iqiHv9a31Wdf8WFpFAOpRU68Sxu+EbXIezImiFvCsOnVYerWryi2qSZ3UYbmufezKH69XJz0wgf9StF+2G5ghGlLx9FJQ4YJ6DO5qmhKfydIT8WJZuFFKszq1vVaAX2Zpj9bEejLc0vkPeD4i8eQmq1EJp+wSvlHLmV1/pf2z3zJ9RnSAQm6o7/nBQNXIp5cb0Lvu32/r7zA9wHtN9/B+WkOVr6MuWh0rff00RWUIr5wuo4u5aKnvwSOYeMnMJ0aqTjDG+v642vlfJo0RT23vYUS3LN/7NYXfNS2vVAgMZ5wPvDJwtKp4WdF3n2QpWjm7bp2H1UepLPnZrsdR+Bp/9QSqDV9p2oJK+wWun67zU3tq4oehRzTxQf2mPe0awJIPJUtENPa4F0LAqiEgFqQBJ8xcug0CatoF/Yl9r5vXQ9YvdxV8baf5+Wqd1CTTT0hCPcvBKxF76u257h8PdPRvkW6hHyZMpBEHEihMePTN8K0WjIfyDFUlPWoULqNJX+X2uVpH0kYwYPkw7czSJ2259d3/Lfdn7rVzHLl2JZ9rJvF1lxmaUFazXCKjsUrl4ShX+PsXIT/XP5BpQcell+qi8JcjnLoBLGvB1bFUj9GxqqXCoAXQSPNRPq40N23d/tTYJawIbd5dAG2e5vCYXxx677U8dV7KvNCGxpA3hO9L5tRAAWlXdbGsb+szCjNcHVePQ0Q/YOh3t5/w0rnq9pzYqqpPEk0Ao1Lw2zzSx3dM9PzdVUEN5bWBraiSJnGCkH63OmPVx2bdSrTgXRd53JeJEqNV5lgBqhYV5YDHBezhGUkKCOJnzfamGAWYnvlKH9lowSlOQUZ+D285JlNpFqbJUwY9pF0XQtSUiVZn9wXEsqtBhj7QW5AyWkO4kstCrjjEMR31BHGgUYSZ1+m8CbNsPZl4zOKycY/8pbWc27O+Lc+KwuxaJV4AoCrTKtKbJXEYOkXbzF0ob/A7ggL4YoXZC9xIta/MBEMziZLJ/OfDkjMEzNT/O5Mf4F9FKikfsvbfIa9Wp+e6jYJSyWxwtVKj+Y+DP7KpSYMGn6H4E/P9N+EYg4V5chhvMZQhTkRMvBjOCXikjmNqPy9QxvhFPJw28tvrTzcUdLiDwYS57XX5h7OK/cTisRHOZoQin4iGQK0EmbHXOLLMUllQoRxwh6EwEWSTCAAuC7yY2JweO2m+fEJ0cRU4hwr9ULLwc9B3VlP4sq3Uu70iWuV4WxrdDNBlNTsx2XjiC0+OpM6ifieGJHZoRsF2f4G6GW/FAcm4oNLzL7LKxI3J9ouyTEwbXOyfo1LbBwfvVU+Xp8XK3DV33i2xZ2Q4nW7iA/RWx/AO7VIRXMRdTi5ZIGrTJWNuu4qqBLDaop83xap/yt1wab1gGZqg==',
  'id': '626fa8ef59dd66e0',
  'captcha_challenge_field': 'E9C273E9A377E62FBD0A7496E5F18FC1AD9BE3C6D193394CF658301B628855EF3CA920D0793A0DDA2C7D20A5D97DCD1F',
  'manual_captcha_challenge_field': 'hegrxy'
}

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('https://www.315jiage.cn/n364233.aspx?__cf_chl_captcha_tk__=0abb4a9aea84c6ee33363acc04397fffefcadff0-1614130863-0-Aeq-nGjXogvMxWsQtCOzKevQ7Yt8QbjYh-RnoR9OYzkKP4y3Mbnb9OZHEoFaOd6_nQDuDCDpfkzj1c2n4OI3VXHrxzWA14ftOOHSg6ecY-aIRmZVUPMKUch5yw90wclpJcmDYpn-NpxWV-gEeJj5zBpORDkKiirrjOf778ubq4StdEnJzVsxfchDbWJmNssoDAhIReRZ0cnrJhnl-RwMJ-k4LRH7vPR80DqOXF6IbzCP4sUyn0X13oilM_zf4N3ytUYkVLO9k6uFOSWFRqS1WDz7w4KWo7X2_-KrzQl3Xaa_Hjf3NmsrR6N5Iau2yi6PpS_ueoT5Ypne6wYsBc0fniqCuHTxa9OVcMsRiI_WyPUs', headers=headers, cookies=cookies, data=data)


# url = 'https://www.315jiage.cn/n325021.aspx'
# url = 'https://www.315jiage.cn/n327184.aspx'
# url = 'https://www.315jiage.cn/n134488.aspx'
# for i in range(2000, 400000):
for i in range(311585, 400000):
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

