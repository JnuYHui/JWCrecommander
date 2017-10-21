#!/usr/bin/env python
#-*-coding:utf-8-*-
# filename: media_down.py
'''
@author: YHui

@contact: ywhui@outlook.com.com

@software: pycharm

@file: media_down.py

@time: 2017/8/30 16:55

'''
# -*- coding: utf-8 -*-
# filename: media.py
import urllib2
import json
from basic import Basic

class Media(object):
    def get(self, accessToken, mediaId):
        postUrl = "https://api.weixin.qq.com/cgi-bin/media/get?access_token=%s&media_id=%s" % (accessToken, mediaId)
        urlResp = urllib2.urlopen(postUrl)

        headers = urlResp.info().__dict__['headers']
        if ('Content-Type: application/json\r\n' in headers) or ('Content-Type: text/plain\r\n' in headers):
            jsonDict = json.loads(urlResp.read())
            print jsonDict
        else:
            buffer = urlResp.read()   #素材的二进制
            mediaFile = file("%s.jpg" % (mediaId), "wb")
            mediaFile.write(buffer)
            print "get successful"
if __name__ == '__main__':
    myMedia = Media()
    accessToken = Basic().get_access_token()
    # 按实际情况填入mediaId
    mediaId = ""
    myMedia.get(accessToken, mediaId)