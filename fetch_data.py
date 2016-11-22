# -*- coding:utf-8 -*-

'''
curl -i -H "Accept: */*"  -H "Referer:http://www.sse.com.cn/assortment/stock/list/name/" "http://query.sse.com.cn/commonQuery.do?&jsonCallBack=jsonpCallback94934&isPagination=true&sqlId=COMMON_SSE_XXPL_CXJL_SSGSGFBDQK_S&pageHelp.pageSize=25&pageHelp.pageNo=4&pageHelp.beginPage=4&pageHelp.cacheSize=1&pageHelp.endPage=41"
'''

import re
import requests

def fetch_managerial_holding():
    url = "http://query.sse.com.cn/commonQuery.do?&jsonCallBack=jsonpCallback94934&isPagination=true&sqlId=COMMON_SSE_XXPL_CXJL_SSGSGFBDQK_S&pageHelp.pageSize=25&pageHelp.pageNo=4&pageHelp.beginPage=4&pageHelp.cacheSize=1&pageHelp.endPage=41"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
            'Referer': 'http://www.sse.com.cn/assortment/stock/list/name/',
            'Accept': '*/*'
            }
    r = requests.get(url, headers=headers)
    rex = r'^jsonpCallback\d+\((\{.+\})\)$'
    a = re.match(rex, r.text).group(1)
    print(a)

fetch_managerial_holding()
