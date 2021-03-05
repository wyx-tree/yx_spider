
cookies = {
    'HMACCOUNT_BFESS': '98606595895E1C2C',
    'BAIDUID_BFESS': '32E8EFF771C1D3601D855D6311D9C98F:FG=1',
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
    'referer': 'https://www.315jiage.cn/n171487.aspx',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': '__cfduid=d28e514d3b45380fb95958c27498274c11613642406; iwmsGid=0FVZL399S8DAZVXFHT4S; Hm_lvt_4cce664ec5d8326cc457ab09053c15b2=1613642407,1613642563,1613973475; cf_clearance=f22347c6964411f83ead2b3f1ec6144a4d2dc7a8-1614320772-0-250; rtv=52A57B,8207652; Hm_lpvt_4cce664ec5d8326cc457ab09053c15b2=1614332577',
    'Referer': 'https://www.315jiage.cn/n171487.aspx',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
    'Connection': 'keep-alive',
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Dest': 'image',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'x-requested-with': 'XMLHttpRequest',
    'pragma': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.315jiage.cn',
}

data = {
  'cmd': 'logVisit',
  'id': '171487'
}



proxyHost = "http-dyn.abuyun.com"
proxyPort = "9020"

# 代理隧道验证信息
proxyUser = "H5UWW33P9X0EWXWD"
proxyPass = "8F486DBEB580CBCB"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}

proxies = {
    "http": proxyMeta,
    "https": proxyMeta,
}