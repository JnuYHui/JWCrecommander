#!/usr/bin/env python
#-*-coding:utf-8-*-
# filename: reply.py
'''
@author: YHui

@contact: ywhui@outlook.com.com

@software: pycharm

@file: reply.py

@time: 2017/8/29 17:05

'''
import time
import web

class Msg(object):
    def __init__(self):
        pass

    def send(self):
        return "success"

# 文本消息
class TextMsg(Msg):
    def __init__(self, toUserName, fromUserName, repcontent):
        self.ToUserName = toUserName
        self.FromUserName = fromUserName
        self.CreateTime = int(time.time())
        self.Content = repcontent
        self.render = web.template.render('templates/')


    def send(self):
        # print self.render.reply_text(self.ToUserName, self.FromUserName, self.CreateTime, self.Content)
        return self.render.reply_text(self.ToUserName, self.FromUserName, self.CreateTime, self.Content)
        # return XmlForm.format(**self.__dict)

# 图文消息
class ImgText(Msg):
    def __init__(self,toUserName, fromUserName, contentlist):
        self.ToUserName = toUserName
        self.FromUserName = fromUserName
        self.CreateTime = int(time.time())
        self.ContentList = contentlist
        self.picurlLargeU = 'https://farm5.staticflickr.com/4411/36185490713_778cab2ae2_o.png'
        self.picurlMinU = 'https://farm5.staticflickr.com/4342/36596698940_50d761cc0b_o.png'
        self.render = web.template.render('templates/')
    
    # @property
    def send(self):
        # 未完成
        if len(self.ContentList) == 1:
            title1 = self.ContentList[0][0]
            url1 = self.ContentList[0][1]
            description1 = '通知时间' + str(self.ContentList[0][2])
            return self.render.reply_imgtext1(self.ToUserName,self.FromUserName,self.CreateTime,self.picurlLargeU,title1,description1,url1)
        
        elif len(self.ContentList) == 2:
            # text1
            title1 = self.ContentList[0][0]
            url1 = self.ContentList[0][1]
            description1 = '通知时间' + str(self.ContentList[0][2])
            # text2
            title2 = self.ContentList[1][0]
            url2 = self.ContentList[1][1]
            description2 = '通知时间' + str(self.ContentList[1][2])
            return self.render.reply_imgtext2(self.ToUserName,self.FromUserName,self.CreateTime,self.picurlLargeU,self.picurlMinU,\
                                              title1,description1,url1,\
                                              title2,description2,url2)
        
        elif len(self.ContentList) == 3:
            # text1
            title1 = self.ContentList[0][0]
            url1 = self.ContentList[0][1]
            description1 = '通知时间' + str(self.ContentList[0][2])
            # text2
            title2 = self.ContentList[1][0]
            url2 = self.ContentList[1][1]
            description2 = '通知时间' + str(self.ContentList[1][2])
            # text3
            title3 = self.ContentList[2][0]
            url3 = self.ContentList[2][1]
            description3 = '通知时间' + str(self.ContentList[2][2])
            return self.render.reply_imgtext3(self.ToUserName, self.FromUserName, self.CreateTime, self.picurlLargeU,self.picurlMinU,\
                                              title1, description1, url1, \
                                              title2, description2, url2, \
                                              title3, description3, url3)
        elif len(self.ContentList) == 4:
            # text1
            title1 = self.ContentList[0][0]
            url1 = self.ContentList[0][1]
            description1 = '通知时间' + str(self.ContentList[0][2])
            # text2
            title2 = self.ContentList[1][0]
            url2 = self.ContentList[1][1]
            description2 = '通知时间' + str(self.ContentList[1][2])
            # text3
            title3 = self.ContentList[2][0]
            url3 = self.ContentList[2][1]
            description3 = '通知时间' + str(self.ContentList[2][2])
            # text4
            title4 = self.ContentList[3][0]
            url4 = self.ContentList[3][1]
            description4 = '通知时间' + str(self.ContentList[3][2])
            return self.render.reply_imgtext4(self.ToUserName, self.FromUserName, self.CreateTime, self.picurlLargeU,self.picurlMinU,\
                                              title1, description1, url1, \
                                              title2, description2, url2, \
                                              title3, description3, url3, \
                                              title4, description4, url4)
            
        elif len(self.ContentList) == 5:
            # text1
            title1 = self.ContentList[0][0]
            url1 = self.ContentList[0][1]
            description1 = '通知时间' + str(self.ContentList[0][2])
            # text2
            title2 = self.ContentList[1][0]
            url2 = self.ContentList[1][1]
            description2 = '通知时间' + str(self.ContentList[1][2])
            # text3
            title3 = self.ContentList[2][0]
            url3 = self.ContentList[2][1]
            description3 = '通知时间' + str(self.ContentList[2][2])
            # text4
            title4 = self.ContentList[3][0]
            url4 = self.ContentList[3][1]
            description4 = '通知时间' + str(self.ContentList[3][2])
            # text5
            title5 = self.ContentList[3][0]
            url5 = self.ContentList[3][1]
            description5 = '通知时间' + str(self.ContentList[3][2])
            return self.render.reply_imgtext5(self.ToUserName, self.FromUserName, self.CreateTime, self.picurlLargeU,self.picurlMinU, \
                                              title1, title2, title3, title4, title5, description1, description2,\
                                              description3, description4, description5, url1, url2, url3, url4, url5)

# 图片消息
class ImageMsg(Msg):
    def __init__(self, toUserName, fromUserName, mediaId):
        self.ToUserName = toUserName
        self.FromUserName = fromUserName
        self.CreateTime = int(time.time())
        self.MediaId = mediaId
        # print "MediaId:", self.MediaId
        self.render = web.template.render('templates/')

    def send(self):
        # print self.ToUserName, self.FromUserName, self.CreateTime, self.MediaId
        # print self.render.reply_img(self.ToUserName, self.FromUserName, self.CreateTime, self.MediaId)
        return self.render.reply_img(self.ToUserName, self.FromUserName, self.CreateTime, self.MediaId)


# 事件消息
class EventMsg(Msg):
    def __init__(self, toUserName, fromUserName, mediaId):
        self.ToUserName = toUserName
        self.FromUserName = fromUserName
        self.CreateTime = int(time.time())
        self.MediaId = mediaId
        print "MediaId:", self.MediaId
        self.render = web.template.render('templates/')

    def send(self):
        return self.render.reply_img(self.ToUserName, self.FromUserName, self.CreateTime, self.MediaId)
