#!/usr/bin/env python
#-*-coding:utf-8-*-
# filename: menu.py
'''
@author: YHui

@contact: ywhui@outlook.com.com

@software: pycharm

@file: menu.py

@time: 2017/8/30 14:12

'''
import urllib
from basic import Basic
import requests



class Menu(object):
    def __init__(self):
        pass

    def create(self, postData, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % accessToken
        if isinstance(postData, unicode):
            postData = postData.encode('utf-8')
        urlResp = requests.post(url=postUrl, data=postData)
        print urlResp

    def query(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/get?access_token=%s" % accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read()

    def delete(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=%s" % accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read()
  
    # 获取自定义菜单配置接口
    def get_current_selfmenu_info(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/get_current_selfmenu_info?access_token=%s" % accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read()


if __name__ == '__main__':
    # def run(self):
    myMenu = Menu()
    postJson = """
      {
          "button":
          [
             
              {
                  "name": "最新通知",
                  "sub_button":
                  [
                      {
                          "type": "click",
                          "name": "最新通知",
                          "key":"NEW_NOTICE"
                      },
                      {
                          "type": "click",
                          "name": "历史通知",
                          "key":"OLD_NOTICE"
                      },
                      
                  ]
              },
              {
                  "name": "校园生活",
                  "sub_button":
                  [
                      {
                          "type": "click",
                          "name": "美美的壁纸",
                          "key":"BACK_GROUND"
                      },
                      {
                          "type": "click",
                          "name": "生活指南",
                          "key":"LIFE_GUIDE"
                      }
                  
                  ]
              }
            ]
      }
      """
    accessToken = Basic().get_access_token()
    # myMenu.delete(accessToken)
    myMenu.create(postJson, accessToken)