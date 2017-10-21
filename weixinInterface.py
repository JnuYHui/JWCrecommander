#!/usr/bin/env python
#-*-coding:utf-8-*-
# filename: weixinInterface.py
'''
@author: YHui

@contact: ywhui@outlook.com.com

@software: pycharm

@file: weixinInterface.py

@time: 2017/8/29 17:03

'''
import hashlib
import web
import lxml
import time
import os
import urllib2, json
from lxml import etree
import reply
import receive
from basic import Basic
from msg_parse import MsgParse
import event_parse



class WeixinInterface:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)  # 实例化模板
        


    def GET(self):
        # 获取输入参数
        data = web.input()
        if len(data) == 0:
            return "hello, this is handle view"
        signature = data.signature
        timestamp = data.timestamp
        nonce = data.nonce
        echostr = data.echostr
        # 自己的token
        token = "ywhui"

        # 字典序排序
        list = [token, timestamp, nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, list)
        hashcode = sha1.hexdigest()
        # sha1加密算法

        # 如果是来自微信的请求，则回复echostr
        if hashcode == signature:
            return echostr
        else:
            return ""


    def POST(self):
        try:
            webData = web.data()
            print "----------------------------------------------"
            print "Handle Post webdata is ", webData  # 后台打日志
            
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg): #判断已经收到的信息是否属于Msg
                msgparse = MsgParse(recMsg)
                replyMsg = msgparse.parse(recMsg)
                print type(replyMsg)
                return replyMsg
                
            elif isinstance(recMsg, receive.EventMsg):
                replyMsg = event_parse.EventParse(recMsg)
                print type(replyMsg)
                return replyMsg


            else:
                print "暂且不处理"
                return "success"
            
        except Exception, Argment:
            return Argment