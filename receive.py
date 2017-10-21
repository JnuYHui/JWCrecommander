#!/usr/bin/env python
#-*-coding:utf-8-*-
# filename: receive.py
'''
@author: YHui

@contact: ywhui@outlook.com.com

@software: pycharm

@file: receive.py

@time: 2017/8/29 17:04

'''


# 本模块用于处理接收到的xml包


import xml.etree.ElementTree as ET


def parse_xml(web_data):
    if len(web_data) == 0:
        return None
    xmlData = ET.fromstring(web_data)
    # print type(xmlData)
    msg_type = xmlData.find('MsgType').text
    # 接下来的条件语句按照可能接受到的消息类型分类
    if msg_type == 'text':
        return TextMsg(xmlData)
    elif msg_type == 'image':
        return ImageMsg(xmlData)
    elif msg_type == 'voice':
        return VoiceMsg(xmlData)
    elif msg_type == 'event':
        event_type = xmlData.find('Event').text
        if event_type == 'CLICK':
            return Click(xmlData)
        # elif event_type in ('subscribe', 'unsubscribe'):
        #   return Subscribe(xmlData)
        # elif event_type == 'VIEW':
        #   return View(xmlData)
        # elif event_type == 'LOCATION':
        #   return LocationEvent(xmlData)
        # elif event_type == 'SCAN':
        #   return Scan(xmlData)

        return EventMsg(xmlData)


class Msg(object):
    def __init__(self, xmlData):
        self.ToUserName = xmlData.find('ToUserName').text
        self.FromUserName = xmlData.find('FromUserName').text
        self.CreateTime = xmlData.find('CreateTime').text
        self.MsgType = xmlData.find('MsgType').text
        self.MsgId = xmlData.find('MsgId').text


# 接下来每一个类的实例化中都会调用Msg并且将其实例化，所以，经过parse_xml处理的data都会变成Msg的实例

# 文字消息
class TextMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.MsgType = xmlData.find('MsgType').text
        self.Content = xmlData.find('Content').text.encode("utf-8")

# 图片消息
class ImageMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.MsgType = xmlData.find('MsgType').text
        self.PicUrl = xmlData.find('PicUrl').text
        self.MediaId = xmlData.find('MediaId').text

# 语音消息
class VoiceMsg(Msg):
    def __init__(self,xmlData):
        Msg.__init__(self,xmlData)
        self.MsgType = xmlData.find('MsgType').text
        self.Recognition = xmlData.find('Recognition').text
        self.MediaId = xmlData.find('MediaId').text


# 事件消息
class EventMsg(object):
    def __init__(self, xmlData):
        self.ToUserName = xmlData.find('ToUserName').text
        self.FromUserName = xmlData.find('FromUserName').text
        self.CreateTime = xmlData.find('CreateTime').text
        self.MsgType = xmlData.find('MsgType').text
        self.Event = xmlData.find('Event').text
# 点击菜单
class Click(EventMsg):
    def __init__(self, xmlData):
        EventMsg.__init__(self, xmlData) #继承了EventMsg类，可以用于主函数的判断
        self.Eventkey = xmlData.find('EventKey').text

class Subscribe(EventMsg):
    def __int__(self,xmlData):
        EventMsg.__init__(self,xmlData)