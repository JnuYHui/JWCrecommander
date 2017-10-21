# -*- coding: utf-8 -*-
'''
Created on 2017年8月3日

@author: YHui
'''
import url_manager
import urllib2
from bs4 import BeautifulSoup
import re
import os
import time


class HtmlParser(object):
    def __init__(self):
        self.downloader = HtmlDownloader()
        
        self.urls = []
        self.outputer = HtmlOutputer()
    
    def _get_new_urls(self,root_url):
        nums = []
#         url_list = []

        html_concent = self.downloader.download(root_url)
        
        soup = BeautifulSoup(html_concent,'html.parser', from_encoding='utf-8') #
        
        find_list = soup.find_all('a',target="_blank")
        
#         print "find_list: \n", find_list
#         print "find_list: \n", type(find_list)
        
        for link in find_list:
            
            new_url = link['href']
#           num = re.findall(r'ID\=\d{4}',new_url)
            nums.append(re.findall(r'(ID\=\d+|id\=\d+)',new_url)[0])
            
        
        print "共有num %d 个 "%len(nums)
        print "nums: \n",nums
        
        for num in nums:
            start_url = 'http://jwc.jnu.edu.cn/ReadNews.asp?ID=3441&BigClassName=%BD%CC%CE%F1%B4%A6&SmallClassName=%CD%A8%D6%AA&SpecialID=0' #发现去掉'&SpecialID=0'这个字符串,并且不以中文(好像主要原因是中文），可以获得完整源代码,直接爬取下来的页面带有'&SpecialID=0'并且因为getHTMLText改变编码URL中文正常显示，所以得到的URL不能获得完整源代码
#             需要将num中的其它部分去掉，只留下数字
#             只需要字符串截取即可搞定
#             num_id = str(num)
#             num = num_id[3:10]
            
            URL = start_url.replace('ID=3441',num)
            
            self.urls.append(URL)
        
        print "urls: \n",self.urls[-1]
        
#         return url_list
        
        
    def changePage(self,root_url):
        pages = []
        count = 1
        while count <= 98:
            start_page = "http://jwc.jnu.edu.cn/SmallClass_index.asp?BigClassName=%BD%CC%CE%F1%B4%A6&SmallClassName=%CD%A8%D6%AA&page=1"
            page_url = start_page.replace('page=1', 'page=%d'%count)
            pages.append(page_url)
            count += 1
#         print "pages: \n", pages
        
        return pages

    
    def _get_new_data(self, soup):
        new_data = {}
        
#         <span class="unnamed5"> 
#             <font color="#000000"> 关于开展2016-2017学年教风学风分级预警与处置自查和巡视工作的通知 
#             </font>
#         </span>
        
        find_title = soup.find('span', class_='unnamed5')
        new_data['title'] = find_title.get_text()

#         要爬取的内容
#         <P class=MsoNormal style="TEXT-ALIGN: center; MARGIN: 0cm 0cm 0pt" align=center>
#             <SPAN style="FONT-SIZE: 14pt; FONT-FAMILY: 仿宋; mso-bidi-font-size: 11.0pt"></SPAN>
#             &nbsp;
#         </P>
#             <SPAN style="FONT-SIZE: 14pt; FONT-FAMILY: 仿宋; mso-bidi-font-size: 11.0pt">
#             <SPAN lang=EN-US>
#             <?xml:namespace prefix = "o" ns = "urn:schemas-microsoft-com:office:office" />
#         <o:p>
        
        find_data = soup.find_all('p',class_='MsoNormal')
        sentences = ''
        for h in find_data:
#             测试输出
#             print "h: \n", h
            sentence = h.get_text()
