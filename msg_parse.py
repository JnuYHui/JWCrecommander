#!/usr/bin/env python
#-*-coding:utf-8-*-
# filename: msg_parse.py
'''
@author: YHui

@contact: ywhui@outlook.com.com

@software: pycharm

@file: msg_parse.py

@time: 2017/9/1 12:56

'''
# from jieba import analyse
import reply
import jieba
import jieba.analyse
from tulingchat import TulingAutoReply
from NewsAnswer import newsAnswer

# 文本处理
class MsgParse():
    def __init__(self,recMsg):
        self.__toUser = recMsg.FromUserName
        self.__fromUser = recMsg.ToUserName
        self.__msgType = recMsg.MsgType
        self.__face = [['/::)','微笑'],['/::~','伤心'],['/::B','美女'],['/::|','发呆'],['/:8-)','墨镜'],['/::<','哭'],['/::$','羞'],['/::X','哑'],['/::Z','睡'],['/::’(','哭'],['/::-|','囧'],['/::@','怒'],['/::P','调皮'],['/::D','笑'],['/::O','惊讶'],['/::(','难过'],['/::+','酷'],['/:–b','汗'],['/::Q','抓狂'],['/::T','吐'],['/:,@P','笑'],['/:,@-D','快乐'],['/::d','奇'],['/:,@o','傲'],['/::g','饿'],['/:|-)','累'],['/::!','吓'],['/::L','汗'],['/::>','高兴'],['/::,@','闲'],['/:,@f','努力'],['/::-S','骂'],['/:?','疑问'],['/:,@x','秘密'],['/:,@@','乱'],['/::8','疯'],['/:,@!','哀'],['/:!!!','鬼'],['/:xx','打击'],['/:bye','bye'],['/:wipe','汗'],['/:dig','抠'],['/:handclap','鼓掌'],['/:&-(','糟糕'],['/:B-)','恶搞'],['/:<@','什么'],['/:@>','什么'],['/::-O','累'],['/:>-|','看'],['/:P-(','难过'],['/::’|','难过'],['/:X-)','坏'],['/::*','亲'],['/:@x','吓'],['/:8*','可怜'],['/:pd','刀'],['/:<W>','水果'],['/:beer','酒'],['/:basketb','篮球'],['/:oo','乒乓'],['/:coffee','咖啡'],['/:eat','美食'],['/:pig','动物'],['/:rose','鲜花'],['/:fade','枯'],['/:showlove','唇'],['/:heart','爱'],['/:break','分手'],['/:cake','生日'],['/:li','电']]
        self.__newsanswer = newsAnswer()
    def parse(self,recMsg):
        toUser = self.__toUser
        fromUser = self.__fromUser
        msgType = self.__msgType
        count = 0
        print self.__msgType
        if msgType == 'text':
            # print 1
            content = recMsg.Content
            # print 2
            # 文本的处理
            if content.lower() == 'help':
                repcontent = u"说句话，让我陪你聊聊天\n问个问题，让我帮你找找有没有相关通知(仅开通暨南大学)\n说个你好,打个招呼吧"
                # print repcontent
                replyMsg = reply.TextMsg(toUser, fromUser, repcontent)
                # print replyMsg
                return replyMsg.send()
            
            else:
                # 处理微信表情
                for i in self.__face:
                    content = content.replace(i[0],i[1])
                # print '0'
                keywords = self.getKey(content)
                print keywords
                # for i in keywords:
                #     print type(i)

                if len(keywords) == 0:
                    # print '7'
                    userid = toUser.replace('-', '0')
                    tuling = TulingAutoReply()
                    ans = tuling.reply(content, userid)
                    repcontent = tuling.analsys(ans)
                    replyMsg = reply.TextMsg(toUser, fromUser, repcontent)
                    return replyMsg.send()
                else:
                    # print '8'
                    # 获取数据库中的通知
                    if len(keywords) == 1:
                        # print '9'
                        resultList = self.__newsanswer.getnews1key(keywords[0])
                        
                    elif len(keywords) == 2:
                        # print '10'
                        resultList = self.__newsanswer.getnews2key(keywords[0],keywords[1])
                        
                    if len(resultList) == 0:
                        # print '1'
                        userid = toUser.replace('-', '0')
                        tuling = TulingAutoReply()
                        ans = tuling.reply(content, userid)
                        repcontent = tuling.analsys(ans)
                        replyMsg = reply.TextMsg(toUser, fromUser, repcontent)
                        return replyMsg.send()
                    else:
                        # print '2'
                        replyMsg = reply.ImgText(toUser, fromUser, resultList)
                        return replyMsg.send()


                        # userid = toUser.replace('-','0')
                # tuling = TulingAutoReply()
                # ans = tuling.reply(content,userid)
                # repcontent = tuling.analsys(ans)
                # print repcontent
            # replyMsg = reply.TextMsg(toUser, fromUser, repcontent)
            # # print replyMsg
            # return replyMsg.send()
        elif msgType == 'image':
            mediaId = recMsg.MediaId
            replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
            return replyMsg.send()
        elif msgType == 'voice':
            content = recMsg.Recognition
            # 文本的处理
            if content == 'help':
                repcontent = u"随便输句话，让我陪你聊聊天\n随便输个问题，让我帮你找找看有没有相关通知\n先说个你好,打个招呼吧（可以直接用语音提问哦）"
                # print repcontent
            else:
                userid = toUser.replace('-', '0')
                tuling = TulingAutoReply()
                ans = tuling.reply(content, userid)
                repcontent = tuling.analsys(ans)
                # print repcontent
            replyMsg = reply.TextMsg(toUser, fromUser, repcontent)
            # print replyMsg
            return replyMsg.send()
            
        else:
            return reply.Msg().send()


    # 文本的分析
    def getKey(self,content):
        tk = jieba.analyse.textrank
        # print '3'
        keyword = list(jieba.cut(content,cut_all=False))
        # print '4'
        if len(keyword) > 1:
            keywords = list(tk(content,topK=2))
            # print '5'
        else:
            keywords = keyword
            # print '6'
            
        return keywords
    

    