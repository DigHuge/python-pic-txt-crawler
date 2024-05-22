#!/usr/bin/env python
# coding: utf-8

# In[10]:


from urllib.request import urlopen
from urllib.request import urlretrieve
import urllib.request
from bs4 import BeautifulSoup as bf
import os
from urllib.parse import quote
import string
import requests

original_url = 'https://www.v2ph.com/album/YTY-693'
address = 'C:/Users/LZH/Downloads/' #存储地址
proxies =  { "http": "http://127.0.0.1:7890", "https": "http://127.0.0.1:7890", } #代理服务器
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
           'Referer':'https://www.v2ph.com/'} #浏览器信息

cookies = {
    'fpestid':'zpaXrw-mV89PNvlI-cFJYqNOslXiKlX_gllfVcrJ8xzUhj4JY3LoNmoeZRjk3SCHUyD_IA',
    '_gid':'GA1.2.496627508.1659686846',
    '_ga_170M3FX3HZ':'GS1.1.1659692359.5.1.1659694296.59',
    '_ga':'GA1.2.1961013052.1653620642',
    '__cf_bm':'7S3VmuWfUXqlUHwU_iALNjP_tJ6dtx61aIOeyk_2Op0-1659694122-0-AVWAN1Wmt+TxUonk8qgN9sqcJyiTTx/N7QikT18kGWlUBkpVXu9IIVSj/u/CT1yFjHBRDg9RMFjfbnoOP6khQVSyLMYuoP2vu9ZtEbyI43WZI3Fqi1pBYzzcNn1tD/XyIg==',
    'frontend':'76b22f52565dbca44cb85f524df61727',
    'frontend-rmt':'nx%2FCvRlTjrF9BqezmsxtB4TvgVXMNyaU8fAPiZ1EJMO2o%2BY3DSwMft2necg4xF%2FR',
    'frontend-rmu':'VaH3HHC0AfEJ9H8VFMTMTXQNgzTo'
} 


# In[11]:


sessions = requests.session()
response =sessions.get(url = original_url,headers = headers,proxies = proxies,cookies = cookies)
#print(response.text)


# In[12]:


obj = bf(response.text,'html.parser')
file_name = obj.h1.get_text() #获取文件夹名
file_path = path = address + file_name + '/'
if not os.path.exists(path): #若不存在，则创建
    os.mkdir(path)
stop = 0 #停止爬图参数
x = 1
for page in range(1,1000):
    if (page == 1):
        URL = original_url
    print(URL)
    s = requests.session()
    response = s.get(url = URL,proxies = proxies,headers = headers,cookies = cookies)
    obj = bf(response.text,'html.parser')
    pic_url = obj.find_all('img', class_='img-fluid album-photo d-block mx-auto')
    for i in pic_url:
        pic = i['data-src']
        r = requests.get(url = pic,proxies = proxies,headers = headers,cookies = cookies)
        print(pic,end = ' ')
        save = os.path.join(file_path,'%s.jpg'%i['alt'])
        with open(save,'wb') as f: #存图片
            f.write(r.content)
            f.close()
        print('done\t %s'%(x))
        x +=1
    #判断是否有下一页
    next_url = obj.find_all('a',class_= 'page-link')
    to = len(next_url)-2
    new_url = next_url[to]['href']
    if(stop == 1):
        break
    else:
        URL = 'https://www.v2ph.com' + new_url
        #已知该网站倒数第二页的页码分布特点为：最后两个页码链接一致。
        #故在爬完倒数第二页后，赋予最后一页链接的同时，激活停止爬图参数(stop=1).
        #这样就可以在爬完最后一页后，停止爬虫了
        if (next_url[to]['href'] == next_url[to-1]['href']): 
            stop += 1
print('All done')


# In[ ]:


temp = (obj.find_all('a',class_= 'page-link'))
print(temp[4]['href'])
for j in temp:
    print(j)


# In[7]:


print(i['alt'])


# In[ ]:





# In[ ]:




