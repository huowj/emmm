
# coding: utf-8

# In[1]:


import csv
import requests
import json
import re
from bs4 import BeautifulSoup


# In[120]:


DOWNLOAD_URL = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%8D%97%E4%BA%AC%20%E4%B8%8A%E6%B5%B7%20%E5%90%88%E4%BD%9C%20%E5%8D%8F%E8%AE%AE&rsv_pq=c6202f920002cecc&rsv_t=bd66f0Ke4bcHlYVEz7EItNpT8ViYQL1cX5ox8SbDv2nZgJEQoRBkd%2BrMHqg&rqlang=cn&rsv_enter=1&inputT=7584&gpc=stf%3D946656000%2C1514649600%7Cstftype%3D2&tfflag=1'


# In[3]:


def download_page(url):
    return requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }).content


# In[4]:


url = DOWNLOAD_URL


# In[5]:


html = download_page(url)


# In[6]:


soup = BeautifulSoup(html, "lxml")


# In[7]:


pc_list_soup = soup.find('div', attrs={'id' : 'content_left'})


# In[54]:


page = soup.find('div', attrs={'id' : 'page'})


# In[51]:


res_list = []
for search_li in pc_list_soup.find_all('div', attrs={'class' : 'result c-container '}):
    row = []
    h3 = search_li.find('h3', attrs={'class' : 't'})
    a = h3.find('a')
    res = ''.join([str(i).strip('<em>').strip('</em>') for i in a.contents])
    ref = a.attrs['href']
    row.append(res)
    row.append(ref)
    res_list.append(row)


# In[55]:


page_list = []
for page_li in page.find_all('a'):
    page_list.append(page_li.attrs['href'])


# In[127]:


res_list = []


# In[142]:


url = DOWNLOAD_URL


# In[143]:


if url:
    html = download_page(url)
    print(0)
    soup = BeautifulSoup(html, "lxml")
    print(1)
    search_list = soup.find('div', attrs={'id' : 'content_left'})
    print(2)
    page = soup.find('div', attrs={'id' : 'page'})
    print(3)
    #print(search_list)
    for search_li in search_list.find_all('div', attrs={'class' : 'result c-container '}):
        #print(search_li)
        row = []
        h3 = search_li.find('h3', attrs={'class' : 't'})
        a = h3.find('a')
        res = ''.join([str(i).strip('<em>').strip('</em>') for i in a.contents])
        ref = a.attrs['href']
        print(res)
        row.append(res)
        row.append(ref)
        res_list.append(row)
    page_list = []
    for page_li in page.find_all('a'):
        page_list.append(page_li.attrs['href'])
    url = 0


# In[166]:


res_list


# In[167]:


for i in range(1, 76):
    url = 'https://www.baidu.com/s?wd=%E5%8D%97%E4%BA%AC%20%E4%B8%8A%E6%B5%B7%20%E5%90%88%E4%BD%9C%20%E5%8D%8F%E8%AE%AE&pn=' + str(i) +'0&oq=%E5%8D%97%E4%BA%AC%20%E4%B8%8A%E6%B5%B7%20%E5%90%88%E4%BD%9C%20%E5%8D%8F%E8%AE%AE&ie=utf-8&rsv_idx=1&rsv_pq=e0a2e6e10001f805&rsv_t=df3cuHXAbGvwR2vBlY8rK14gSk8g8%2Ba6xUOqEz01WxNGuesf1R9mqoGuUQ8&gpc=stf%3D946656000%2C1514649600%7Cstftype%3D2&tfflag=1'
    html = download_page(url)
    print(0)
    soup = BeautifulSoup(html, "lxml")
    print(1)
    search_list = soup.find('div', attrs={'id' : 'content_left'})
    print(2)
    page = soup.find('div', attrs={'id' : 'page'})
    print(3)
    #print(search_list)
    for search_li in search_list.find_all('div', attrs={'class' : 'result c-container '}):
        #print(search_li)
        row = []
        h3 = search_li.find('h3', attrs={'class' : 't'})
        a = h3.find('a')
        res = ''.join([str(i).strip('<em>').strip('</em>') for i in a.contents])
        ref = a.attrs['href']
        print(res)
        row.append(res)
        row.append(ref)
        res_list.append(row)


# In[172]:


len(res_list)


# In[148]:


page_str = 'https://www.baidu.com/s?wd=%E5%8D%97%E4%BA%AC%20%E4%B8%8A%E6%B5%B7%20%E5%90%88%E4%BD%9C%20%E5%8D%8F%E8%AE%AE&pn=' + str(2) +'0&oq=%E5%8D%97%E4%BA%AC%20%E4%B8%8A%E6%B5%B7%20%E5%90%88%E4%BD%9C%20%E5%8D%8F%E8%AE%AE&ie=utf-8&rsv_idx=1&rsv_pq=e0a2e6e10001f805&rsv_t=df3cuHXAbGvwR2vBlY8rK14gSk8g8%2Ba6xUOqEz01WxNGuesf1R9mqoGuUQ8&gpc=stf%3D946656000%2C1514649600%7Cstftype%3D2&tfflag=1'


# In[154]:


page_str is ('https://www.baidu.com' + page_list[2])


# In[155]:


page_str


# In[159]:


'https://www.baidu.com' + page_list[1]


# In[160]:


page_str is ('https://www.baidu.com' + page_list[1])


# In[164]:


d=difflib.Differ()
diff=d.compare(page_str,'https://www.baidu.com' + page_list[1])
print(' '.join(list(diff)))


# In[173]:


import pandas as pd
df = pd.DataFrame(res_list, columns=['res', 'ref'])


# In[177]:


df.to_csv("result.csv", index = False)

