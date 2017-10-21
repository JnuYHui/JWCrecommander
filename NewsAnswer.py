#!/usr/bin/env python
#-*-coding:utf-8-*-
"""
Created on Fri Sep  1 19:46:53 2017

@author: as
"""

import pymysql
import sys

class newsAnswer:
    
    def getnews1key(self,keyword):
        db = pymysql.connect(host='127.0.0.1', port=3306, user='JNU', passwd='123456', charset='utf8')
        cursor = db.cursor()
        cursor.execute("use jnu")
        # 转码
        reload(sys)
        sys.setdefaultencoding('utf-8')

        sql = 'select 通知名称,通知链接,通知时间 from news2 where 通知名称 LIKE "%{}%" order by 通知时间 desc'.format(keyword)
        cursor.execute(sql)
        all_result = list(cursor.fetchall())
        if len(all_result) >= 5:
            all_result_list = all_result[0:5]
        elif len(all_result) == 0:
            all_result_list = []
        #     修改
        else:
            l = len(all_result)
            all_result_list = all_result[0:l]
        cursor.close()
        db.close()
        return all_result_list
    
    def getnews2key(self,keyword1,keyword2):
        db = pymysql.connect(host='127.0.0.1', port=3306, user='JNU', passwd='123456', charset='utf8')
        cursor = db.cursor()
        cursor.execute("use jnu")
        # print '11'
        # 转码
        reload(sys)
        sys.setdefaultencoding('utf-8')

        sql = 'select 通知名称,通知链接,通知时间 from news1 where 通知名称 LIKE "%{}%" or 通知名称 LIKE "%{}%" order by 通知时间 desc;'.format(
            keyword1, keyword2)
        cursor.execute(sql)
        all_result = list(cursor.fetchall())
        # print '12'
        if len(all_result) >= 5:
            all_result_list = all_result[0:5]
        elif len(all_result) == 0:
            all_result_list = []
        else:
            l = len(all_result)
            all_result_list = all_result[0:l]
        cursor.close()
        db.close()
        return all_result_list
        
        
        # ALL_result_list = []
        # for i in range(5):
        #     result_list = []
        #     try:
        #         result = all_result[i+1]
        #         result_list.append(result[0])
        #         result_list.append(result[1])
        #         result_list.append(result[2])#怎么输出  再次调用怎么输出后五条  还有不是五的整数
        #         ALL_result_list.append(result_list)
        #     except:
        #         continue
        # cursor.close()
        # db.close()
        # return all_result_list