#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time  : 2019/5/19 15:26
# @Author: Junzhe_Zhang
import pymysql
import os
import json

def return_files(rootDir):
    list_dirs = os.walk(rootDir)
    funfiles=[]
    for root, dirs, files in list_dirs:
        for f in files:
            funfiles.append(os.path.join(root, f))
    return funfiles

connection = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             password='123456',
                             db='net',
                             charset='utf8')
num=0
files=return_files('file')
for file in files:c:\''
    print(file)
    with open(file,encoding='utf8') as fr:
        for line in fr.readlines():
            try:
                m=json.loads(line)
            except json.decoder.JSONDecodeError:
                num+=1
                continue
            # for key in m:
            #     print(m[key])
            # m={'key1':'1','key2':'3','key3':'3'}
            cmd = 'insert into darkweb ('
            for key in m:
                cmd += "`" + key + "`,"
            cmd = cmd[:-1]
            cmd += ') values ('
            for key in m:
                temp_thing=json.dumps(m[key])
                if(temp_thing=="[]"):
                    temp_thing='"[]"'
                cmd += temp_thing + ","
            cmd = cmd[:-1]
            cmd += ');'
            # print(cmd)
            # break
            cursor = connection.cursor()
            try:
                effect_row = cursor.execute(
                    cmd
                    )
            except pymysql.err.ProgrammingError:
                continue
            connection.commit()
            # break
print(num)