#             print "sentence: \n", sentence
            sentences = sentences + sentence
                
        
        new_data['content'] = sentences
        
        return new_data
    
    
    def _get_page_urls(self,page_urls,page_count):
        # 判断文件夹是否存在
        if not os.path.exists("/dir"):
            os.makedirs("/dir")
            print '已经创建文件夹'
        else:
            print '文件夹已经创建'


        if os.path.exists('/dir/urls.txt'):
            f = open('/dir/urls.txt','r')
            self.urls = f.readlines()
            print '读取到的urls: \n',self.urls
            for url in self.urls:
                url = str(url)
                url = url.strip('\n')
            print '修改后的urls: \n',self.urls
        else:
            for page_url in page_urls:
                print("第 %s 页"%page_count)
                self._get_new_urls(page_url)
                print("第 %s 页的URL已经被下载"%page_count)
#                 self.outputer.output_url(url_list,page_count)
#                 print("第 %s 页的URL已经被写入"%page_count)
                page_count += 1
            
            self.outputer.output_url(self.urls)
    
    def parse(self,html_cont):
        cdatas = BeautifulSoup(html_cont,'html.parser', from_encoding='utf-8')
        
        new_data = self._get_new_data(cdatas)
        
        return new_data



class HtmlDownloader(object):
    
    
    def download(self,url):
        if url is None:
            return None
        
        response = urllib2.urlopen(url)
        
        if response.getcode() != 200 :
            print "Fail to get : %s" %url
            return None
        
        return response.read()
    
    




class HtmlOutputer(object):
    
    
    def output_html(self,new_data,count):
        ftitle = new_data['title']
        
        ftit = '/dir/%d %s.txt'%(count, ftitle)
        
        fout = open(ftit, 'w')
        
        fout.write(new_data['title'].encode('utf-8'))
        fout.write("\n")
        fout.write(new_data['content'].encode('utf-8'))
        
        fout.close()
        print("已写入 %d 个文件" %count)
    
    
    def output_url(self,urls):
        fout = open('/dir/urls.txt','w')
        for url in urls:
            fout.write(url)
            fout.write('\n')
        fout.close()




class JWCMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.outputer = HtmlOutputer()

    
    def craw(self, root_url):
        
#         User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
#         
#         headers = {'User_Agent':User_Agent}
#         req = urllib2.Request(root_url,headers)
#         
        
        page_urls = self.parser.changePage(root_url)
        print "page_urls \n",page_urls
        page_count = 1
        
#         self.parser._get_new_urls(page_urls[70])
#         print("第 %s 页的URL已经被下载"%page_count)
        
        self.parser._get_page_urls(page_urls,page_count)
        
#         for page_url in page_urls:
#             print("第 %s 页"%page_count)
#             self.parser._get_new_urls(page_url)
#             print("第 %s 页的URL已经被下载"%page_count)
#             page_count += 1
            
#             if page_count >=71:
#                 break
        
        urls = self.parser.urls
        
        len_url = len(urls)
        
        print "urls: \n", urls[-1]
        print "共有 url: \n", len_url
        
#         把下载的url存起来，省的每次都下载
#         self.outputer.output_url(urls)
        
        count = 1
        j = 1
#         os.makedirs("/dir")
#         print "目录已创建"
        
        while self.urls.has_new_url(urls):
            
            i = count-1
            
            new_url = self.urls.get_new_url(urls,i)
            print "craw %d : %s " %(count,new_url),
            left = len(urls)-count
            print "left: %s" %left
            
            html_content = self.downloader.download(new_url) #下载内容
            new_data = self.parser.parse(html_content) #处理文本
            self.outputer.output_html(new_data,count) #将下载内容输出到文件
            
            count += 1
            
            time.sleep(1)
            
            j += 1
            
            if j >100:
                print '开始休息 \n'
                time.sleep(120)
                print '休息两分钟  \n'
                j = 1
            
            if count > 1300:
                break
            
    
        print "已爬取完毕"
    
    


if __name__ == "__main__":
    root_url = "http://jwc.jnu.edu.cn/SmallClass_index.asp?BigClassName=%BD%CC%CE%F1%B4%A6&SmallClassName=%CD%A8%D6%AA&page=1"
    
    obj_spider = JWCMain()
    obj_spider.craw(root_url)
    
