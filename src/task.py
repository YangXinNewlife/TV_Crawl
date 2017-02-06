# -*- coding:utf-8 -*-
__author__ = 'yx'
import urllib
import sys
import urllib2
url = 'http://www.tvmao.com/program/CCTV-CCTV1-w8.html'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
#values = {'username' : 'cqc',  'password' : 'XXXX' }
headers = { 'User-Agent' : user_agent }
#data = urllib.urlencode(values)
data = None
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
page = response.read()
file_page = file("C:\\Tran\\a.txt","w")
file_page.write(page)
print page
file_page.close()



