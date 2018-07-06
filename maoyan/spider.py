import json
from multiprocessing import Pool
import requests
from requests.exceptions import RequestException
import re

def get_one_page(url):
    try:
        # 反爬虫 浏览器参数
        headers = {
            # 'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
            # 'Accept - Encoding': 'gzip, deflate',
            # 'Accept - Language': 'zh - CN, zh;q = 0.9',
            # 'Connection': 'keep - alive',
            # 'Cookie': 'td_cookie = 3791400249;uuid = 1A6E888B4A4B29B16FBA1299108DBE9CD9C4EFBDEC8BF1DF28F414391B1156DC;_csrf = 152b784f5dcd9c787145e2c392d53fa3aa2423468df652c21c5857afc02c2ed5;_lxsdk_cuid = 16464516a7b91 - 0dc2e3137a6244 - 5e442e19 - 1fa400 - 16464516a7cc8;_lxsdk = 1A6E888B4A4B29B16FBA1299108DBE9CD9C4EFBDEC8BF1DF28F414391B1156DC;td_cookie = 3791016260;__mta = 54296087.1530691414887.1530693048436.1530693539122.33;_lxsdk_s = 16464516a7d - fb7 - 1e5 - 3d8 % 7C % 7C80',
            # 'Host': 'maoyan.com',
            # 'Referer': 'http: // maoyan.com / board',
            # 'Upgrade - Insecure - Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)  Chrome / 67.0.3396.99 Safari/537.36',
        }

        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5]+item[6]
        }

def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()

def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    print(html)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    pool = Pool()
    pool.map(main, [i*10 for i in range(10)])
    pool.close()
    pool.join()