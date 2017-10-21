#!/usr/bin/env python
#-*-coding:utf-8-*-
# filename: event_parse.py
'''
@author: YHui

@contact: ywhui@outlook.com.com

@software: pycharm

@file: event_parse.py

@time: 2017/9/1 12:57

'''
# 用于处理事件消息
import reply

def EventParse(recMsg):
    MsgEvent = recMsg.Event
    toUser = recMsg.FromUserName
    fromUser = recMsg.ToUserName
    print MsgEvent
    # accessToken = self.__accessToken
    if MsgEvent == 'CLICK':
        print recMsg.Eventkey
        if recMsg.Eventkey == 'NEW_NOTICE':
            content = u"编写中，马上就能看到通知了呢".encode('utf-8')
            # 此处事件消息本应回复更复杂的内容，但因为权限问题，只能使用简单的文本消息回复
            replyMsg = reply.TextMsg(toUser, fromUser, content)
            return replyMsg.send()
        if recMsg.Eventkey == 'OLD_NOTICE':
            content = u"过去的已成云烟，将来的还未出现，只有现在，摆你面前".encode('utf-8')
            replyMsg = reply.TextMsg(toUser, fromUser, content)
            print replyMsg
            return replyMsg.send()
    
    if MsgEvent == 'subscribe':
        content = "欢迎来到校问，我是有知识、有内涵、声音超萌还健谈的校问机器人。\n回复“help”，看看怎么和我交(tiao)朋(qing)友吧(｡･ω･｡)"
        replyMsg = reply.TextMsg(toUser, fromUser, content)
        return replyMsg.send()
    
    else:
        content = "还在测试中"
        replyMsg = reply.TextMsg(toUser, fromUser, content)
        
        return replyMsg.send()
    