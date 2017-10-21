#!/usr/bin/env python
#-*-coding:utf-8-*-
# filename: material.py
'''
@author: YHui

@contact: ywhui@outlook.com.com

@software: pycharm

@file: material.py

@time: 2017/8/30 16:47

'''
import urllib2
import requests
import json
import poster.encode
from poster.streaminghttp import register_openers
from basic import Basic
import os
import time


class Material(object):
    def __init__(self):
        register_openers()
        self.getmater = getMaterial()
        self.accessToken = Basic().get_access_token()

    #上传图文
    def add_news(self, text):
        title = text['title']
        thumb_media_id = text['thumb_media_id']
        content = text['content']
        content_source_url = text['content_source_url']
        img_text = self.getmater.getNews(title, thumb_media_id, content, content_source_url)
        img_text = json.dumps(img_text, ensure_ascii=False)
        postUrl = "https://api.weixin.qq.com/cgi-bin/material/add_news?access_token=%s" % self.accessToken
        urlResp = urllib2.urlopen(postUrl, img_text)
        print urlResp.read()

    # 上传一般素材，类似图片
    def uplaod(self, accessToken, filePath, mediaType, name):
        # 官方给出的代码，事实证明不能用
        # openFile = open(filePath, "rb")
        # fileName = "hello"
        # param = {'media': openFile, 'filename': fileName}
        # # param = {'media': openFile}
        # postData, postHeaders = poster.encode.multipart_encode(param)
        #
        # postUrl = "https://api.weixin.qq.com/cgi-bin/material/add_material?access_token=%s&type=%s" % (accessToken, mediaType)
        # request = urllib2.Request(postUrl, postData, postHeaders)
        # urlResp = urllib2.urlopen(request)
        # 和临时素材相比，只是url接口不同
        openFile = open(filePath, "rb")
        postUrl = "https://api.weixin.qq.com/cgi-bin/material/add_material?access_token=%s&type=%s" % (accessToken, mediaType)
        files = {'media': ('%s' % (name), openFile, 'image/png')}
        urlResp = requests.post(postUrl, files=files)
        openFile.close()
        urlResp = urlResp.json()
        # print urlResp
        media_id = urlResp['media_id']
        fmediaId = open("D:\\material\picture\cover\media.txt", 'a')
        fmediaId.write(filePath[26:])
        fmediaId.write('\t')
        fmediaId.write(media_id)
        fmediaId.write('\n')
        fmediaId.close()
        print urlResp

    # 下载
    def get(self, accessToken, mediaId):
        postUrl = "https://api.weixin.qq.com/cgi-bin/material/get_material?access_token=%s" % accessToken
        postData = "{ \"media_id\": \"%s\" }" % mediaId
        urlResp = urllib2.urlopen(postUrl, postData)
        headers = urlResp.info().__dict__['headers']
        if ('Content-Type: application/json\r\n' in headers) or ('Content-Type: text/plain\r\n' in headers):
            jsonDict = json.loads(urlResp.read())
            print jsonDict
        else:
            buffer = urlResp.read()  # 素材的二进制
            mediaFile = file("test_media.jpg", "wb")
            mediaFile.write(buffer)
            print "get successful"

    # 删除
    def delete(self, accessToken, mediaId):
        postUrl = "https://api.weixin.qq.com/cgi-bin/material/del_material?access_token=%s" % accessToken
        postData = "{ \"media_id\": \"%s\" }" % mediaId
        urlResp = urllib2.urlopen(postUrl, postData)
        print urlResp.read()

    # 获取素材列表
    def batch_get(self, accessToken, mediaType, offset=0, count=20):
        postUrl = ("https://api.weixin.qq.com/cgi-bin/material"
               "/batchget_material?access_token=%s" % accessToken)
        postData = ("{ \"type\": \"%s\", \"offset\": %d, \"count\": %d }"
                    % (mediaType, offset, count))
        urlResp = urllib2.urlopen(postUrl, postData)
        print urlResp.read()

class getMaterial(object):
    def __init__(self):
        self.img_text = dict()

    def getNews(self, title, thumb_media_id, content, content_source_url):
        self.img_text = (
            {
                "articles":
                    [
                        {
                            "title": title.encode('utf-8'),
                            "thumb_media_id": thumb_media_id,
                            "author": "yuhui",
                            "digest": "",
                            "show_cover_pic": 1,
                            "content": content,
                            "content_source_url": content_source_url,
                        }
                    ]
            })
        return self.img_text




if __name__ == '__main__':
    count = 0
    myMaterial = Material()
    accessToken = Basic().get_access_token()
    picname = os.listdir('D:\\material\picture\cover')
    for i in picname:
        filePath = "D:\\material\picture\cover\%s" % (i)
        mediaType = "image"
        myMaterial.uplaod(accessToken, filePath, mediaType,i)
        count = count + 1
        if count >= 5:
            print "start rest"
            time.sleep(3)
            print "continue upload"
            count = 0


    #img_text 是个dict类型，可通过下面方式修改内容
    # dict类型便于修改
    #img_text['articles'][0]['title'] = u"测试".encode('utf-8')
    #print img_text['articles'][0]['title']

    # img_text = json.dumps(img_text, ensure_ascii=False)  # 将dict转为str，用于发送
    # myMaterial.add_news(accessToken, img_text)