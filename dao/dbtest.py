#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3

def insert():

    cursor.execute('create table user (id varchar(20) primary key, password varchar(20))')
    cursor.execute("insert into user (id, password) values ('lhcmt', '123456')")
    print cursor.rowcount
    conn.commit()


def search():
    cursor.execute('select * from user where id=?', ('lhcmt',))
    values = cursor.fetchall()

    if(values):
        print values[0][1]

    else:
        print 'cant find'



conn = sqlite3.connect('gamedata.db')
cursor = conn.cursor()

search()

cursor.close()
conn.close()