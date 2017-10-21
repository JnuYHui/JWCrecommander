#!/usr/bin/env python
# -*-coding:utf-8-*-
# filename: basic.py
'''
@author: YHui

@contact: ywhui@outlook.com.com

@software: pycharm

@file: basic.py

@time: 2017/8/30 12:06

'''
import requests
import time
import datetime
from ATfunction import ATmanager


class Basic:
    def __init__(self):
        # self.token_dic = dict()
        self.__accessToken = ''
        self.__leftTime = 0
        # self.__startTime = 0
        # self.__endTime = 0
        self.__aTcode = ATmanager()
    
    # self.tokenId = 1
    
    
    def __real_get_access_token(self):
        # 需要传入的参数
        appId = "wx4efb08c772d3848d"
        appSecret = "489f3a9daffc218328763c410119fb16"
        
        postUrl = (
        "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (appId, appSecret))
        # 获取access-token
        urlResp = requests.get(postUrl)
        startTime = datetime.datetime.now()
        # self.token_dic['tokenId'] = self.tokenId
        
        # 对返回的json包进行解码
        urlResp = urlResp.json()
        # 获取包中的参数
        self.__accessToken = urlResp['access_token']
        self.__leftTime = urlResp['expires_in']
        endTime = startTime + datetime.timedelta(seconds=self.__leftTime)
        self.__aTcode.ATsave(self.__accessToken, endTime)
        print "-----NEW TOKEN-----"
        print self.__accessToken
        print startTime
        # print '一个新表已经创建'
        return self.__accessToken

        # 调用access-token
        # 接下来从数据库中取得accessToken的方法还没确定，思路有两种
        # 第一是从这个方法里面提取，第二个是从数据库里面提取
        # 其实本人更倾向于直接调用从数据库里面提取的方法
        # 而这个程序将变为直接对数据库进行更新的过程
    def get_access_token(self):
        if self.__leftTime < 10:
            self.__real_get_access_token()
            # else:
            # self.__accessToken = self.__aTcode.ATget()
        return self.__accessToken
    
    # 运行整个模块，应该放置在主程序里面
    def run(self):
        while (True):
            # if self.__aTcode.TableCreate() == None:
            #     print '1'
            #     self.__real_get_access_token()
            #     return self.__accessToken
            
            # else:
            if self.__leftTime > 60:
                print '1',
                time.sleep(2)
                self.__leftTime -= 2
                # return self.__accessToken
            else:
                print '2'
                self.__real_get_access_token()
                # return self.__accessToken
                
                
                # 判读已经获得的access-token的剩余时间
                # 但在应用中应该先将access-token获取，然后再判断是否要调用
                # if self.__leftTime > 10:
                #     time.sleep(2)
                #     self.__leftTime -= 2
                #     return self.__accessToken
                # else:
                #     self.__real_get_access_token()
                #     return self.__accessToken


if __name__ == '__main__':
    # at = ATmanager()
    # at.TableCreate()
    # print 'chenggongchuangjian'
    
    basic = Basic()
    token = basic.run()
    
    print datetime.datetime.now()
    print token
