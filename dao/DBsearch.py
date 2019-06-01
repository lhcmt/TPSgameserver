#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
import  logging
from config import *

#根据用户名查询密码
def searchUserIDandPassword(userID,password):
    #数据库操作
    conn = sqlite3.connect('./dao/gamedata.db')
    cursor = conn.cursor()
    cursor.execute('select * from user where id=?', (userID,))
    values = cursor.fetchall()
    cursor.close()
    conn.close()

    if (values):
        if(password == values[0][1]):
            return PASSWORD_CORRECT
        else:
            return PASSWORD_ERROR
    else:
        return USER_ID_ERROR


