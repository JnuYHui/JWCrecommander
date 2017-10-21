#!/usr/bin/env python
# -*-coding:utf-8-*-
# filename: media_up.py
'''
@author: YHui

@contact: ywhui@outlook.com.com

@software: pycharm

@file: media_up.py

@time: 2017/8/30 14:23

'''
from basic import Basic
# import urllib2
import requests
import os
import poster.encode
from poster.streaminghttp import register_openers


class Media(object):
    def __init__(self):
        register_openers()

    # 上传图片
    def uplaod(self, accessToken, filePath, mediaType,name):
        # 接下来的部分，是请求的官方部件，不过不能用，用requests库很多问题，还是继续用官方的版本比较稳妥
        # param = {'media': openFile}
        # postData, postHeaders = poster.encode.multipart_encode(param)
        # postUrl = "https://api.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=%s" % (accessToken, mediaType)
        # request = urllib2.Request(postUrl, postData, postHeaders)
        # urlResp = urllib2.urlopen(request)
        # 结束上传请求
        # 此处代码可用，关键在于提交足够的表头
        openFile = open(filePath, "rb")
        postUrl = "https://api.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=%s" % (accessToken, mediaType)
        files = {'media': ('%s' % (name), openFile, 'image/png')}
        urlResp = requests.post(postUrl, files=files)

        openFile.close()
        urlResp.json()
        media_id = urlResp["media_id"]
        fmediaId = open("media.txt", 'a')
        fmediaId.write(filePath[22:])
        fmediaId.write('\t')
        fmediaId.write(media_id)
        fmediaId.write('\n')
        fmediaId.close()
        print urlResp


if __name__ == '__main__':
    myMedia = Media()
    accessToken = Basic().get_access_token()
    picname = os.listdir('D:\\material\picture\cover')
    for i in picname:
        filePath = "D:\\material\picture\cover\%s" % (i)
        mediaType = "image"
        myMedia.uplaod(accessToken, filePath, mediaType,i)
