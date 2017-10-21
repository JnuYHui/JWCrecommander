# -*- coding: utf-8 -*-
"""
Spyder Editor
BY J
"""
import pymysql


class ATmanager:
    def TableCreate(self):
        db = pymysql.connect(host='127.0.0.1', port=3306, user='JNU', passwd='123456', charset='utf8')
        cursor = db.cursor()
        cursor.execute("use accesstoken")
        sql = "create table token(accesstoken    varchar(500),date    datetime)"
        cursor.execute(sql)
        db.close()
        print '成功创建'
        return None
    
    def ATsave(self, accesstoken, date):
        db = pymysql.connect(host='127.0.0.1', port=3306, user='JNU', passwd='123456', charset='utf8')
        cursor = db.cursor()
        cursor.execute("use accesstoken")
        sql = "insert into token(accesstoken,date) values('{}','{}')".format(str(accesstoken), date)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
    
    def ATget(self):
        import re
        db = pymysql.connect(host='127.0.0.1', port=3306, user='JNU', passwd='123456', charset='utf8')
        cursor = db.cursor()
        cursor.execute("use accesstoken")
        sql = 'select accesstoken from Accesstoken where date in (select MAX(date) from Accesstoken)'
        cursor.excute(sql)
        rows = cursor.fetchall()
        a = re.findall(r"[^\(*\)*\,*]", str(rows))
        AT = ''.join(a)
        cursor.close()
        db.close()
        return AT