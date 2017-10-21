# -*- coding: utf-8 -*-
'''
Created on 2017年8月3日

@author: YHui
'''


class UrlManager(object):
    
    
    def has_new_url(self,new_urls):
        return len(new_urls) != 0

    
    def get_new_url(self,urls,count):
        url = urls[count]
#         urls.pop(count)
#         如果是不定链接的爬虫，即可能从新的页面中进行URL提取，则要设置另一个set来储存已经爬下来的链接库
#         self.old_urls.add(url)
        return url
    
    
    
    



