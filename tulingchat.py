#!/usr/bin/env python
#-*-coding:utf-8-*-
# filename: tulingchat.py
'''
@author: YHui

@contact: ywhui@outlook.com.com

@software: pycharm

@file: tulingchat.py

@time: 2017/9/1 15:21

'''

# 用于将问题输入给图灵机器人，返回相应答案

# import json
import requests
import traceback


class TulingAutoReply:
    def __init__(self):
        self.key = 'ee5d14cbae0340beb35ababae426cf06'
        self.url = 'http://www.tuling123.com/openapi/api'
    
    def reply(self, unicode_str,userid):
        body = {'key': self.key, 'info': unicode_str,'userid':userid}
        r = requests.post(self.url, data=body)
        print 'r',r
        ans = r.json()
        return ans
        
    
    def analsys(self,ans):
        try:
            # 判断返回的消息类型，获取消息内容
            if ans['code'] == 200000:
                return ans['url']
            if ans['code'] == 40004 or ans['code'] == 40007 or ans['code'] == 40002 or ans['code'] == 40004 :
                text = '哎呦，好像出错了'
                self.key = '53d7ac65ccdf4533b0064004d9f76fd4'
                return text
            else:
                text = ans['text'].encode('utf-8')
                return text
        except Exception:
            traceback.print_exc()
            return None