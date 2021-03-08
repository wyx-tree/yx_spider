from pymongo import MongoClient

client = MongoClient('mongodb://root:123456@172.16.10.136:27017/')
db = client['spider']
collection1 = db['result']
collection2 = db['t_medicine']


class GuanLian():
    def __init__(self):
        self.count = 0

    def spider_data(self):
        for i in collection1.find({'is_crawl': {'$exists': True}}):
            if i['commodity_code'][0] == '6':
                self.origin_data(i)

    def origin_data(self, spider_data_dict):
        '''
            思路： 先找出与爬虫数据公司相同，国药准字形同，没有69码的数据，如果有，则继续。
                    接下来判断，爬虫数据公司相同，国药准字形同的结果中有没有已经有相同69码的，如果没有则继续，有就不继续了。
                    下一步的关联规则，是去处理爬虫数据中的guige字段，先处理的是'guige': '0.25g*30粒'这种数据类型的，
                    用这个数据与元数据中的pkg_strength和strength去比对，如果相同，则关联成功。
        '''
        crawl_guige = spider_data_dict['guige']
        approval_no = spider_data_dict['approval_no']
        company = spider_data_dict['changjia']
        commodity_code = spider_data_dict['commodity_code']
        result2 = collection2.find({'approval_no': approval_no, 'company': company, 'commodity_code': None},
                                   {'approval_no': 1, 'commodity_code': 1, 'company': 1, 'pkg_strength': 1,
                                    'strength': 1,
                                    'generic_name': 1, 'commodity_name': 1})
        if result2.count() > 0:
            result3 = collection2.find(
                {'approval_no': approval_no, 'company': company, 'commodity_code': commodity_code},
                {'approval_no': 1, 'commodity_code': 1, 'company': 1, 'pkg_strength': 1})
            if result3.count() > 0:
                pass
            else:
                crawl_list = crawl_guige.split('*')
                if len(crawl_list) == 2:  # 先处理有一个*的情况
                    crawl_strength = crawl_list[0]
                    crawl_pkg_strength = crawl_list[1]
                    for a in list(result2):
                        origin_pkg_strength = a['pkg_strength']
                        origin_strength = a['strength']
                        if origin_pkg_strength == crawl_pkg_strength and origin_strength == crawl_strength:
                            print(spider_data_dict)
                            print(a)
                            self.count += 1
                            print(self.count)
                            print('--' * 50)


if __name__ == '__main__':
    a = GuanLian()
    a.spider_data()
